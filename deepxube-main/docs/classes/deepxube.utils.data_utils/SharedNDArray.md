---
id: "class:deepxube.utils.data_utils.SharedNDArray"
kind: "class"
name: "SharedNDArray"
qualified_name: "deepxube.utils.data_utils.SharedNDArray"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 172
line_end: 241
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.utils.data_utils.SharedNDArray.__init__"
  - "func:deepxube.utils.data_utils.SharedNDArray.name"
  - "func:deepxube.utils.data_utils.SharedNDArray.close"
  - "func:deepxube.utils.data_utils.SharedNDArray.unlink"
  - "func:deepxube.utils.data_utils.SharedNDArray.__reduce__"
  - "func:deepxube.utils.data_utils.SharedNDArray.__getitem__"
  - "func:deepxube.utils.data_utils.SharedNDArray.__setitem__"
  - "func:deepxube.utils.data_utils.SharedNDArray.__array__"
  - "func:deepxube.utils.data_utils.SharedNDArray.__repr__"
attributes:
  - name: "self.array"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.dtype"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.shape"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.shm"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.utils.data_utils.SharedNDArray`

**File:** [deepxube/utils/data_utils.py:172](../../../deepxube/utils/data_utils.py#L172)
**Abstract:** no

## Docstring

Wraps a numpy array in multiprocessing shared memory.
Pickleable: can be sent through multiprocessing.Queue.

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `name` *(trivial, skipped)*
- `close` *(trivial, skipped)*
- `unlink` *(trivial, skipped)*
- `__reduce__` *(trivial, skipped)*
- `__getitem__` — *(no docstring)*
- `__setitem__` *(trivial, skipped)* — *(no docstring)*
- `__array__` *(trivial, skipped)* — *(no docstring)*
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.array` | — | __init__ |
| `self.dtype` | — | __init__ |
| `self.shape` | — | __init__ |
| `self.shm` | — | __init__ |

## Source

```python
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
```
