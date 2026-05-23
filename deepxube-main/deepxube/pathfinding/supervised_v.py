""" Supervised V-pathfinder: each "step" emits a single node carrying the
random-walk path cost as its heuristic target. Used by ``UpdateHeurVSup`` to
generate (state, goal, ctg) training tuples without running an actual search. """

from abc import ABC
from typing import List, Any, Optional, Type, TypeVar, Tuple
from deepxube.base.domain import Domain, State, Goal, StartGoalWalkable, GoalStartRevWalkable
from deepxube.base.pathfinding import InstanceNode, Node, EdgeQ, PathFindNode, PathFindSup
from deepxube.factories.pathfinding_factory import pathfinding_factory
import time


class InstanceNodeSup(InstanceNode):
    """ Supervised one-shot instance: just carries the random-walk target path cost. """

    def filter_expanded_nodes(self, nodes: List[Node]) -> List[Node]:
        """ Not used for supervised instances. """
        raise NotImplementedError

    def frontier_size(self) -> int:
        """ Not used for supervised instances. """
        raise NotImplementedError

    def record_goal(self, nodes: List[Node]) -> None:
        """ Not used for supervised instances. """
        raise NotImplementedError

    def push_pop_nodes(self, nodes: List[Node], costs: List[float]) -> List[Node]:
        """ Not used for supervised instances. """
        raise NotImplementedError

    def __init__(self, root_node: Node, path_cost_sup: float, inst_info: Any):
        """ Initialise with the random-walk path cost as the heuristic target. """
        super().__init__(root_node, inst_info)
        self.path_cost_sup: float = path_cost_sup

    def finished(self) -> bool:
        """ :return: True after one iteration (single emission per instance). """
        return self.itr > 0


D = TypeVar('D', bound=Domain)


class PathFindNodeSup(PathFindNode[D, Any, InstanceNodeSup], PathFindSup[D, InstanceNodeSup], ABC):
    """ Abstract supervised V pathfinder: ``step`` emits the root node and finishes. """

    def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]:
        """ Emit each instance's root node with its supervised path cost as heuristic. """
        nodes: List[Node] = []
        for instance in self.instances:
            node_root: Node = instance.root_node
            node_root.heuristic = instance.path_cost_sup
            node_root.backup_val = instance.path_cost_sup
            nodes.append(node_root)
            instance.add_nodes_popped([node_root])
            instance.itr += 1
        start_time = time.time()
        self.set_is_solved(nodes)
        self.times.record_time("is_solved", time.time() - start_time)

        return nodes, []

    def _compute_costs(self, instances: List[InstanceNodeSup], nodes_by_inst: List[List[Node]]) -> List[List[float]]:
        """ Not used: supervised pathfinders skip cost computation. """
        raise NotImplementedError

    def _make_instances(self, states_start: List[State], goals: List[Goal], path_costs: List[float], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]:
        """ Build one ``InstanceNodeSup`` per (state, goal, target path-cost) triple. """
        nodes_root: List[Node] = self._create_root_nodes(states_start, goals, False)

        start_time = time.time()
        if inst_infos is None:
            inst_infos = [None for _ in states_start]

        instances: List[InstanceNodeSup] = []
        for node_root, path_cost, inst_info in zip(nodes_root, path_costs, inst_infos):
            instances.append(InstanceNodeSup(node_root, path_cost, inst_info))
        self.times.record_time("instances", time.time() - start_time)

        return instances

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"


@pathfinding_factory.register_class("sup_v_rw")
class PathFindNodeSupRW(PathFindNodeSup[StartGoalWalkable]):
    """ Supervised V pathfinder driven by forward random walks from sampled start states. """

    @staticmethod
    def domain_type() -> Type[StartGoalWalkable]:
        """ :return: Requires ``StartGoalWalkable``. """
        return StartGoalWalkable

    def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]:
        """ Sample start states, walk forward, derive goals from the walked states. """
        start_time = time.time()
        states_start: List[State] = self.domain.sample_start_states(len(steps_gen))
        self.times.record_time("get_start_states", time.time() - start_time)

        start_time = time.time()
        states_goal, path_costs = self.domain.random_walk(states_start, steps_gen)
        self.times.record_time("random_walk", time.time() - start_time)

        # state to goal
        start_time = time.time()
        goals: List[Goal] = self.domain.sample_goal_from_state(states_start, states_goal)
        self.times.record_time("sample_goal", time.time() - start_time)

        return self._make_instances(states_start, goals, path_costs, inst_infos)


@pathfinding_factory.register_class("sup_v_rw_rev")
class PathFindNodeSupRWRev(PathFindNodeSup[GoalStartRevWalkable]):
    """ Supervised V pathfinder driven by reverse random walks from sampled (state, goal) pairs. """

    @staticmethod
    def domain_type() -> Type[GoalStartRevWalkable]:
        """ :return: Requires ``GoalStartRevWalkable``. """
        return GoalStartRevWalkable

    def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[InstanceNodeSup]:
        """ Sample (goal-state, goal) pairs, walk backwards to derive starts. """
        start_time = time.time()
        states_goal, goals = self.domain.sample_goalstate_goal_pairs(len(steps_gen))
        self.times.record_time("samp_goal_state_goal", time.time() - start_time)

        start_time = time.time()
        states_start, path_costs = self.domain.random_walk(states_goal, steps_gen)
        self.times.record_time("random_walk", time.time() - start_time)

        return self._make_instances(states_start, goals, path_costs, inst_infos)
