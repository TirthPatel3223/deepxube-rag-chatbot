""" Weighted best-first graph-search variants (A*, GBFS, and hybrids). Supports node-based V heuristics and
edge-based Q heuristics, batch expansion, and epsilon-random pop. Parsers at the bottom enable CLI flags like
``graph_v.10B_0.5W_0.1E``. """

from abc import ABC, abstractmethod
from typing import List, Any, Type, Optional, TypeVar, Generic, Tuple, Dict
from deepxube.base.factory import Parser
from deepxube.base.domain import Domain, ActsEnum, State, Goal
from deepxube.base.pathfinding import (Instance, InstanceNode, InstanceEdge, Node, EdgeQ, FNs, FNsHV, FNsHQ, FNsHeurQ, FNsHeurV, FNsHeurQPolicy,
                                       FNsHeurVPolicy, PathFind, PathFindNode, PathFindEdge, PathFindActsPolicy, PathFindSetHeurV, PathFindSetHeurQ,
                                       PathFindActsEnum)
from deepxube.factories.pathfinding_factory import pathfinding_factory
from deepxube.utils import misc_utils
from heapq import heappush, heappop, heapify
import numpy as np
import random
import time
import re


SchOver = TypeVar("SchOver")


class InstanceGraph(Instance, Generic[SchOver]):
    """ Per-instance graph-search state: min-heap open set, closed dict, best upper bound, and current lower bound. """

    def __init__(self, root_node: Node, inst_info: Any):
        """ Initialise heap, closed dict, ub=inf, lb=root heuristic; default batch_size=1, weight=1.0, eps=0.0. """
        super().__init__(root_node, inst_info)
        self.open_set: List[Tuple[float, int, SchOver]] = []
        self.heappush_count: int = 0
        self.closed_dict: Dict[State, float] = {}
        self.ub: float = np.inf
        self.lb: float = self.root_node.heuristic
        self.batch_size: int = 1
        self.weight: float = 1.0
        self.eps: float = 0.0

    def set_batch_size(self, batch_size: int) -> None:
        """ Set how many nodes/edges to pop from the open set per iteration (>= 1). """
        assert batch_size >= 1
        self.batch_size = batch_size

    def set_weight(self, weight: float) -> None:
        """ Set the path-cost weight in [0, 1] (0 = GBFS, 1 = A*). """
        assert (weight <= 1) and (weight >= 0)
        self.weight = weight

    def set_eps(self, eps: float) -> None:
        """ Set the probability of popping a random element instead of the minimum (epsilon in [0, 1]). """
        assert (eps <= 1) and (eps >= 0)
        self.eps = eps

    def frontier_size(self) -> int:
        """ :return: Number of items currently in the open set. """
        return len(self.open_set)

    def record_goal(self, nodes: List[Node]) -> None:
        """ Record the cheapest solved node found so far and update the upper bound. """
        # keep solved nodes for training
        for node in nodes:
            assert node.is_solved is not None
            if node.is_solved and (self.ub > node.path_cost):
                self.goal_node = node
                self.ub = node.path_cost

    def finished(self) -> bool:
        """ :return: True when the lower bound meets the weighted upper bound, or the open set is empty. """
        case1: bool = (self.goal_node is not None) and (self.lb >= (self.weight * self.ub))
        case2: bool = (self.itr > 0) and (len(self._nodes_curr) == 0)
        return case1 or case2

    def _push_to_open(self, sch_over_l: List[SchOver], costs: List[float]) -> None:
        """ Push (cost, tie-break count, item) tuples onto the min-heap. """
        for sch_over, cost in zip(sch_over_l, costs, strict=True):
            heappush(self.open_set, (cost, self.heappush_count, sch_over))
            self.heappush_count += 1

    def _pop_from_open(self) -> List[SchOver]:
        """ Pop up to ``batch_size`` items; with probability ``eps`` each pick is drawn uniformly at random. """
        num_to_pop: int = min(self.batch_size, len(self.open_set))

        elems_popped: List[Tuple[float, int, SchOver]] = []
        for _ in range(num_to_pop):
            if random.random() < self.eps:
                pop_idx: int = random.randrange(0, len(self.open_set))
                elems_popped.append(self.open_set.pop(pop_idx))
                heapify(self.open_set)
            else:
                elems_popped.append(heappop(self.open_set))

        sch_over_popped: List[SchOver] = [elem_popped[2] for elem_popped in elems_popped]

        if len(elems_popped) > 0:
            cost_first: float = elems_popped[0][0]
            self.lb = max(cost_first, self.lb)

        return sch_over_popped

    def _check_closed(self, nodes: List[Node]) -> List[Node]:
        """ Return only those nodes whose ``path_cost`` improves (or creates) their closed-dict entry. """
        nodes_ret: List[Node] = []
        for node in nodes:
            path_cost_prev: Optional[float] = self.closed_dict.get(node.state)
            if (path_cost_prev is None) or (path_cost_prev > node.path_cost):
                self.closed_dict[node.state] = node.path_cost
                nodes_ret.append(node)
        return nodes_ret


D = TypeVar('D', bound=Domain)
IGraph = TypeVar('IGraph', bound=InstanceGraph)


class GraphSearch(PathFind[D, FNs, IGraph], ABC):
    """ Abstract best-first graph-search base; stores default batch_size, weight, and eps. """

    def __init__(self, domain: D, functions: FNs, batch_size: int = 1, weight: float = 1.0, eps: float = 0.0):
        """ Store default batch/weight/eps parameters used when constructing instances. """
        super().__init__(domain, functions)
        self.batch_size_default: int = batch_size
        self.weight_default: float = weight
        self.eps_default: float = eps

    def _construct_instances(self, inst_cls: type[IGraph], nodes_root: List[Node], inst_infos: Optional[List[Any]], batch_size: Optional[int],
                             weight: Optional[float], eps: Optional[float]) -> List[IGraph]:
        """ Instantiate ``inst_cls`` for each root node and apply batch/weight/eps (instance overrides take precedence). """
        if inst_infos is None:
            inst_infos = [None for _ in nodes_root]

        batch_size_inst: int = batch_size if batch_size is not None else self.batch_size_default
        weight_inst: float = weight if weight is not None else self.weight_default
        eps_inst: float = eps if eps is not None else self.eps_default

        instances: List[IGraph] = [inst_cls(node_root, inst_info) for node_root, inst_info in zip(nodes_root, inst_infos, strict=True)]
        for instance in instances:
            instance.set_batch_size(batch_size_inst)
            instance.set_weight(weight_inst)
            instance.set_eps(eps_inst)

        return instances

    def __repr__(self) -> str:
        return f"{type(self).__name__}(batch_size={self.batch_size_default}, weight={self.weight_default}, eps={self.eps_default})"


class InstanceNodeGraph(InstanceNode, InstanceGraph[Node]):
    """ Node-driven graph-search instance; pre-inserts the root into the closed dict at cost 0. """

    def __init__(self, root_node: Node, inst_info: Any):
        super().__init__(root_node, inst_info)
        self.closed_dict[self.root_node.state] = 0.0

    def filter_expanded_nodes(self, nodes: List[Node]) -> List[Node]:
        """ Filter expanded children through the closed dict; discard nodes that do not improve it. """
        return self._check_closed(nodes)

    def push_pop_nodes(self, nodes: List[Node], costs: List[float]) -> List[Node]:
        """ Push nodes onto the open heap, then pop the next best batch. """
        self._push_to_open(nodes, costs)
        return self._pop_from_open()


class InstanceEdgeGraph(InstanceEdge, InstanceGraph[EdgeQ]):
    """ Edge-driven graph-search instance; closed-dict check is applied to nodes after they are popped. """

    def filter_popped_nodes(self, nodes: List[Node]) -> List[Node]:
        """ Filter popped nodes through the closed dict. """
        return self._check_closed(nodes)

    def push_pop_edges(self, edges: List[EdgeQ], costs: List[float]) -> List[EdgeQ]:
        """ Push edges onto the open heap, then pop the next best batch. """
        self._push_to_open(edges, costs)
        return self._pop_from_open()


class GraphSearchHeurNode(GraphSearch[D, FNsHV, InstanceNodeGraph], PathFindNode[D, FNsHV, InstanceNodeGraph],
                          PathFindSetHeurV[D, FNsHV, InstanceNodeGraph], ABC):
    """ Abstract node-driven graph search using a V heuristic; cost = weight * path_cost + heuristic. """

    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       beam_size: Optional[int] = None, weight: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceNodeGraph]:
        """ Build node-graph instances, optionally computing root heuristic values. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, compute_root_vals)
        return self._construct_instances(InstanceNodeGraph, nodes_root, inst_infos, beam_size, weight, eps)

    def _compute_costs(self, instances: List[InstanceNodeGraph], nodes_by_inst: List[List[Node]]) -> List[List[float]]:
        """ :return: Per-instance costs = weight * path_cost + heuristic (lower = higher priority). """
        start_time = time.time()
        nodes_c_flat: List[Node] = misc_utils.flatten(nodes_by_inst)[0]
        weights, split_idxs = misc_utils.flatten([[instance.weight] * len(nodes_c) for instance, nodes_c in zip(instances, nodes_by_inst, strict=True)])
        path_costs: List[float] = [node.path_cost for node in nodes_c_flat]
        heuristics: List[float] = [node.heuristic for node in nodes_c_flat]
        costs_flat: List[float] = ((np.array(weights) * np.array(path_costs)) + np.array(heuristics)).tolist()
        costs_by_inst: List[List[float]] = misc_utils.unflatten(costs_flat, split_idxs)

        self.times.record_time("cost", time.time() - start_time)

        return costs_by_inst


class GraphSearchHeurEdge(GraphSearch[D, FNsHQ, InstanceEdgeGraph], PathFindEdge[D, FNsHQ, InstanceEdgeGraph],
                          PathFindSetHeurQ[D, FNsHQ, InstanceEdgeGraph], ABC):
    """ Abstract edge-driven graph search using Q-values; cost = weight * node.path_cost + q_val. """

    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       batch_size: Optional[int] = None, weight: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceEdgeGraph]:
        """ Build edge-graph instances from (state, goal) pairs. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, True)
        return self._construct_instances(InstanceEdgeGraph, nodes_root, inst_infos, batch_size, weight, eps)

    def _compute_costs(self, instances: List[InstanceEdgeGraph], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]:
        """ :return: Per-instance costs = weight * node.path_cost + q_val (lower = higher priority). """
        start_time = time.time()
        edges_flat: List[EdgeQ] = misc_utils.flatten(edges_by_inst)[0]
        weights_flat, split_idxs = misc_utils.flatten([[instance.weight] * len(edges) for instance, edges in zip(instances, edges_by_inst, strict=True)])
        path_costs_flat: List[float] = [edge.node.path_cost for edge in edges_flat]
        qvals_flat: List[float] = [edge.q_val for edge in edges_flat]
        costs_flat: List[float] = ((np.array(weights_flat) * np.array(path_costs_flat)) + np.array(qvals_flat)).tolist()
        costs_by_inst: List[List[float]] = misc_utils.unflatten(costs_flat, split_idxs)

        self.times.record_time("cost", time.time() - start_time)

        return costs_by_inst


@pathfinding_factory.register_class("graph_v")
class GraphSearchHeurNodeActsEnum(GraphSearchHeurNode[ActsEnum, FNsHeurV], PathFindActsEnum[ActsEnum, FNsHeurV, InstanceNodeGraph]):
    """ Concrete node-graph search (V heuristic) for ActsEnum domains; registered as ``graph_v``. """

    @staticmethod
    def domain_type() -> Type[ActsEnum]:
        """ :return: ``ActsEnum``. """
        return ActsEnum

    @staticmethod
    def functions_type() -> Type[FNsHeurV]:
        """ :return: ``FNsHeurV``. """
        return FNsHeurV


@pathfinding_factory.register_class("graph_q")
class GraphSearchHeurEdgeActsEnum(GraphSearchHeurEdge[ActsEnum, FNsHeurQ], PathFindActsEnum[ActsEnum, FNsHeurQ, InstanceEdgeGraph]):
    """ Concrete edge-graph search (Q heuristic) for ActsEnum domains; registered as ``graph_q``. """

    @staticmethod
    def domain_type() -> Type[ActsEnum]:
        """ :return: ``ActsEnum``. """
        return ActsEnum

    @staticmethod
    def functions_type() -> Type[FNsHeurQ]:
        """ :return: ``FNsHeurQ``. """
        return FNsHeurQ


@pathfinding_factory.register_class("graph_v_p")
class GraphSearchHeurNodeActsPolicy(GraphSearchHeurNode[Domain, FNsHeurVPolicy], PathFindActsPolicy[Domain, FNsHeurVPolicy, InstanceNodeGraph]):
    """ Concrete node-graph search (V heuristic + policy) for any Domain; registered as ``graph_v_p``. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    @staticmethod
    def functions_type() -> Type[FNsHeurVPolicy]:
        """ :return: ``FNsHeurVPolicy``. """
        return FNsHeurVPolicy


@pathfinding_factory.register_class("graph_q_p")
class GraphSearchHeurEdgeActsPolicy(GraphSearchHeurEdge[Domain, FNsHeurQPolicy], PathFindActsPolicy[Domain, FNsHeurQPolicy, InstanceEdgeGraph]):
    """ Concrete edge-graph search (Q heuristic + policy) for any Domain; registered as ``graph_q_p``. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    @staticmethod
    def functions_type() -> Type[FNsHeurQPolicy]:
        """ :return: ``FNsHeurQPolicy``. """
        return FNsHeurQPolicy


class GraphSearchParser(Parser, ABC):
    """ Abstract CLI parser for all graph-search variants; parses ``<n>B_<f>W_<f>E`` arg strings. """

    def parse(self, args_str: str) -> Dict[str, Any]:
        """ Parse an underscore-separated arg string into ``batch_size``, ``weight``, and/or ``eps`` kwargs. """
        args_str_l: List[str] = args_str.split("_")
        kwargs: Dict[str, Any] = dict()
        for args_str_i in args_str_l:
            batch_size_re = re.search(r"^(\S+)B$", args_str_i)
            weight_re = re.search(r"^(\S+)W", args_str_i)
            eps_re = re.search(r"^(\S+)E", args_str_i)
            if batch_size_re is not None:
                kwargs["batch_size"] = int(batch_size_re.group(1))
            elif weight_re is not None:
                kwargs["weight"] = float(weight_re.group(1))
            elif eps_re is not None:
                kwargs["eps"] = float(eps_re.group(1))
            else:
                raise ValueError(f"Unexpected argument {args_str_i!r}")
        return kwargs

    def help(self) -> str:
        """ :return: CLI usage string describing ``B``/``W``/``E`` suffixes with an example. """
        return ("<int>B (batch size), <float>W (weight), <float>E (epsilon for chance to randomly pop node).\n"
                f"E.g. {self._alg_name()}.10B_0.5W_0.1E")

    @abstractmethod
    def _alg_name(self) -> str:
        """ :return: The algorithm key (e.g. ``graph_v``) used in CLI help examples. """
        pass


@pathfinding_factory.register_parser("graph_v")
class GraphSearchNodeParser(GraphSearchParser):
    """ CLI parser for the ``graph_v`` (V heuristic) graph-search variant. """

    def _alg_name(self) -> str:
        return "graph_v"


@pathfinding_factory.register_parser("graph_q")
class GraphSearchEdgeParser(GraphSearchParser):
    """ CLI parser for the ``graph_q`` (Q heuristic) graph-search variant. """

    def _alg_name(self) -> str:
        return "graph_q"


@pathfinding_factory.register_parser("graph_v_p")
class GraphSearchNodeHasPolicyParser(GraphSearchParser):
    """ CLI parser for the ``graph_v_p`` (V heuristic + policy) graph-search variant. """

    def _alg_name(self) -> str:
        return "graph_v_p"


@pathfinding_factory.register_parser("graph_q_p")
class GraphSearchEdgeHasPolicyParser(GraphSearchParser):
    """ CLI parser for the ``graph_q_p`` (Q heuristic + policy) graph-search variant. """

    def _alg_name(self) -> str:
        return "graph_q_p"
