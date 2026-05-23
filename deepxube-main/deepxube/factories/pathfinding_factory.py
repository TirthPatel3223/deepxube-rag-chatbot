""" Registry for ``PathFind`` subclasses and helpers to assemble their
functions bundles.

Concrete pathfinders in ``deepxube/pathfinding/`` register themselves here via
``@pathfinding_factory.register_class("key")``. Two helpers resolve what each
pathfinder needs: ``get_pathfind_functions`` bundles the heuristic/policy
callables into the expected ``FNs*`` dataclass, and
``get_domain_compat_pathfind_names`` lists the pathfinders a given domain can
use.
"""

from typing import List, Type, Optional, Any
from deepxube.base.factory import Factory
from deepxube.base.domain import Domain
from deepxube.base.heuristic import HeurFn, HeurFnV, HeurFnQ, PolicyFn
from deepxube.base.pathfinding import PathFind, FNsHeurV, FNsHeurQ, FNsPolicy, FNsHeurVPolicy, FNsHeurQPolicy


pathfinding_factory: Factory[PathFind] = Factory[PathFind]("PathFind")


def get_pathfind_functions(pathfind_name: str, heur_fn: Optional[HeurFn], policy_fn: Optional[PolicyFn]) -> Any:
    """ Package heuristic and policy callables into the ``FNs*`` dataclass
    expected by the named pathfinder.

    Returns whichever of ``FNsHeurV``, ``FNsHeurQ``, ``FNsPolicy``,
    ``FNsHeurVPolicy``, or ``FNsHeurQPolicy`` the pathfinder's
    ``functions_type()`` declares.

    :param pathfind_name: Key of a registered ``PathFind`` subclass.
    :param heur_fn: Heuristic function, required if the pathfinder uses one.
        Must be a ``HeurFnV`` for V-type pathfinders and a ``HeurFnQ`` for
        Q-type.
    :param policy_fn: Policy function, required if the pathfinder uses one.
    :return: A populated ``FNs*`` dataclass, or ``None`` if the pathfinder's
        ``functions_type`` is ``Any`` (i.e. supervised pathfinders).
    :raises ValueError: If the pathfinder's ``functions_type`` is not one of
        the known ``FNs*`` classes.
    """
    pathfind_t: Type[PathFind] = pathfinding_factory.get_type(pathfind_name)
    functions_type: Any = pathfind_t.functions_type()
    if functions_type is FNsHeurV:
        assert (heur_fn is not None) and isinstance(heur_fn, HeurFnV)
        return FNsHeurV(heur_fn)
    elif functions_type is FNsHeurQ:
        assert (heur_fn is not None) and isinstance(heur_fn, HeurFnQ)
        return FNsHeurQ(heur_fn)
    elif functions_type is FNsPolicy:
        assert policy_fn is not None
        return FNsPolicy(policy_fn)
    elif functions_type is FNsHeurVPolicy:
        assert (heur_fn is not None) and isinstance(heur_fn, HeurFnV)
        assert policy_fn is not None
        return FNsHeurVPolicy(heur_fn, policy_fn)
    elif functions_type is FNsHeurQPolicy:
        assert (heur_fn is not None) and isinstance(heur_fn, HeurFnQ)
        assert policy_fn is not None
        return FNsHeurQPolicy(heur_fn, policy_fn)
    elif functions_type is Any:
        return None
    else:
        raise ValueError(f"Unknown Function type {functions_type}")


def get_domain_compat_pathfind_names(domain_t: Type[Domain]) -> List[str]:
    """ Return the registered pathfinder names that accept ``domain_t``.

    A pathfinder is compatible if ``domain_t`` is a subclass of the pathfinder's
    declared ``domain_type()``.

    :param domain_t: The concrete domain class to check compatibility for.
    :return: List of pathfinder registration keys compatible with the domain.
    """
    pathfind_names: List[str] = []
    for pathfind_name in pathfinding_factory.get_all_class_names():
        pathfind_t: Type[PathFind] = pathfinding_factory.get_type(pathfind_name)
        if issubclass(domain_t, pathfind_t.domain_type()):
            pathfind_names.append(pathfind_name)

    return pathfind_names
