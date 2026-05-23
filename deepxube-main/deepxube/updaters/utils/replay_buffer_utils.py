""" Fixed-capacity replay buffers used by the RL updaters.

Three typed variants store the tuples needed by each training regime:
``ReplayBufferV`` for value-based learning (state, goal, is_solved),
``ReplayBufferQ`` for Q-learning (state, goal, is_solved, action, tc, next_state),
and ``ReplayBufferP`` for policy learning (state, goal, action).
All use a ``collections.deque`` bounded by ``max_size`` with uniform
random sampling.
"""

from abc import ABC, abstractmethod
from typing import Deque, Tuple, List, Optional, Generic, TypeVar
from collections import deque
from deepxube.base.domain import State, Action, Goal
import numpy as np


ReplayVElem = Tuple[State, Goal, bool]
ReplayQElem = Tuple[State, Goal, bool, Action, float, State]
ReplayPElem = Tuple[State, Goal, Action]

ReplayVRet = Tuple[List[State], List[Goal], List[bool]]
ReplayQRet = Tuple[List[State], List[Goal], List[bool], List[Action], List[float], List[State]]
ReplayPRet = Tuple[List[State], List[Goal], List[Action]]

Elem = TypeVar('Elem')
SampRet = TypeVar('SampRet')


class ReplayBuffer(Generic[Elem, SampRet], ABC):
    """ Generic fixed-capacity replay buffer backed by a bounded deque with
    uniform random sampling. Concrete subclasses differ only in the element
    tuple shape and the unpacking done by ``_elems_to_ret``.
    """

    def __init__(self, max_size: int):
        """ Create an empty buffer of the given capacity.

        :param max_size: Maximum number of elements; once exceeded, the
            oldest elements are dropped (``deque`` semantics).
        """
        self.deque: Deque[Elem] = deque([], max_size)

    def add(self, data: List[Elem]) -> None:
        """ Append a batch of elements, evicting oldest if full.

        :param data: List of new elements to push.
        """
        self.deque.extend(data)

    def sample(self, num: int) -> SampRet:
        """ Uniformly sample ``num`` elements (with replacement) and unpack
        them into per-field lists via ``_elems_to_ret``.

        :param num: Number of elements to sample.
        :return: A tuple of per-field lists, defined by the subclass.
        """
        assert self.size() > 0, f"Replay buffer size should not be {self.size()}"
        idxs: List[int] = np.random.randint(0, len(self.deque), size=num).tolist()
        elems: List[Elem] = [self.deque[idx] for idx in idxs]
        return self._elems_to_ret(elems)

    def size(self) -> int:
        """ Return the current number of elements in the buffer.

        :return: Number of elements currently stored.
        """
        return len(self.deque)

    def max_size(self) -> int:
        """ Return the configured capacity.

        :return: The ``max_size`` passed at construction.
        """
        maxlen: Optional[int] = self.deque.maxlen
        assert maxlen is not None

        return maxlen

    @abstractmethod
    def _elems_to_ret(self, elems: List[Elem]) -> SampRet:
        """ Unpack a list of element tuples into parallel per-field lists.

        :param elems: Sampled element tuples.
        :return: Per-field lists in the subclass's return format.
        """
        pass


class ReplayBufferV(ReplayBuffer[ReplayVElem, ReplayVRet]):
    """ Replay buffer storing ``(state, goal, is_solved)`` triples for V-based
    RL.
    """

    def _elems_to_ret(self, elems: List[ReplayVElem]) -> ReplayVRet:
        """ Unpack ``(state, goal, is_solved)`` tuples into three parallel
        lists.

        :param elems: Sampled triples.
        :return: ``(states, goals, is_solved_l)``.
        """
        states: List[State] = [replay_q_elem[0] for replay_q_elem in elems]
        goals: List[Goal] = [replay_q_elem[1] for replay_q_elem in elems]
        is_solved_l: List[bool] = [replay_q_elem[2] for replay_q_elem in elems]

        return states, goals, is_solved_l


class ReplayBufferQ(ReplayBuffer[ReplayQElem, ReplayQRet]):
    """ Replay buffer storing
    ``(state, goal, is_solved, action, tc, next_state)`` six-tuples for
    Q-learning.
    """

    def _elems_to_ret(self, elems: List[ReplayQElem]) -> ReplayQRet:
        """ Unpack the six-tuples into six parallel lists.

        :param elems: Sampled six-tuples.
        :return: ``(states, goals, is_solved_l, actions, tcs, states_next)``.
        """
        states: List[State] = [replay_q_elem[0] for replay_q_elem in elems]
        goals: List[Goal] = [replay_q_elem[1] for replay_q_elem in elems]
        is_solved_l: List[bool] = [replay_q_elem[2] for replay_q_elem in elems]
        actions: List[Action] = [replay_q_elem[3] for replay_q_elem in elems]
        tcs: List[float] = [replay_q_elem[4] for replay_q_elem in elems]
        states_next: List[State] = [replay_q_elem[5] for replay_q_elem in elems]

        return states, goals, is_solved_l, actions, tcs, states_next


class ReplayBufferP(ReplayBuffer[ReplayPElem, ReplayPRet]):
    """ Replay buffer storing ``(state, goal, action)`` triples for policy
    training.
    """

    def _elems_to_ret(self, elems: List[ReplayPElem]) -> ReplayPRet:
        """ Unpack ``(state, goal, action)`` tuples into three parallel lists.

        :param elems: Sampled triples.
        :return: ``(states, goals, actions)``.
        """
        states: List[State] = [replay_q_elem[0] for replay_q_elem in elems]
        goals: List[Goal] = [replay_q_elem[1] for replay_q_elem in elems]
        actions: List[Action] = [replay_q_elem[2] for replay_q_elem in elems]

        return states, goals, actions
