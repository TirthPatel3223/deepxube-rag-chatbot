""" CLI-argument parsing helpers that resolve dotted strings like ``grid.7``
or ``resnet_fc.100H_2B_bn`` into fully-constructed domain, heuristic, policy,
or pathfinding objects via the factory registries.

The convention is ``<name>.<parser-args>``: the part before the first dot is
the factory registration key; the part after is handed to the registered
``Parser`` for that key.
"""

from typing import Tuple, Optional, List, Dict, Any

from deepxube.base.domain import Domain
from deepxube.base.heuristic import HeurNNetPar, PolicyNNetPar
from deepxube.base.pathfinding import PathFind

from deepxube.factories.domain_factory import domain_factory
from deepxube.factories.heuristic_factory import heuristic_factory, policy_factory, build_heur_nnet_par, build_policy_nnet_par
from deepxube.factories.pathfinding_factory import pathfinding_factory


def get_name_args(name_args: str) -> Tuple[str, Optional[str]]:
    """ Split a CLI argument of the form ``<name>[.<args>]`` at the first dot.

    :param name_args: Raw CLI argument, e.g. ``"grid.7"`` or ``"grid"``.
    :return: ``(name, args)``; ``args`` is ``None`` if no dot is present.
    """
    name_args_split: List[str] = name_args.split(".", 1)
    name: str = name_args_split[0]
    args: Optional[str]
    if len(name_args_split) == 1:
        args = None
    else:
        assert len(name_args_split) == 2
        args = name_args_split[1]
    return name, args


def get_domain_from_arg(domain: str) -> Tuple[Domain, str]:
    """ Resolve a ``--domain`` CLI argument into a ``Domain`` instance.

    :param domain: CLI string, e.g. ``"grid.7"``.
    :return: Tuple of (instantiated ``Domain``, registration name).
    """
    domain_name, domain_args = get_name_args(domain)
    domain_kwargs: Dict[str, Any] = domain_factory.get_kwargs(domain_name, domain_args)
    return domain_factory.build_class(domain_name, domain_kwargs), domain_name


def get_heur_nnet_par_from_arg(domain: Domain, domain_name: str, heur: str, heur_type: str) -> Tuple[HeurNNetPar, str]:
    """ Resolve a ``--heur`` / ``--heur_type`` CLI argument pair into a
    ``HeurNNetPar`` for the given domain.

    :param domain: Instantiated domain the network will run on.
    :param domain_name: Domain registration key.
    :param heur: CLI string for the network, e.g. ``"resnet_fc.100H_2B_bn"``.
    :param heur_type: One of ``"V"``, ``"QFIX"``, ``"QIN"`` (case-insensitive).
    :return: Tuple of (``HeurNNetPar``, network registration name).
    """
    nnet_name, nnet_args = get_name_args(heur)
    heuristic_factory.get_type(nnet_name)  # to ensure existence
    nnet_kwargs: Dict[str, Any] = heuristic_factory.get_kwargs(nnet_name, nnet_args)
    nnet_par: HeurNNetPar = build_heur_nnet_par(domain, domain_name, nnet_name, nnet_kwargs, heur_type)
    return nnet_par, nnet_name


def get_policy_nnet_par_from_arg(domain: Domain, domain_name: str, policy: str, num_samp: int, num_int: int) -> Tuple[PolicyNNetPar, str]:
    """ Resolve a ``--policy`` CLI argument into a ``PolicyNNetPar`` for the
    given domain.

    :param domain: Instantiated domain the policy will act on.
    :param domain_name: Domain registration key.
    :param policy: CLI string for the policy network.
    :param num_samp: Number of sampled actions per state at training time.
    :param num_int: Number of random (mode-collapse guard) actions to mix in.
    :return: Tuple of (``PolicyNNetPar``, network registration name).
    """
    nnet_name, nnet_args = get_name_args(policy)
    policy_factory.get_type(nnet_name)  # to ensure existence
    nnet_kwargs: Dict[str, Any] = policy_factory.get_kwargs(nnet_name, nnet_args)
    nnet_par: PolicyNNetPar = build_policy_nnet_par(domain, domain_name, nnet_name, nnet_kwargs, num_samp, num_int)
    return nnet_par, nnet_name


def get_pathfind_name_kwargs(pathfind: str) -> Tuple[str, Dict[str, Any]]:
    """ Resolve a ``--pathfind`` CLI argument into its registration name and
    constructor kwargs, without instantiating it.

    :param pathfind: CLI string, e.g. ``"graph_v.1B_1.0W"``.
    :return: Tuple of (pathfinder registration name, constructor kwargs).
    """
    name, args_str = get_name_args(pathfind)
    pathfind_kwargs: Dict[str, Any] = pathfinding_factory.get_kwargs(name, args_str)
    return name, pathfind_kwargs


def get_pathfind_from_arg(domain: Domain, functions: Any, pathfind: str) -> Tuple[PathFind, str]:
    """ Resolve a ``--pathfind`` CLI argument into a constructed ``PathFind``.

    Injects ``domain`` and ``functions`` into the pathfinder kwargs before
    instantiation.

    :param domain: Instantiated domain the pathfinder will run over.
    :param functions: An ``FNs*`` dataclass (heuristic / policy bundle), or
        ``None`` for supervised pathfinders.
    :param pathfind: CLI string, e.g. ``"graph_v.1B_1.0W"``.
    :return: Tuple of (instantiated ``PathFind``, registration name).
    """
    pathfind_name, args_str = get_name_args(pathfind)
    pathfind_kwargs: Dict[str, Any] = pathfinding_factory.get_kwargs(pathfind_name, args_str)
    pathfind_kwargs["domain"] = domain
    pathfind_kwargs["functions"] = functions
    return pathfinding_factory.build_class(pathfind_name, pathfind_kwargs), pathfind_name
