""" Abstract ``NNetInput`` plus the ``Has*In`` mixins domains use to declare
which input shapes their states/goals/actions can be converted to.

A concrete ``NNetInput`` answers two questions: what tensor shapes does the
network see, and how do you convert (states[, goals[, actions]]) into those
tensors? The ``DynamicNNetInput`` machinery lets a domain register concrete
``NNetInput`` classes at class-definition time so the heuristic factory can
discover them. """

from typing import Any, List, Tuple, Generic, TypeVar, Type, ClassVar, Dict, Optional
from abc import ABC, abstractmethod

from deepxube.base.domain import Domain, State, Action, Goal

import numpy as np

from numpy.typing import NDArray


D = TypeVar('D', bound=Domain)
S = TypeVar('S', bound=State)
A = TypeVar('A', bound=Action)
G = TypeVar('G', bound=Goal)


class NNetInput(ABC, Generic[D]):
    """ Abstract base: knows how to describe the network input shape and convert objects to numpy. """

    def __init__(self, domain: D):
        """ Bind to its domain. """
        self.domain: D = domain

    @abstractmethod
    def get_input_info(self) -> Any:
        """ :return: Subclass-specific tuple describing input shapes / one-hot depths. """
        pass

    @abstractmethod
    def to_np(self, *args: Any) -> List[NDArray]:
        """ Convert input objects to a list of numpy arrays (one per network tensor slot). """
        pass


class FlatIn(NNetInput[D]):
    """ Marker mixin: the network input is a flat (1-D) vector. """

    @abstractmethod
    def get_input_info(self) -> Tuple[List[int], List[int]]:
        """
        :return: A list of dimensions of the arrays given to the neural network (pre one_hot), A list of depths for performing a one_hot representation on
        that corresponding input.
        If 1, then no one_hot is performed.
        """
        pass


class TwoDIn(NNetInput[D]):
    """ Marker mixin: the network input is a (channels, height, width) tensor. """

    @abstractmethod
    def get_input_info(self) -> Tuple[List[int], Tuple[int, int], List[int], Optional[int]]:
        """
        :return: A list of channels of the arrays given to the neural network (pre one_hot), (height, width),
        a list of depths for performing a one_hot representation on that corresponding input, optional 1x1 conv channel out for qfix.
        The one_hot is applied to the channel dimension. If 1, then no one_hot is performed.
        """
        pass


class StateGoalIn(NNetInput[D], Generic[D, S, G]):
    """ Marker mixin: input is built from (states, goals). """

    @abstractmethod
    def to_np(self, states: List[S], goals: List[G]) -> List[NDArray]:
        """ Convert (state, goal) pairs to numpy network inputs. """
        pass


class StateGoalActFixIn(NNetInput[D], Generic[D, S, G, A]):
    """ Marker mixin: input is built from (states, goals, fixed-length action lists). """

    @abstractmethod
    def to_np(self, states: List[S], goals: List[G], actions_l: List[List[A]]) -> List[NDArray]:
        """ Convert (state, goal, action-list) triples to numpy inputs. """
        pass


class StateGoalActIn(NNetInput[D], Generic[D, S, G, A]):
    """ Marker mixin: input is built from (states, goals, one action per row). """

    @abstractmethod
    def to_np(self, states: List[S], goals: List[G], actions: List[A]) -> List[NDArray]:
        """ Convert (state, goal, action) triples to numpy inputs. """
        pass


class PolicyNNetIn(NNetInput[D], Generic[D, S, G, A]):
    """ Marker mixin: input feeds a policy network — needs both training (with actions) and inference (without) conversions. """

    @abstractmethod
    def to_np(self, states: List[S], goals: List[G], actions: List[A]) -> List[NDArray]:
        """ Training-side conversion (target actions included). """
        pass

    @abstractmethod
    def to_np_fn(self, states: List[S], goals: List[G]) -> List[NDArray]:
        """ Inference-side conversion (no actions). """
        pass

    @abstractmethod
    def nnet_out_to_actions(self, nnet_out: List[NDArray[np.float64]]) -> List[A]:
        """ Decode network output arrays into ``A`` objects. """
        pass

    @abstractmethod
    def states_goals_actions_split_idx(self) -> int:
        """ :return: Index in the ``to_np`` list at which actions begin (states/goals on the left). """
        pass


class FlatInPolicy(FlatIn[D], PolicyNNetIn[D, S, G, A], ABC):
    """ Combination of ``FlatIn`` and ``PolicyNNetIn`` for flat-input policy networks. """
    pass


# Env mixins for inputs
class DynamicNNetInput(Domain[S, A, G], ABC):
    """ Domain mixin: subclass declares which concrete ``NNetInput`` classes
    it offers. A subclass-local registry is created in ``__init_subclass__``. """

    _nnet_input_register: ClassVar[Dict[str, Type[NNetInput]]] = dict()

    def __init_subclass__(cls, **kwargs: Any):
        """ Give every subclass its own fresh ``_nnet_input_register`` dict. """
        super().__init_subclass__(**kwargs)
        # Create a fresh dict for THIS subclass
        cls._nnet_input_register = {}

    @classmethod
    def register_nnet_input(cls, nnet_input_t: Type[NNetInput], nnet_input_name: str) -> None:
        """ Record ``nnet_input_t`` under ``nnet_input_name`` in the subclass registry. """
        cls._nnet_input_register[nnet_input_name] = nnet_input_t

    @classmethod
    def get_dynamic_nnet_inputs(cls) -> Dict[str, Type[NNetInput]]:
        """ :return: A copy of this subclass's registered ``{nnet_input_name: cls}`` map. """
        return cls._nnet_input_register.copy()


class HasFlatSGIn(DynamicNNetInput[S, A, G]):
    """ Has a flat representation for state/goal inputs

    """

    class FlatSGConcrete(FlatIn["HasFlatSGIn"], StateGoalIn["HasFlatSGIn", State, Goal]):
        """ Auto-generated ``NNetInput`` for ``HasFlatSGIn`` domains; delegates to the domain's ``to_np_flat_sg``. """

        def __init__(self, domain: "HasFlatSGIn"):
            """ Bind to the host domain. """
            super().__init__(domain)

        def get_input_info(self) -> Tuple[List[int], List[int]]:
            """ Delegate to the domain's ``get_input_info_flat_sg``. """
            return self.domain.get_input_info_flat_sg()

        def to_np(self, states: List[State], goals: List[Goal]) -> List[NDArray]:
            """ Delegate to the domain's ``to_np_flat_sg``. """
            return self.domain.to_np_flat_sg(states, goals)

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``FlatSGConcrete`` under the ``"flat_sg"`` key for every subclass. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.FlatSGConcrete, "flat_sg")

    @abstractmethod
    def get_input_info_flat_sg(self) -> Tuple[List[int], List[int]]:
        """
        :return: A list of dimensions of the arrays given to the neural network (pre one_hot), A list of depths for performing a one_hot representation on
        that corresponding input.
        If 1, then no one_hot is performed.
        """
        pass

    @abstractmethod
    def to_np_flat_sg(self, states: List[S], goals: List[G]) -> List[NDArray]:
        """ Domain-specific conversion of (states, goals) into the flat numpy input. """
        pass


class HasActsEnumFixedIn(Domain[S, A, G]):
    """ Mixin for domains whose actions can be mapped to a fixed integer index. """

    @abstractmethod
    def actions_to_indices(self, actions: List[A]) -> List[int]:
        """ :return: Integer index of each action in the fixed action list. """
        pass


class HasFlatSGActsEnumFixedIn(HasFlatSGIn[S, A, G], HasActsEnumFixedIn[S, A, G], ABC):
    """ Combines ``HasFlatSGIn`` with ``HasActsEnumFixedIn`` for fixed-Q networks on flat inputs. """

    class FlatSGActFixConcrete(FlatIn["HasFlatSGActsEnumFixedIn"], StateGoalActFixIn["HasFlatSGActsEnumFixedIn", State, Goal, Action]):
        """ Auto-generated ``NNetInput`` that appends per-state action-index arrays to the flat state/goal input. """

        def __init__(self, domain: "HasFlatSGActsEnumFixedIn"):
            """ Bind to the host domain. """
            super().__init__(domain)

        def get_input_info(self) -> Tuple[List[int], List[int]]:
            """ Delegate to the domain's ``get_input_info_flat_sg``. """
            return self.domain.get_input_info_flat_sg()

        def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]:
            """ Build the flat (state, goal) input then append an integer action-index array. """
            num_actions: int = len(actions_l[0])
            actions_np: NDArray = np.zeros((len(actions_l), num_actions)).astype(int)
            for i, actions in enumerate(actions_l):
                actions_np[i] = np.array(self.domain.actions_to_indices(actions))

            return self.domain.to_np_flat_sg(states, goals) + [actions_np]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``FlatSGActFixConcrete`` under ``"flat_sg_actfix"``. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.FlatSGActFixConcrete, "flat_sg_actfix")


class HasFlatSGAIn(DynamicNNetInput[S, A, G]):
    """ Domain mixin: provides a flat (state, goal, single action) network input. """

    class FlatSGAConcrete(FlatIn["HasFlatSGAIn"], StateGoalActIn["HasFlatSGAIn", State, Goal, Action]):
        """ Auto-generated ``NNetInput`` delegating to the domain's ``to_np_flat_sga``. """

        def __init__(self, domain: "HasFlatSGAIn"):
            """ Bind to the host domain. """
            super().__init__(domain)

        def get_input_info(self) -> Tuple[List[int], List[int]]:
            """ Delegate to the domain's ``get_input_info_flat_sga``. """
            return self.domain.get_input_info_flat_sga()

        def to_np(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray]:
            """ Delegate to the domain's ``to_np_flat_sga``. """
            return self.domain.to_np_flat_sga(states, goals, actions)

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``FlatSGAConcrete`` under ``"flat_sga"``. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.FlatSGAConcrete, "flat_sga")

    @abstractmethod
    def get_input_info_flat_sga(self) -> Tuple[List[int], List[int]]:
        """ :return: Same shape as ``get_input_info_flat_sg`` but for the (state, goal, action) input. """
        pass

    @abstractmethod
    def to_np_flat_sga(self, states: List[S], goals: List[G], actions: List[A]) -> List[NDArray]:
        """ Convert (states, goals, actions) to numpy network input. """
        pass


class HasTwoDSGIn(DynamicNNetInput[S, A, G]):
    """ Has a 2d representation for state/goal inputs

    """

    class TwoDSGConcrete(TwoDIn["HasTwoDSGIn"], StateGoalIn["HasTwoDSGIn", State, Goal]):
        """ Auto-generated 2-D ``NNetInput`` for ``HasTwoDSGIn`` domains. """

        def __init__(self, domain: "HasTwoDSGIn"):
            """ Bind to the host domain. """
            super().__init__(domain)

        def get_input_info(self) -> Tuple[List[int], Tuple[int, int], List[int], Optional[int]]:
            """ Delegate to the domain's ``get_input_info_2d_sg``. """
            return self.domain.get_input_info_2d_sg()

        def to_np(self, states: List[State], goals: List[Goal]) -> List[NDArray]:
            """ Delegate to the domain's ``to_np_2d_sg``. """
            return self.domain.to_np_2d_sg(states, goals)

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``TwoDSGConcrete`` under ``"2d_sg"``. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.TwoDSGConcrete, "2d_sg")

    @abstractmethod
    def get_input_info_2d_sg(self) -> Tuple[List[int], Tuple[int, int], List[int], Optional[int]]:
        """
        :return: A list of channels of the arrays given to the neural network (pre one_hot), (height, width),
        a list of depths for performing a one_hot representation on that corresponding input, optional 1x1 conv channel out for qfix.
        The one_hot is applied to the channel dimension. If 1, then no one_hot is performed.
        """
        pass

    @abstractmethod
    def to_np_2d_sg(self, states: List[S], goals: List[G]) -> List[NDArray]:
        """
        :param states: List of states
        :param goals: List of goals

        :return: list of arrays representing states and goals in (chan, height, width) format
        """


class HasTwoDSGActsEnumFixedIn(HasTwoDSGIn[S, A, G], HasActsEnumFixedIn[S, A, G], ABC):
    """ ``HasTwoDSGIn`` + ``HasActsEnumFixedIn`` for fixed-Q networks on 2-D inputs. """

    class TwoDSGActFixConcrete(TwoDIn["HasTwoDSGActsEnumFixedIn"], StateGoalActFixIn["HasTwoDSGActsEnumFixedIn", State, Goal, Action]):
        """ Auto-generated 2-D ``NNetInput`` that appends per-state action indices. """

        def __init__(self, domain: "HasTwoDSGActsEnumFixedIn"):
            """ Bind to the host domain. """
            super().__init__(domain)

        def get_input_info(self) -> Tuple[List[int], Tuple[int, int], List[int], Optional[int]]:
            """ Delegate to the domain's ``get_input_info_2d_sg``. """
            return self.domain.get_input_info_2d_sg()

        def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]:
            """ Build the 2-D (state, goal) input then append an integer action-index array. """
            num_actions: int = len(actions_l[0])
            actions_np: NDArray = np.zeros((len(actions_l), num_actions)).astype(int)
            for i, actions in enumerate(actions_l):
                actions_np[i] = np.array(self.domain.actions_to_indices(actions))

            return self.domain.to_np_2d_sg(states, goals) + [actions_np]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``TwoDSGActFixConcrete`` under ``"2d_sg_actfix"``. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.TwoDSGActFixConcrete, "2d_sg_actfix")
