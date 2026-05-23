""" Small numeric and collection utilities used throughout DeepXube.

Contents: flatten/unflatten list-of-lists with matching split indices, even
integer partitions, whitespace stripping, random set subsampling, and a
numerically-stable Boltzmann softmax.
"""

from typing import List, Tuple, Any, Union, Set, cast
import numpy as np
import math
import re
from numpy.typing import NDArray


def flatten(data: List[List[Any]]) -> Tuple[List[Any], List[int]]:
    """ Flatten a list of lists into one list plus the split points that
    recover the original grouping.

    :param data: List of sublists to concatenate.
    :return: Tuple of (flat list, split_idxs) where ``split_idxs`` are the
        cumulative lengths of all but the last sublist. Pass them to
        ``unflatten`` (or ``np.split``) to rebuild the grouping.
    """
    num_each = [len(x) for x in data]
    split_idxs: List[int] = np.cumsum(num_each)[:-1].tolist()

    data_flat = [item for sublist in data for item in sublist]

    return data_flat, split_idxs


def unflatten(data: Union[List[Any], NDArray[Any]], split_idxs: List[int]) -> List[List[Any]]:
    """ Inverse of ``flatten``: split a flat sequence back into sublists at
    the given cumulative boundaries.

    :param data: Flat sequence (list or ndarray).
    :param split_idxs: Cumulative split points, as produced by ``flatten``.
    :return: List of sublists reproducing the original grouping.
    """
    data_split: List[List[Any]] = []

    start_idx: int = 0
    end_idx: int
    for end_idx in split_idxs:
        data_split.append(list(data[start_idx:end_idx]))
        start_idx = end_idx

    data_split.append(list(data[start_idx:]))

    return data_split


def split_evenly(num_total: int, num_splits: int) -> List[int]:
    """ Partition ``num_total`` into ``num_splits`` integers that differ by
    at most 1, distributing the remainder across the leading buckets.

    :param num_total: Total to split.
    :param num_splits: Number of buckets.
    :return: List of length ``num_splits`` summing to ``num_total``.
    """
    num_per: List[int] = [math.floor(num_total / num_splits) for _ in range(num_splits)]
    left_over: int = num_total % num_splits
    for idx in range(left_over):
        num_per[idx] += 1

    return num_per


def split_evenly_w_max(num_total: int, num_splits: int, max_per: int) -> List[int]:
    """ Partition ``num_total`` into chunks, each no larger than ``max_per``,
    balanced across ``num_splits`` per round. The returned list may be
    longer than ``num_splits`` if ``num_total > num_splits * max_per``.

    :param num_total: Total to split.
    :param num_splits: Target number of buckets per round.
    :param max_per: Maximum value of any single bucket.
    :return: List of positive integers summing to ``num_total``, each
        at most ``max_per``.
    """
    num_done: int = 0
    num_per: List[int] = []
    while num_done < num_total:
        num_left = num_total - num_done
        num_per_no_max: List[int] = split_evenly(num_left, num_splits)
        for num_per_i in num_per_no_max:
            num_per_i = min(num_per_i, max_per)
            num_per.append(num_per_i)
            num_done += num_per_i
    assert num_done == num_total
    return num_per


def remove_all_whitespace(val: str) -> str:
    """ Return ``val`` with every whitespace character removed.

    :param val: Input string.
    :return: ``val`` stripped of all whitespace.
    """
    pattern = re.compile(r'\s+')
    val = re.sub(pattern, '', val)

    return val


def random_subset(set_orig: Union[Set[Any], frozenset[Any]], keep_prob: bool) -> Set[Any]:
    """ Return a Bernoulli-sampled subset of ``set_orig`` where each element
    is kept independently with probability ``keep_prob``.

    :param set_orig: Input set (or frozenset).
    :param keep_prob: Per-element keep probability in [0, 1].
    :return: A new set containing the retained elements.
    """
    rand_vals: NDArray[Any] = np.random.rand(len(set_orig))
    keep_arr: NDArray[np.bool_] = np.array(rand_vals < keep_prob)
    rand_subset: Set[Any] = set(elem for elem, keep_i in zip(set_orig, keep_arr) if keep_i)

    return rand_subset


def boltzmann(vals: List[float], temp: float) -> List[float]:
    """ Return the Boltzmann (softmax) distribution over ``vals`` at the given
    temperature. Numerically stable via max-subtraction.

    :param vals: Scores. If length is 1, returns ``[1.0]`` without
        computation.
    :param temp: Temperature; smaller values concentrate probability on the
        maxima, larger values flatten the distribution.
    :return: List of probabilities summing to 1.
    """
    if len(vals) == 1:
        return [1.0]
    else:
        vals_np: NDArray[np.float64] = np.array(vals)
        exp_vals_np: NDArray[np.float64] = np.exp((1.0 / temp) * (vals_np - np.max(vals_np)))
        probs_np: NDArray[np.float64] = exp_vals_np / np.sum(exp_vals_np)

        return cast(List[float], probs_np.tolist())
