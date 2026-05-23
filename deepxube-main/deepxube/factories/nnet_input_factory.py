""" Registry of per-(domain, nnet-input-name) ``NNetInput`` classes.

Unlike the class-only factories, ``NNetInput`` classes are keyed by the pair
``(domain_name, nnet_input_name)`` so the same input shape (e.g. ``flat_sg``)
can have different implementations per domain. Domains that implement
``DynamicNNetInput`` register their mixin-derived ``NNetInput`` classes at
module load via ``register_nnet_input_dynamic``.
"""

from typing import Dict, Tuple, Type, Callable, List

from deepxube.base.nnet_input import NNetInput, DynamicNNetInput
from deepxube.base.domain import Domain
from deepxube.factories.domain_factory import domain_factory


_nnet_input_registry: Dict[Tuple[str, str], Type[NNetInput]] = {}


def register_nnet_input(domain_name: str, nnet_input_name: str) -> Callable[[Type[NNetInput]], Type[NNetInput]]:
    """ Return a decorator that registers an ``NNetInput`` class under the
    ``(domain_name, nnet_input_name)`` pair.

    :param domain_name: Registration key of the domain this input belongs to.
    :param nnet_input_name: Short name identifying the input shape (e.g.
        ``"flat_sg"`` for flat state/goal inputs).
    :return: A decorator that records the class in the registry and returns it
        unchanged.
    :raises ValueError: If the key is already registered (via the decorator).
    """
    def deco(cls: Type[NNetInput]) -> Type[NNetInput]:
        key: Tuple[str, str] = (domain_name, nnet_input_name)
        if key in _nnet_input_registry.keys():
            raise ValueError(f"{key!r} already registered for nnet inputs")
        _nnet_input_registry[key] = cls
        return cls
    return deco


def get_domain_nnet_input_keys(domain_name: str) -> List[Tuple[str, str]]:
    """ Return every registered ``(domain_name, nnet_input_name)`` whose first
    element matches ``domain_name``.

    :param domain_name: Registration key of the domain.
    :return: List of registry keys belonging to that domain.
    """
    return [key for key in _nnet_input_registry.keys() if key[0] == domain_name]


def get_nnet_input_t(key: Tuple[str, str]) -> Type[NNetInput]:
    """ Return the ``NNetInput`` class registered under ``key``.

    :param key: ``(domain_name, nnet_input_name)`` pair.
    :return: The concrete ``NNetInput`` class.
    :raises KeyError: If ``key`` is not registered.
    """
    return _nnet_input_registry[key]


def register_nnet_input_dynamic() -> None:
    """ Register ``NNetInput`` classes for every domain implementing
    ``DynamicNNetInput``.

    Iterates ``domain_factory``, and for each domain that subclasses
    ``DynamicNNetInput`` calls ``get_dynamic_nnet_inputs()`` and registers
    every returned ``(nnet_input_name, cls)`` pair under the domain's name.
    Called once during CLI startup after domain modules have been imported.
    """
    for domain_name in domain_factory.get_all_class_names():
        domain_t: Type[Domain] = domain_factory.get_type(domain_name)
        if issubclass(domain_t, DynamicNNetInput):
            nnet_input_t_dict: Dict[str, Type[NNetInput]] = domain_t.get_dynamic_nnet_inputs()
            for nnet_input_name, nnet_input_t in nnet_input_t_dict.items():
                register_nnet_input(domain_name, f"{nnet_input_name}")(nnet_input_t)
