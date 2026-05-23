""" Supervised-learning updaters: train targets are the path costs produced
by supervised random-walk pathfinders (see ``deepxube/pathfinding/supervised_*``).

Three concrete updaters — for policy, V-heuristic, and Q-heuristic networks —
all register with ``updater_factory`` so the CLI can pick them when
``--pathfind`` resolves to a supervised pathfinder.
"""

from typing import List, Type, Any

from numpy.typing import NDArray

from deepxube.base.domain import Domain, State, Action, Goal
from deepxube.base.pathfinding import Node, EdgeQ, InstanceEdge, InstanceNode
from deepxube.base.updater import UpdatePolicy, UpdateHeurV, UpdateHeurQ, UpdateSup
from deepxube.factories.updater_factory import updater_factory
from deepxube.utils.timing_utils import Times
from deepxube.pathfinding.supervised_v import PathFindNodeSup
from deepxube.pathfinding.supervised_q import PathFindEdgeSup

import numpy as np


@updater_factory.register_class("update_policy_sup")
class UpdatePolicySup(UpdatePolicy[Domain, Any, PathFindEdgeSup, InstanceEdge], UpdateSup[Domain, PathFindEdgeSup, InstanceEdge]):
    """ Supervised policy updater: training targets are the actions taken along
    each random-walk path produced by ``PathFindEdgeSup``.
    """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Accepts any ``Domain`` (no additional mixin required). """
        return Domain

    @staticmethod
    def pathfind_type() -> Type[PathFindEdgeSup]:
        """ :return: Requires an edge-based supervised pathfinder. """
        return PathFindEdgeSup

    def _get_instance_data_norb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]:
        """ Convert popped edges from finished instances into training numpy
        arrays (state, goal, action) for the policy network.

        :param instances: Finished supervised instances.
        :param times: Timer accumulator (unused here but part of the
            signature).
        :return: List of numpy arrays ready for policy training.
        """
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())

        states: List[State] = [edge.node.state for edge in edges_popped]
        goals: List[Goal] = [edge.node.goal for edge in edges_popped]
        actions: List[Action] = [edge.action for edge in edges_popped]

        inputs_np: List[NDArray] = self.get_policy_nnet_par().to_np_train(states, goals, actions)
        return inputs_np


@updater_factory.register_class("update_heurv_sup")
class UpdateHeurVSup(UpdateHeurV[Domain, Any, PathFindNodeSup], UpdateSup[Domain, PathFindNodeSup, InstanceNode]):
    """ Supervised V-heuristic updater: training target is the node's
    ``heuristic`` cost-to-go computed by ``PathFindNodeSup``.
    """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Accepts any ``Domain``. """
        return Domain

    @staticmethod
    def pathfind_type() -> Type[PathFindNodeSup]:
        """ :return: Requires a node-based supervised pathfinder. """
        return PathFindNodeSup

    def _get_instance_data_norb(self, instances: List[InstanceNode], times: Times) -> List[NDArray]:
        """ Convert popped nodes from finished instances into training numpy
        arrays (state, goal, ctg) for the V-heuristic network.

        :param instances: Finished supervised instances.
        :param times: Timer accumulator (unused here).
        :return: List of numpy arrays, last element is the cost-to-go target.
        """
        nodes_popped: List[Node] = []
        for instance in instances:
            nodes_popped.extend(instance.get_nodes_popped())

        states: List[State] = [node.state for node in nodes_popped]
        goals: List[Goal] = [node.goal for node in nodes_popped]

        ctgs_backup: List[float] = [node.heuristic for node in nodes_popped]
        inputs_np: List[NDArray] = self.get_heur_nnet_par().to_np(states, goals)
        return inputs_np + [np.array(ctgs_backup)]


@updater_factory.register_class("update_heurq_sup")
class UpdateHeurQSup(UpdateHeurQ[Domain, Any, PathFindEdgeSup], UpdateSup[Domain, PathFindEdgeSup, InstanceEdge]):
    """ Supervised Q-heuristic updater: training target is the edge's
    ``q_val`` computed by ``PathFindEdgeSup``.
    """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Accepts any ``Domain``. """
        return Domain

    @staticmethod
    def pathfind_type() -> Type[PathFindEdgeSup]:
        """ :return: Requires an edge-based supervised pathfinder. """
        return PathFindEdgeSup

    def _get_instance_data_norb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]:
        """ Convert popped edges from finished instances into training numpy
        arrays (state, goal, action, q_val) for the Q-heuristic network.

        :param instances: Finished supervised instances.
        :param times: Timer accumulator (unused here).
        :return: List of numpy arrays, last element is the Q-value target.
        """
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())

        states: List[State] = [edge.node.state for edge in edges_popped]
        goals: List[Goal] = [edge.node.goal for edge in edges_popped]
        actions: List[Action] = [edge.action for edge in edges_popped]

        ctgs_backup: List[float] = [edge.q_val for edge in edges_popped]
        inputs_np: List[NDArray] = self.get_heur_nnet_par().to_np(states, goals, [[action] for action in actions])
        return inputs_np + [np.array(ctgs_backup)]
