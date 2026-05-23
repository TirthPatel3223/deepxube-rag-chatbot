""" Batch beam search variants. Each iteration keeps the top ``beam_size``
children (selected greedily, by Boltzmann sampling at temperature ``temp``,
or with ``eps`` random replacements). Variants exist for V/Q heuristics,
policy-only, and combined V/Q + policy. Parsers live at the bottom so CLI
arguments like ``beam_v.10B_1.0T_0.1E`` work. """

from abc import ABC, abstractmethod
from typing import List, Any, Type, Optional, TypeVar, Dict
from deepxube.base.factory import Parser
from deepxube.base.domain import Domain, ActsEnum, State, Goal
from deepxube.base.pathfinding import (Instance, InstanceNode, InstanceEdge, Node, EdgeQ, FNs, FNsHV, FNsHQ, FNsPolicy, FNsHeurQ, FNsHeurV, FNsHeurQPolicy,
                                       FNsHeurVPolicy, PathFind, PathFindNode, PathFindEdge, PathFindActsPolicy, PathFindSetPolicy, PathFindSetHeurV,
                                       PathFindSetHeurQ, PathFindActsEnum)
from deepxube.factories.pathfinding_factory import pathfinding_factory
from deepxube.utils.misc_utils import boltzmann
import numpy as np
import time
import re


class InstanceBeam(Instance, ABC):
    """ Per-instance beam-search state: beam size, sampling temperature, exploration epsilon, plus best-so-far goal tracking. """

    def __init__(self, root_node: Node, inst_info: Any):
        """ Initialise with default beam_size=1, temp=0, eps=0. """
        super().__init__(root_node, inst_info)
        self.beam_size: int = 1
        self.temp: float = 0.0
        self.eps: float = 0.0

    def set_beam_size(self, beam_size: int) -> None:
        """ Set the per-step beam size (>= 1). """
        assert beam_size >= 1
        self.beam_size = beam_size

    def set_temp(self, temp: float) -> None:
        """ Set Boltzmann sampling temperature (0 = pure argmax top-k). """
        assert temp >= 0.0
        self.temp = temp

    def set_eps(self, eps: float) -> None:
        """ Set the per-pick random-replacement probability (epsilon in [0, 1]). """
        assert (eps >= 0.0) and (eps <= 1.0)
        self.eps = eps

    def frontier_size(self) -> int:
        """ :return: Current beam-frontier size. """
        return len(self._nodes_curr)

    def record_goal(self, nodes: List[Node]) -> None:
        """ Record the best (lowest-cost) solved node seen so far. """
        for node in nodes:
            assert node.is_solved is not None
            if node.is_solved:
                if (self.goal_node is None) or (self.goal_node.path_cost > node.path_cost):
                    self.goal_node = node

    def select_idxs_from_logits(self, logits: List[float]) -> List[int]:
        """ Pick ``beam_size`` indices greedily, by Boltzmann sampling, or with epsilon random replacement. """
        num_logits: int = len(logits)
        next_idxs: List[int]
        if len(logits) <= self.beam_size:
            next_idxs = list(range(num_logits))
        else:
            # get next idxs
            if self.temp == 0:
                next_idxs = (np.argpartition(logits, -self.beam_size)[-self.beam_size:]).tolist()
            else:
                # select next according to boltzmann
                probs: List[float] = boltzmann(logits, self.temp)
                next_idxs = np.random.choice(num_logits, size=self.beam_size, replace=False, p=probs).tolist()

            # randomly select index
            if self.eps > 0:
                replace_rand_idxs: List[int] = np.where(np.random.random(len(next_idxs)) < self.eps)[0].tolist()
                num_replace: int = len(replace_rand_idxs)
                if num_replace > 0:
                    next_idxs_rand: List[int] = np.random.choice(num_logits, replace=False, size=num_replace).tolist()
                    for replace_idx, next_idx_rand in zip(replace_rand_idxs, next_idxs_rand):
                        next_idxs[replace_idx] = next_idx_rand
                    next_idxs = list(set(next_idxs))
        return next_idxs

    def finished(self) -> bool:
        """ :return: True once a solved goal has been recorded. """
        return self.has_soln()


D = TypeVar('D', bound=Domain)
IBeam = TypeVar('IBeam', bound=InstanceBeam)


class BeamSearch(PathFind[D, FNs, IBeam], ABC):
    """ Abstract beam-search base. Carries default beam size, temperature, and epsilon used when constructing instances. """

    def __init__(self, domain: D, functions: FNs, beam_size: int = 1, temp: float = 0.0, eps: float = 0.0):
        """ Store default beam-search parameters; per-instance overrides may be supplied to ``make_instances``. """
        super().__init__(domain, functions)
        self.beam_size_default: int = beam_size
        self.temp_default: float = temp
        self.eps_default: float = eps

    def _construct_instances(self, inst_cls: type[IBeam], nodes_root: List[Node], inst_infos: Optional[List[Any]], beam_size: Optional[int],
                             temp: Optional[float], eps: Optional[float]) -> List[IBeam]:
        """ Instantiate ``inst_cls`` for each root node and apply beam-size / temp / eps (instance overrides take precedence). """
        if inst_infos is None:
            inst_infos = [None for _ in nodes_root]

        beam_size_inst: int = beam_size if beam_size is not None else self.beam_size_default
        temp_inst: float = temp if temp is not None else self.temp_default
        eps_inst: float = eps if eps is not None else self.eps_default

        instances: List[IBeam] = [inst_cls(node_root, inst_info) for node_root, inst_info in zip(nodes_root, inst_infos, strict=True)]
        for instance in instances:
            instance.set_beam_size(beam_size_inst)
            instance.set_temp(temp_inst)
            instance.set_eps(eps_inst)

        return instances

    def __repr__(self) -> str:
        return f"{type(self).__name__}(beam_size={self.beam_size_default}, temp={self.temp_default}, eps={self.eps_default})"


class InstanceNodeBeam(InstanceNode, InstanceBeam):
    """ Node-driven beam instance: keeps the top ``beam_size`` expanded children. """

    def filter_expanded_nodes(self, nodes: List[Node]) -> List[Node]:
        """ No filtering — keep all expanded children. """
        return nodes

    def push_pop_nodes(self, nodes: List[Node], costs: List[float]) -> List[Node]:
        """ Pick the beam from the expanded nodes by their costs (logits). """
        next_idxs: List[int] = self.select_idxs_from_logits(costs)
        return [nodes[idx] for idx in next_idxs]


class InstanceEdgeBeam(InstanceEdge, InstanceBeam):
    """ Edge-driven beam instance: beam selects from edges (action probabilities or Q-values). """

    def __init__(self, root_node: Node, inst_info: Any):
        """ Initialise plus an empty list to hold currently-selected edges. """
        super().__init__(root_node, inst_info)
        self.beam_edges: List[EdgeQ] = []

    def filter_popped_nodes(self, nodes: List[Node]) -> List[Node]:
        """ No filtering — keep all popped nodes. """
        return nodes

    def push_pop_edges(self, edges: List[EdgeQ], costs: List[float]) -> List[EdgeQ]:
        """ Pick the beam from candidate edges by their logits. """
        next_idxs: List[int] = self.select_idxs_from_logits(costs)
        return [edges[idx] for idx in next_idxs]


@pathfinding_factory.register_class("beam_p")
class BeamSearchPolicy(BeamSearch[Domain, FNsPolicy, InstanceEdgeBeam], PathFindEdge[Domain, FNsPolicy, InstanceEdgeBeam],
                       PathFindActsPolicy[Domain, FNsPolicy, InstanceEdgeBeam], PathFindSetPolicy[Domain, FNsPolicy, InstanceEdgeBeam]):
    """ Policy-driven beam search: edges chosen by the policy network's action probabilities. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    @staticmethod
    def functions_type() -> Type[FNsPolicy]:
        """ :return: ``FNsPolicy``. """
        return FNsPolicy

    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       beam_size: Optional[int] = None, temp: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceEdgeBeam]:
        """ Build edge-beam instances from (state, goal) pairs with optional per-call beam parameter overrides. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, True)
        return self._construct_instances(InstanceEdgeBeam, nodes_root, inst_infos, beam_size, temp, eps)

    def _compute_costs(self, instances: List[InstanceEdgeBeam], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]:
        """ Logits = the policy's per-edge log-probabilities (already in ``edge.q_val``). """
        start_time = time.time()
        logits_by_inst: List[List[float]] = []
        for edges in edges_by_inst:
            logits: List[float] = [edge.q_val for edge in edges]  # corresponds to prob densities
            logits_by_inst.append(logits)

        self.times.record_time("logits", time.time() - start_time)

        return logits_by_inst


class BeamSearchHeurNode(BeamSearch[D, FNsHV, InstanceNodeBeam], PathFindNode[D, FNsHV, InstanceNodeBeam],
                         PathFindSetHeurV[D, FNsHV, InstanceNodeBeam], ABC):
    """ Abstract node-driven beam search guided by a value heuristic (V). Logits = -(transition_cost + heuristic). """

    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       beam_size: Optional[int] = None, temp: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceNodeBeam]:
        """ Build node-beam instances, optionally computing root heuristic values. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, compute_root_vals)
        return self._construct_instances(InstanceNodeBeam, nodes_root, inst_infos, beam_size, temp, eps)

    def _compute_costs(self, instances: List[InstanceNodeBeam], nodes_by_inst: List[List[Node]]) -> List[List[float]]:
        """ :return: Per-instance logits = -(transition_cost + heuristic); higher is better. """
        start_time = time.time()
        logits_by_inst: List[List[float]] = []
        for nodes in nodes_by_inst:
            logits: List[float] = []
            for node in nodes:
                assert node.parent_t_cost is not None
                logits.append(-(node.parent_t_cost + node.heuristic))

            logits_by_inst.append(logits)

        self.times.record_time("logits", time.time() - start_time)

        return logits_by_inst


class BeamSearchHeurEdge(BeamSearch[D, FNsHQ, InstanceEdgeBeam], PathFindEdge[D, FNsHQ, InstanceEdgeBeam],
                         PathFindSetHeurQ[D, FNsHQ, InstanceEdgeBeam], ABC):
    """ Abstract edge-driven beam search guided by a Q heuristic. Logits = -q_val (lower Q = worse beam candidate). """

    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       beam_size: Optional[int] = None, temp: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceEdgeBeam]:
        """ Build edge-beam instances from (state, goal) pairs. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, True)
        return self._construct_instances(InstanceEdgeBeam, nodes_root, inst_infos, beam_size, temp, eps)

    def _compute_costs(self, instances: List[InstanceEdgeBeam], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]:
        """ :return: Per-instance logits = -q_val; higher is better. """
        start_time = time.time()
        logits_by_inst: List[List[float]] = []
        for edges in edges_by_inst:
            logits: List[float] = [-edge.q_val for edge in edges]
            logits_by_inst.append(logits)

        self.times.record_time("logits", time.time() - start_time)

        return logits_by_inst


@pathfinding_factory.register_class("beam_v")
class BeamSearchHeurNodeActsEnum(BeamSearchHeurNode[ActsEnum, FNsHeurV], PathFindActsEnum[ActsEnum, FNsHeurV, InstanceNodeBeam]):
    """ Concrete node-beam (V heuristic) for ActsEnum domains; registered as ``beam_v``. """

    @staticmethod
    def domain_type() -> Type[ActsEnum]:
        """ :return: ``ActsEnum``. """
        return ActsEnum

    @staticmethod
    def functions_type() -> Type[FNsHeurV]:
        """ :return: ``FNsHeurV``. """
        return FNsHeurV


@pathfinding_factory.register_class("beam_q")
class BeamSearchHeurEdgeActsEnum(BeamSearchHeurEdge[ActsEnum, FNsHeurQ], PathFindActsEnum[ActsEnum, FNsHeurQ, InstanceEdgeBeam]):
    """ Concrete edge-beam (Q heuristic) for ActsEnum domains; registered as ``beam_q``. """

    @staticmethod
    def domain_type() -> Type[ActsEnum]:
        """ :return: ``ActsEnum``. """
        return ActsEnum

    @staticmethod
    def functions_type() -> Type[FNsHeurQ]:
        """ :return: ``FNsHeurQ``. """
        return FNsHeurQ


@pathfinding_factory.register_class("beam_v_p")
class BeamSearchHeurNodeActsPolicy(BeamSearchHeurNode[Domain, FNsHeurVPolicy], PathFindActsPolicy[Domain, FNsHeurVPolicy, InstanceNodeBeam]):
    """ Concrete node-beam (V heuristic + policy) for any Domain; registered as ``beam_v_p``. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    @staticmethod
    def functions_type() -> Type[FNsHeurVPolicy]:
        """ :return: ``FNsHeurVPolicy``. """
        return FNsHeurVPolicy


@pathfinding_factory.register_class("beam_q_p")
class BeamSearchHeurEdgeActsPolicy(BeamSearchHeurEdge[Domain, FNsHeurQPolicy], PathFindActsPolicy[Domain, FNsHeurQPolicy, InstanceEdgeBeam]):
    """ Concrete edge-beam (Q heuristic + policy) for any Domain; registered as ``beam_q_p``. """

    @staticmethod
    def domain_type() -> Type[Domain]:
        """ :return: Any ``Domain``. """
        return Domain

    @staticmethod
    def functions_type() -> Type[FNsHeurQPolicy]:
        """ :return: ``FNsHeurQPolicy``. """
        return FNsHeurQPolicy


class BeamSearchParser(Parser, ABC):
    """ Abstract CLI parser for all beam-search variants; parses ``<n>B_<f>T_<f>E`` arg strings. """

    def parse(self, args_str: str) -> Dict[str, Any]:
        """ Parse an underscore-separated arg string into ``beam_size``, ``temp``, and/or ``eps`` kwargs. """
        args_str_l: List[str] = args_str.split("_")
        kwargs: Dict[str, Any] = dict()
        for args_str_i in args_str_l:
            beam_re = re.search(r"^(\S+)B$", args_str_i)
            temp_re = re.search(r"^(\S+)T", args_str_i)
            eps_re = re.search(r"^(\S+)E", args_str_i)
            if beam_re is not None:
                kwargs["beam_size"] = int(beam_re.group(1))
            elif temp_re is not None:
                kwargs["temp"] = float(temp_re.group(1))
            elif eps_re is not None:
                kwargs["eps"] = float(eps_re.group(1))
            else:
                raise ValueError(f"Unexpected argument {args_str_i!r}")
        return kwargs

    def help(self) -> str:
        """ :return: CLI usage string describing ``B``/``T``/``E`` suffixes with an example. """
        return ("<int>B (beam size), <float>T (temperature for Boltzmann distribution), <float>E (epsilon for chance to randomly select node).\n"
                f"E.g. {self._alg_name()}.10B_1.0T_0.1E")

    @abstractmethod
    def _alg_name(self) -> str:
        """ :return: The algorithm key (e.g. ``beam_v``) used in CLI help examples. """
        pass


@pathfinding_factory.register_parser("beam_p")
class BeamSearchPolicyParser(BeamSearchParser):
    """ CLI parser for the ``beam_p`` (policy-only) beam-search variant. """

    def _alg_name(self) -> str:
        return "beam_p"


@pathfinding_factory.register_parser("beam_v")
class BeamSearchNodeParser(BeamSearchParser):
    """ CLI parser for the ``beam_v`` (V heuristic) beam-search variant. """

    def _alg_name(self) -> str:
        return "beam_v"


@pathfinding_factory.register_parser("beam_q")
class BeamSearchEdgeParser(BeamSearchParser):
    """ CLI parser for the ``beam_q`` (Q heuristic) beam-search variant. """

    def _alg_name(self) -> str:
        return "beam_q"


@pathfinding_factory.register_parser("beam_v_p")
class BeamSearchNodeHasPolicyParser(BeamSearchParser):
    """ CLI parser for the ``beam_v_p`` (V heuristic + policy) beam-search variant. """

    def _alg_name(self) -> str:
        return "beam_v_p"


@pathfinding_factory.register_parser("beam_q_p")
class BeamSearchEdgeHasPolicyParser(BeamSearchParser):
    """ CLI parser for the ``beam_q_p`` (Q heuristic + policy) beam-search variant. """

    def _alg_name(self) -> str:
        return "beam_q_p"
