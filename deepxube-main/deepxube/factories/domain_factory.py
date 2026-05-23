""" Registry for ``Domain`` subclasses.

Concrete domains in ``deepxube/domains/`` (cube3, grid, lightsout, npuzzle,
sokoban) register themselves here via ``@domain_factory.register_class("key")``.
CLI tooling resolves arguments like ``--domain grid.7`` against this registry.
"""

from deepxube.base.factory import Factory
from deepxube.base.domain import Domain


domain_factory: Factory[Domain] = Factory[Domain]("domain")
