""" Registries for heuristic and policy neural networks, plus builders that
pair a registered network with a compatible per-domain ``NNetInput``.

The factories here are used to turn a CLI pair like
``(--domain grid.7, --heur resnet_fc.100H_2B_bn, --heur_type V)`` into a
fully-wired ``HeurNNetPar`` that knows how to convert states/goals into numpy
arrays and then into a network. The concrete ``*Concrete`` subclasses at the
bottom of this file plug the right ``NNetInput`` into the right
``HeurNNetPar`` / ``PolicyNNetPar`` variant.
"""

from abc import ABC
from typing import Dict, Tuple, Type, List, Any, Optional

import numpy as np

from deepxube.base.factory import Factory
from deepxube.base.domain import Domain, State, Action, Goal, ActsEnumFixed
from deepxube.base.nnet_input import NNetInput, StateGoalIn, StateGoalActFixIn, StateGoalActIn, PolicyNNetIn
from deepxube.base.heuristic import HeurNNet, PolicyNNet, HeurNNetPar, PolicyNNetPar, HeurNNetParV, HeurNNetParQIn, HeurNNetParQFixOut

from numpy.typing import NDArray

from deepxube.factories.nnet_input_factory import get_domain_nnet_input_keys, get_nnet_input_t


heuristic_factory: Factory[HeurNNet] = Factory[HeurNNet]("HeurNNet")
policy_factory: Factory[PolicyNNet] = Factory[PolicyNNet]("PolicyNNet")


def build_heur_nnet_par(domain: Domain, domain_name: str, nnet_name: str, nnet_kwargs: Dict[str, Any], heur_type: str) -> HeurNNetPar:
    """ Build a ``HeurNNetPar`` by pairing a registered heuristic network with
    an ``NNetInput`` the domain supports and the network accepts.

    Walks every ``NNetInput`` registered under ``domain_name`` and returns the
    first one that is simultaneously a subclass of the heuristic network's
    expected input type and of the input mixin required by ``heur_type``
    (``StateGoalIn`` for ``V``, ``StateGoalActFixIn`` for ``QFIX``,
    ``StateGoalActIn`` for ``QIN``).

    :param domain: The instantiated domain the network will run against.
    :param domain_name: Registration key of the domain.
    :param nnet_name: Registration key of the heuristic network (e.g.
        ``"resnet_fc"``).
    :param nnet_kwargs: Keyword arguments to pass to the network constructor.
    :param heur_type: One of ``"V"``, ``"QFIX"``, ``"QIN"``
        (case-insensitive). Selects the output shape.
    :return: A concrete ``HeurNNetPar`` (``HeurNNetParVConcrete``,
        ``HeurNNetParQFixOutConcrete``, or ``HeurNNetParQActInConcrete``).
    :raises ValueError: If ``heur_type`` is unrecognised, or if no compatible
        ``NNetInput`` is found for the given domain, heur type, and network.
    """
    nnet_input_t: Type[NNetInput] = heuristic_factory.get_type(nnet_name).nnet_input_type()
    nnet_input_domain_keys: List[Tuple[str, str]] = get_domain_nnet_input_keys(domain_name)

    for nnet_input_domain_key in nnet_input_domain_keys:
        nnet_input_cls: Type[NNetInput] = get_nnet_input_t(nnet_input_domain_key)
        if heur_type.upper() == "V":
            if issubclass(nnet_input_cls, StateGoalIn) and issubclass(nnet_input_cls, nnet_input_t):
                return HeurNNetParVConcrete(domain, nnet_input_domain_key, nnet_name, nnet_kwargs)
        elif heur_type.upper() == "QFIX":
            assert isinstance(domain, ActsEnumFixed)
            if issubclass(nnet_input_cls, StateGoalActFixIn) and issubclass(nnet_input_cls, nnet_input_t):
                return HeurNNetParQFixOutConcrete(domain, nnet_input_domain_key, nnet_name, nnet_kwargs, domain.get_num_acts())
        elif heur_type.upper() == "QIN":
            if issubclass(nnet_input_cls, StateGoalActIn) and issubclass(nnet_input_cls, nnet_input_t):
                return HeurNNetParQActInConcrete(domain, nnet_input_domain_key, nnet_name, nnet_kwargs)
        else:
            raise ValueError(f"Unknown heur type {heur_type}")
    raise ValueError(f"Cannot build heur nnet for domain: {domain_name}, heur type {heur_type}, and "
                     f"nnet_input type {nnet_input_t}.\nNNet inputs checked: {nnet_input_domain_keys}")


def build_policy_nnet_par(domain: Domain, domain_name: str, nnet_name: str, nnet_kwargs: Dict[str, Any], num_samp: int, num_rand: int) -> PolicyNNetPar:
    """ Build a ``PolicyNNetPar`` by pairing a registered policy network with
    a ``PolicyNNetIn`` the domain supports and the network accepts.

    :param domain: The instantiated domain the policy will act on.
    :param domain_name: Registration key of the domain.
    :param nnet_name: Registration key of the policy network.
    :param nnet_kwargs: Keyword arguments to pass to the network constructor.
    :param num_samp: Number of sampled actions per state for training.
    :param num_rand: Number of random actions to mix in (mode-collapse guard).
    :return: A ``PolicyNNetParConcrete``.
    :raises ValueError: If no ``PolicyNNetIn``-compatible input is found for
        the domain and network.
    """
    nnet_input_t: Type[NNetInput] = policy_factory.get_type(nnet_name).nnet_input_type()
    nnet_input_domain_keys: List[Tuple[str, str]] = get_domain_nnet_input_keys(domain_name)
    for nnet_input_domain_key in nnet_input_domain_keys:
        nnet_input_cls: Type[NNetInput] = get_nnet_input_t(nnet_input_domain_key)
        if issubclass(nnet_input_cls, PolicyNNetIn) and issubclass(nnet_input_cls, nnet_input_t):
            return PolicyNNetParConcrete(domain, nnet_input_domain_key, nnet_name, nnet_kwargs, num_samp, num_rand)

    raise ValueError(f"Cannot build policy nnet for domain: {domain_name}, and "
                     f"nnet_input type {nnet_input_t}.\nNNet inputs checked: {nnet_input_domain_keys}")


class HeurNNetParFacClass(HeurNNetPar, ABC):
    """ Shared plumbing for factory-built ``HeurNNetPar`` subclasses.

    Holds the (domain, input-registry-key, network-name, kwargs, Q-fix flag,
    output dim) needed to lazily construct both the ``NNetInput`` and the
    heuristic network. Subclasses differ only in which ``StateGoalIn`` /
    ``StateGoalActFixIn`` / ``StateGoalActIn`` mixin the input must satisfy.
    """

    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str, nnet_kwargs: Dict[str, Any], q_fix: bool, out_dim: int):
        """ Store the domain, input key, and network parameters for later
        lazy construction.

        :param domain: The domain the input and network operate on.
        :param nnet_input_name: ``(domain_name, nnet_input_name)`` key into
            the nnet-input registry.
        :param nnet_name: Registration key of the heuristic network.
        :param nnet_kwargs: Keyword arguments for the network constructor.
        :param q_fix: ``True`` for a fixed-output-dim Q-network
            (one output per action).
        :param out_dim: Number of heuristic outputs (1 for V, ``num_acts``
            for fixed Q).
        """
        self.domain: Domain = domain
        self.nnet_input_name: Tuple[str, str] = nnet_input_name
        self.nnet_input: Optional[NNetInput] = None
        self.nnet_name: str = nnet_name
        self.nnet_kwargs: Dict[str, Any] = nnet_kwargs
        self.q_fix: bool = q_fix
        self.out_dim: int = out_dim

    def get_nnet(self) -> HeurNNet:
        """ Construct the heuristic network, injecting the lazily-built
        ``NNetInput`` plus the Q-fix flag and output dimension into the
        factory kwargs.

        :return: A freshly-constructed ``HeurNNet`` ready for training
            or inference.
        """
        nnet_params: Dict = self.nnet_kwargs.copy()
        nnet_params['nnet_input'] = self._get_nnet_input()
        nnet_params['q_fix'] = self.q_fix
        nnet_params['out_dim'] = self.out_dim
        return heuristic_factory.build_class(self.nnet_name, nnet_params)

    def _get_nnet_input(self) -> NNetInput:
        """ Lazily build (once) and return the ``NNetInput`` instance for the
        stored ``nnet_input_name`` + domain.

        :return: The cached ``NNetInput`` instance.
        """
        if self.nnet_input is None:
            self.nnet_input = get_nnet_input_t(self.nnet_input_name)(domain=self.domain)
        return self.nnet_input

    def __getstate__(self) -> Dict:
        """ Drop ``self.nnet_input`` before pickling so worker processes
        rebuild it locally rather than sharing a (possibly unpicklable)
        cached one.

        :return: ``self.__dict__`` with ``nnet_input`` cleared.
        """
        self.nnet_input = None
        return self.__dict__


class PolicyNNetParFacClass(PolicyNNetPar, ABC):
    """ Shared plumbing for factory-built ``PolicyNNetPar`` subclasses,
    analogous to ``HeurNNetParFacClass`` but for policy networks.
    """

    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str, nnet_kwargs: Dict[str, Any], num_samp: int, num_rand: int):
        """ Store the domain, input key, and network parameters for later
        lazy construction.

        :param domain: The domain the policy operates on.
        :param nnet_input_name: ``(domain_name, nnet_input_name)`` key into
            the nnet-input registry; must resolve to a ``PolicyNNetIn``.
        :param nnet_name: Registration key of the policy network.
        :param nnet_kwargs: Keyword arguments for the network constructor.
        :param num_samp: Number of sampled actions per state for training.
        :param num_rand: Number of random actions mixed in.
        """
        super().__init__(num_samp, num_rand)
        self.domain: Domain = domain
        self.nnet_input_name: Tuple[str, str] = nnet_input_name
        self.nnet_input: Optional[PolicyNNetIn] = None
        self.nnet_name: str = nnet_name
        self.nnet_kwargs: Dict[str, Any] = nnet_kwargs

    def get_nnet(self) -> PolicyNNet:
        """ Construct the policy network, injecting the lazily-built
        ``PolicyNNetIn`` into the factory kwargs.

        :return: A freshly-constructed ``PolicyNNet``.
        """
        nnet_params: Dict = self.nnet_kwargs.copy()
        nnet_params['nnet_input'] = self._get_nnet_input()
        return policy_factory.build_class(self.nnet_name, nnet_params)

    def _get_nnet_input(self) -> PolicyNNetIn:
        """ Lazily build (once) the ``PolicyNNetIn`` instance, asserting that
        the registered class implements the ``PolicyNNetIn`` mixin.

        :return: The cached ``PolicyNNetIn`` instance.
        """
        if self.nnet_input is None:
            nnet_input: NNetInput = get_nnet_input_t(self.nnet_input_name)(domain=self.domain)
            assert isinstance(nnet_input, PolicyNNetIn)
            self.nnet_input = nnet_input
        return self.nnet_input

    def __getstate__(self) -> Dict:
        """ Drop ``self.nnet_input`` before pickling; see
        ``HeurNNetParFacClass.__getstate__``.

        :return: ``self.__dict__`` with ``nnet_input`` cleared.
        """
        self.nnet_input = None
        return self.__dict__


class HeurNNetParVConcrete(HeurNNetParV, HeurNNetParFacClass):
    """ V-type heuristic network wrapper: output is a scalar cost-to-go per
    (state, goal) pair, input shape satisfies ``StateGoalIn``.
    """

    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str,
                 nnet_kwargs: Dict[str, Any]):
        """ Initialise a V-type wrapper with Q-fix off and output dim 1.

        :param domain: The domain the input operates on.
        :param nnet_input_name: Input registry key.
        :param nnet_name: Heuristic network registration key.
        :param nnet_kwargs: Network constructor kwargs.
        """
        HeurNNetParFacClass.__init__(self, domain, nnet_input_name, nnet_name, nnet_kwargs, False, 1)

    def to_np(self, states: List[State], goals: List[Goal]) -> List[NDArray]:
        """ Convert state/goal pairs to numpy network inputs.

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :return: List of numpy arrays, one per network input tensor.
        """
        return self._get_nnet_input().to_np(states, goals)

    def _get_nnet_input(self) -> StateGoalIn:
        """ Return the cached input, asserting it satisfies ``StateGoalIn``.

        :return: The ``StateGoalIn`` instance.
        """
        nnet_input: NNetInput = super()._get_nnet_input()
        assert isinstance(nnet_input, StateGoalIn)
        return nnet_input


class HeurNNetParQFixOutConcrete(HeurNNetParQFixOut, HeurNNetParFacClass):
    """ Q-network wrapper with a fixed output per action
    (output dim = ``num_acts``); input satisfies ``StateGoalActFixIn``.
    """

    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str, nnet_kwargs: Dict[str, Any], out_dim: int):
        """ Initialise a Q-fix wrapper with Q-fix on and output dim = ``out_dim``.

        :param domain: The domain the input operates on.
        :param nnet_input_name: Input registry key.
        :param nnet_name: Heuristic network registration key.
        :param nnet_kwargs: Network constructor kwargs.
        :param out_dim: Number of outputs, one per fixed action.
        """
        HeurNNetParFacClass.__init__(self, domain, nnet_input_name, nnet_name, nnet_kwargs, True, out_dim)

    def _to_np_fixed_acts(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]:
        """ Convert state/goal plus per-state action lists to numpy inputs.

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :param actions_l: One list of actions per (state, goal), all drawn
            from the fixed-action set.
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np(states, goals, actions_l)

    def _get_nnet_input(self) -> StateGoalActFixIn:
        """ Return the cached input, asserting it satisfies
        ``StateGoalActFixIn``.

        :return: The ``StateGoalActFixIn`` instance.
        """
        nnet_input: NNetInput = super()._get_nnet_input()
        assert isinstance(nnet_input, StateGoalActFixIn)
        return nnet_input


class HeurNNetParQActInConcrete(HeurNNetParQIn, HeurNNetParFacClass):
    """ Q-network wrapper with action-as-input (scalar Q output); input
    satisfies ``StateGoalActIn``. Used when the action space is not fixed.
    """

    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str],
                 nnet_name: str, nnet_kwargs: Dict[str, Any]):
        """ Initialise a Q-in wrapper with Q-fix off and output dim 1.

        :param domain: The domain the input operates on.
        :param nnet_input_name: Input registry key.
        :param nnet_name: Heuristic network registration key.
        :param nnet_kwargs: Network constructor kwargs.
        """
        HeurNNetParFacClass.__init__(self, domain, nnet_input_name, nnet_name, nnet_kwargs, False, 1)

    def _to_np_one_act(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray]:
        """ Convert state/goal plus one action per (state, goal) to numpy
        inputs.

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :param actions: One action per (state, goal).
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np(states, goals, actions)

    def _get_nnet_input(self) -> StateGoalActIn:
        """ Return the cached input, asserting it satisfies ``StateGoalActIn``.

        :return: The ``StateGoalActIn`` instance.
        """
        nnet_input: NNetInput = super()._get_nnet_input()
        assert isinstance(nnet_input, StateGoalActIn)
        return nnet_input


class PolicyNNetParConcrete(PolicyNNetParFacClass):
    """ Factory-built concrete ``PolicyNNetPar`` delegating input conversion
    and output decoding to a ``PolicyNNetIn``.
    """

    def to_np_fn(self, states: List[State], goals: List[Goal]) -> List[NDArray[Any]]:
        """ Convert state/goal pairs to numpy inputs for policy inference
        (no actions supplied).

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np_fn(states, goals)

    def to_np_train(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray[Any]]:
        """ Convert state/goal/action triples to numpy inputs for policy
        training (target-action labels included).

        :param states: List of state objects.
        :param goals: Matching list of goal objects.
        :param actions: One target action per (state, goal).
        :return: List of numpy network input arrays.
        """
        return self._get_nnet_input().to_np(states, goals, actions)

    def _nnet_out_to_actions(self, nnet_out: List[NDArray[np.float64]]) -> List[Action]:
        """ Decode raw network outputs into one ``Action`` per input state.

        :param nnet_out: Per-state output arrays from the policy network.
        :return: One sampled/argmaxed ``Action`` per state.
        """
        return self._get_nnet_input().nnet_out_to_actions(nnet_out)
