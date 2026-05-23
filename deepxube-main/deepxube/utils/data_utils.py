""" IO, multiprocessing-queue, and numpy-array plumbing used across DeepXube.

Includes: a ``Logger`` that tees stdout to a file, non-blocking queue helpers,
list-of-ndarray indexing and concatenation, and a pickleable ``SharedNDArray``
that lets worker processes share numpy buffers via POSIX/Windows shared memory.
"""

from typing import List, Any, Tuple, Optional, Type, cast

import sys

from multiprocessing import Queue
import queue
import os
import shutil
import numpy as np
from numpy.typing import NDArray, ArrayLike

from multiprocessing import shared_memory
from multiprocessing.shared_memory import SharedMemory


class Logger(object):
    """ Stdout-compatible file logger that tees writes to both a file and
    (optionally) the real terminal.

    Instantiate and assign to ``sys.stdout`` to capture all prints to a log
    file while still showing them on screen.
    """

    def __init__(self, filename: str, mode: str = "a", echo: bool = True):
        """ Open the log file and snapshot the current stdout.

        :param filename: Path to the log file.
        :param mode: ``open()`` mode; ``"a"`` appends, ``"w"`` overwrites.
        :param echo: If ``True`` (default) writes also go to the original
            stdout; if ``False`` they go only to the file.
        """
        self.terminal = sys.stdout
        self.log = open(filename, mode)
        self.echo: bool = echo

    def write(self, message: str) -> None:
        """ Write ``message`` to the log file (and to the terminal if
        ``echo`` is ``True``), flushing the file afterwards.

        :param message: String to write.
        """
        if self.echo:
            self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

    def flush(self) -> None:
        """ No-op; stdout file objects must define ``flush``, but this
        logger flushes on every ``write``.
        """
        pass


def get_nowait_noerr(q: Queue) -> Any:
    """ Non-blocking ``queue.get_nowait`` that swallows the ``Empty``
    exception and returns ``None`` instead.

    :param q: The multiprocessing queue.
    :return: The dequeued value, or ``None`` if the queue was empty.
    """
    try:
        q_ret: Any = q.get_nowait()
        return q_ret
    except queue.Empty:
        return None


def get_while_not_empty(q: Queue) -> List[Any]:
    """ Drain all currently-available items from ``q`` without blocking.

    :param q: The multiprocessing queue.
    :return: List of items drained. Empty if the queue was empty at the
        start of the call.
    """
    q_rets: List[Any] = []

    while not q.empty():
        try:
            q_ret: Any = q.get_nowait()
            q_rets.append(q_ret)
        except queue.Empty:
            break

    return q_rets


def get_in_order(q: Queue, num: int) -> List[Any]:
    """ Pull ``num`` ``(idx, val)`` pairs from ``q`` and return them as a
    list positioned by ``idx``.

    Workers put ``(idx, payload)`` tuples onto the queue; this reorders the
    arrivals so the caller gets deterministic indexing regardless of which
    worker completed first.

    :param q: Queue from which workers publish ``(idx, val)`` tuples.
    :param num: Number of items to read.
    :return: List of length ``num`` with ``ret_vals[idx] = val``.
    """
    ret_vals: List[Any] = [None for _ in range(num)]
    for _ in range(num):
        idx, val = q.get()
        ret_vals[idx] = val
    return ret_vals


def copy_dir_files(src_dir: str, dest_dir: str) -> None:
    """ Copy every regular file from ``src_dir`` into ``dest_dir``.

    Subdirectories are ignored. Destination must already exist.

    :param src_dir: Source directory path.
    :param dest_dir: Destination directory path.
    """
    src_files: List[str] = os.listdir(src_dir)
    for file_name in src_files:
        full_file_name: str = os.path.join(src_dir, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_dir)


def sel_l(data_l: List[NDArray], idxs: NDArray) -> List[NDArray]:
    """ Index every array in a list with the same row indices.

    :param data_l: List of numpy arrays sharing axis-0 length.
    :param idxs: Row indices to select from each array.
    :return: A parallel list where each element is ``arr[idxs]``.
    """
    data_l_sel: List[NDArray] = []
    for np_idx in range(len(data_l)):
        data_l_sel.append(data_l[np_idx][idxs])

    return data_l_sel


def combine_l_l(l_l: List[List[NDArray]], comb: str) -> List[NDArray]:
    """ Combine a list of per-item ndarray lists into a single per-position
    ndarray list by either concatenating or stacking.

    Given ``[[a1, b1], [a2, b2], ...]`` returns ``[comb(a1,a2,...), comb(b1,b2,...)]``.

    :param l_l: Outer list: one entry per item; inner list: one ndarray per
        position. Inner lists must all have the same length.
    :param comb: ``"concat"`` for ``np.concatenate`` along axis 0;
        ``"stack"`` for ``np.stack`` along axis 0.
    :return: List of combined ndarrays, same length as ``l_l[0]``.
    :raises ValueError: If ``comb`` is neither ``"concat"`` nor ``"stack"``.
    """
    l_l_comb: List[NDArray] = []
    for np_idx in range(len(l_l[0])):
        l_l_idx: List[NDArray] = [x[np_idx] for x in l_l]

        l_l_idx_comb: NDArray
        if comb == "concat":
            l_l_idx_comb = np.concatenate(l_l_idx, axis=0)
        elif comb == "stack":
            l_l_idx_comb = np.stack(l_l_idx, axis=0)
        else:
            raise ValueError(f"Unknown comb method {comb}")

        l_l_comb.append(l_l_idx_comb)

    return l_l_comb


class SharedNDArray:
    """
    Wraps a numpy array in multiprocessing shared memory.
    Pickleable: can be sent through multiprocessing.Queue.
    """

    def __init__(self, shape: Tuple[int, ...], dtype: np.dtype, name: Optional[str], create: bool):
        """ Create a new shared-memory block or attach to an existing one.

        :param shape: Array shape.
        :param dtype: Array dtype.
        :param name: Shared-memory block name. Must be ``None`` if
            ``create=True`` (the OS assigns one); must be a valid existing
            block name if ``create=False``.
        :param create: ``True`` to allocate a new block, ``False`` to
            attach to an existing block by ``name``.
        """
        self.shape = tuple(shape)
        self.dtype = np.dtype(dtype)

        self.shm: SharedMemory
        if create:
            # create new shared block
            assert name is None, "Let SharedMemory do name creation"
            nbytes: int = int(np.prod(self.shape)) * self.dtype.itemsize
            self.shm = shared_memory.SharedMemory(create=True, size=nbytes, name=name)
        else:
            # attach to existing shared block
            self.shm = shared_memory.SharedMemory(name=name)

        # numpy view backed by shared memory
        self.array: NDArray = np.ndarray(self.shape, dtype=self.dtype, buffer=self.shm.buf)

    @property
    def name(self) -> str:
        """ Return the OS name of the underlying shared-memory block.

        :return: The shared-memory block's ``shm.name``.
        """
        return self.shm.name

    def close(self) -> None:
        """Close this process's handle."""
        self.shm.close()

    def unlink(self) -> None:
        """Free system resource (call once when all processes are done)."""
        del self.array
        self.shm.unlink()

    # --- Pickling support ---
    def __reduce__(self) -> Tuple[Type, Tuple[Tuple[int, ...], np.dtype, str, bool]]:
        """
        When pickled, only send (shape, dtype, name).
        Receiving process reattaches with create=False.
        """
        return self.__class__, (self.shape, self.dtype, self.shm.name, False)

    # --- Convenience ---
    def __getitem__(self, key: Any) -> NDArray:
        return cast(NDArray, self.array[key])

    def __setitem__(self, key: Any, value: ArrayLike) -> None:
        self.array[key] = value

    def __array__(self) -> NDArray:
        return self.array

    def __repr__(self) -> str:
        return f"SharedNDArray(name={self.name}, shape={self.shape}, dtype={self.dtype})"


def np_to_shnd(arr: NDArray) -> SharedNDArray:
    """ Copy an in-process numpy array into a fresh shared-memory block.

    :param arr: Source numpy array. Its shape and dtype are preserved.
    :return: A new ``SharedNDArray`` whose contents equal ``arr``.
    """
    arr_shm: SharedNDArray = SharedNDArray(arr.shape, arr.dtype, None, True)
    arr_shm.array[:] = arr

    return arr_shm
