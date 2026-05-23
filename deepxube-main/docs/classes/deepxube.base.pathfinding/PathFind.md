---
id: "class:deepxube.base.pathfinding.PathFind"
kind: "class"
name: "PathFind"
qualified_name: "deepxube.base.pathfinding.PathFind"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 260
line_end: 397
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters:
  - "D"
  - "FNs"
  - "I"
bases:
  - name: "Generic[D, FNs, I]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.pathfinding.PathFind.domain_type"
  - "func:deepxube.base.pathfinding.PathFind.functions_type"
  - "func:deepxube.base.pathfinding.PathFind.__init__"
  - "func:deepxube.base.pathfinding.PathFind.make_instances"
  - "func:deepxube.base.pathfinding.PathFind.add_instances"
  - "func:deepxube.base.pathfinding.PathFind.expand_states"
  - "func:deepxube.base.pathfinding.PathFind.get_state_actions"
  - "func:deepxube.base.pathfinding.PathFind.step"
  - "func:deepxube.base.pathfinding.PathFind.remove_finished_instances"
  - "func:deepxube.base.pathfinding.PathFind.remove_instances"
  - "func:deepxube.base.pathfinding.PathFind.set_is_solved"
  - "func:deepxube.base.pathfinding.PathFind._set_node_vals"
  - "func:deepxube.base.pathfinding.PathFind._create_root_nodes"
  - "func:deepxube.base.pathfinding.PathFind._verbose"
attributes:
  - name: "self.domain"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.functions"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.instances"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.itr"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.times"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.PathFind`

**File:** [deepxube/base/pathfinding.py:260](../../../deepxube/base/pathfinding.py#L260)
**Abstract:** yes
**Generic parameters:** `D, FNs, I`

## Docstring

Abstract batched pathfinder. Holds a list of in-progress instances and
drives them all forward one ``step()`` at a time. 

## Inheritance

**Direct bases:**
- `Generic[D, FNs, I]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `domain_type` *(trivial, skipped)*
- `functions_type` *(trivial, skipped)*
- `__init__`
- `make_instances` *(trivial, skipped)*
- `add_instances` *(trivial, skipped)*
- `expand_states` *(trivial, skipped)*
- `get_state_actions` *(trivial, skipped)*
- `step` *(trivial, skipped)*
- `remove_finished_instances`
- `remove_instances`
- `set_is_solved`
- `_set_node_vals` *(trivial, skipped)*
- `_create_root_nodes`
- `_verbose`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.domain` | — | __init__ |
| `self.functions` | — | __init__ |
| `self.instances` | — | __init__ |
| `self.itr` | — | __init__ |
| `self.times` | — | __init__ |

## Source

```python
class PathFind(Generic[D, FNs, I], ABC):
    """ Abstract batched pathfinder. Holds a list of in-progress instances and
    drives them all forward one ``step()`` at a time. """

    @staticmethod
    @abstractmethod
    def domain_type() -> Type[D]:
        """ :return: Minimum ``Domain`` type this pathfinder supports. """
        pass

    @staticmethod
    @abstractmethod
    def functions_type() -> Type[FNs]:
        """ :return: ``FNs*`` bundle class this pathfinder needs. """
        pass

    def __init__(self, domain: D, functions: FNs):
        """ Bind to a domain and a function bundle; init empty instance list. """
        assert isinstance(domain, self.domain_type()), f"Domain {domain} must be an instance of {self.domain_type()}."
        if self.functions_type() is not Any:
            assert isinstance(functions, self.functions_type()), f"Functions {functions} must be an instance of {self.functions_type()}."
        self.domain: D = domain
        self.functions: FNs = functions
        self.instances: List[I] = []
        self.times: Times = Times()
        self.itr: int = 0

    @abstractmethod
    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True) -> List[I]:
        """ Make instances from states and goals

        :param states: List of states
        :param goals: List of goals
        :param inst_infos: Optional list of information to add to an instance
        :param compute_root_vals: If true, compute the values for the root node. Some algorithms may have to ignore this argument and always compute it.
        :return: List of instances
        """
        pass

    def add_instances(self, instances: List[I]) -> None:
        """ Append new instances to the active set. """
        self.instances.extend(instances)

    @abstractmethod
    def expand_states(self, states: List[State], goals: List[Goal]) -> Tuple[List[List[State]], List[List[Action]], List[List[float]]]:
        """ For each (state, goal), return its child states, actions, and transition costs. """
        pass

    @abstractmethod
    def get_state_actions(self, states: List[State], goals: List[Goal]) -> List[List[Action]]:
        """ :return: Per-state list of applicable actions. """
        pass

    @abstractmethod
    def step(self, verbose: bool = False) -> Tuple[List[Node], List[EdgeQ]]:
        """ Advance every active instance by one search step; return popped nodes and pushed edges. """
        pass

    def remove_finished_instances(self, itr_max: int) -> List[I]:
        """ Remove instances that are finished or have run for ``itr_max`` iterations; return the removed list. """
        def remove_instance_fn(inst_in: I) -> bool:
            if inst_in.finished():
                return True
            if inst_in.itr >= itr_max:
                return True
            return False

        return self.remove_instances(remove_instance_fn)

    def remove_instances(self, test_rem: Callable[[I], bool]) -> List[I]:
        """ Remove instances

        :param test_rem: A Callable that takes an instance as input and returns true if the instance should be removed
        :return: List of removed instances
        """
        instances_remove: List[I] = []
        instances_keep: List[I] = []
        for instance in self.instances:
            if test_rem(instance):
                instances_remove.append(instance)
            else:
                instances_keep.append(instance)

        self.instances = instances_keep

        return instances_remove

    def set_is_solved(self, nodes: List[Node]) -> None:
        """ Populate ``node.is_solved`` for each node by querying the domain. """
        start_time = time.time()
        states: List[State] = []
        goals: List[Goal] = []
        for node in nodes:
            states.append(node.state)
            goals.append(node.goal)

        is_solved_l: List[bool] = self.domain.is_solved(states, goals)
        for node, is_solved in zip(nodes, is_solved_l, strict=True):
            node.is_solved = is_solved

        self.times.record_time("is_solved", time.time() - start_time)

    @abstractmethod
    def _set_node_vals(self, nodes: List[Node]) -> None:
        """ Subclass hook: populate ``heuristic``, ``q_values``, or ``act_probs`` on each node. """
        pass

    def _create_root_nodes(self, states: List[State], goals: List[Goal], compute_root_vals: bool) -> List[Node]:
        """ Build per-instance root nodes; optionally evaluate their heuristic/Q values. """
        start_time = time.time()

        root_nodes: List[Node] = []
        for state, goal in zip(states, goals, strict=True):
            root_node: Node = Node(state, goal, 0.0, 0.0, None, None, None, None, None)
            root_nodes.append(root_node)

        self.times.record_time("root", time.time() - start_time)

        if compute_root_vals:
            self._set_node_vals(root_nodes)

        return root_nodes

    def _verbose(self, instances: List[I], nodes_by_inst: List[List[Node]]) -> None:
        """ Print per-iteration summary stats (heuristic min/max, frontier sizes, solve rate). """
        nodes_flat: List[Node] = misc_utils.flatten(nodes_by_inst)[0]
        if len(nodes_flat) > 0:
            heuristics: List[float] = [node.heuristic for node in nodes_flat]
            path_costs: List[float] = [node.path_cost for node in nodes_flat]
            frontier_sizes: List[int] = [instance.frontier_size() for instance in instances]
            per_has_soln: float = 100.0 * float(np.mean([inst.has_soln() for inst in instances]))
            per_finished: float = 100.0 * float(np.mean([inst.finished() for inst in instances]))

            print(f"Itr: {self.itr}, Heur(PathCost)(Min/Max): "
                  f"{float(np.min(heuristics)):.2E}({float(path_costs[np.argmin(heuristics)]):.2E})/"
                  f"{float(np.max(heuristics)):.2E}({float(path_costs[np.argmax(heuristics)]):.2E}),"
                  f" Frontier sizes(Min/Max): {min(frontier_sizes)}/{max(frontier_sizes)}, %has_soln: {per_has_soln}, %finished: {per_finished}")
        print(f"Times - {self.times.get_time_str()}\n")
```
