---
id: "class:deepxube.pathfinding.graph_search.InstanceGraph"
kind: "class"
name: "InstanceGraph"
qualified_name: "deepxube.pathfinding.graph_search.InstanceGraph"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 24
line_end: 108
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters:
  - "SchOver"
bases:
  - name: "Instance"
    resolved_id: null
  - name: "Generic[SchOver]"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.InstanceGraph.__init__"
  - "func:deepxube.pathfinding.graph_search.InstanceGraph.set_batch_size"
  - "func:deepxube.pathfinding.graph_search.InstanceGraph.set_weight"
  - "func:deepxube.pathfinding.graph_search.InstanceGraph.set_eps"
  - "func:deepxube.pathfinding.graph_search.InstanceGraph.frontier_size"
  - "func:deepxube.pathfinding.graph_search.InstanceGraph.record_goal"
  - "func:deepxube.pathfinding.graph_search.InstanceGraph.finished"
  - "func:deepxube.pathfinding.graph_search.InstanceGraph._push_to_open"
  - "func:deepxube.pathfinding.graph_search.InstanceGraph._pop_from_open"
  - "func:deepxube.pathfinding.graph_search.InstanceGraph._check_closed"
attributes:
  - name: "self.batch_size"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.closed_dict"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.eps"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.heappush_count"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.lb"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.open_set"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.ub"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.weight"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.InstanceGraph`

**File:** [deepxube/pathfinding/graph_search.py:24](../../../deepxube/pathfinding/graph_search.py#L24)
**Abstract:** no
**Generic parameters:** `SchOver`

## Docstring

Per-instance graph-search state: min-heap open set, closed dict, best upper bound, and current lower bound. 

## Inheritance

**Direct bases:**
- `Instance`
- `Generic[SchOver]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `set_batch_size` *(trivial, skipped)*
- `set_weight` *(trivial, skipped)*
- `set_eps` *(trivial, skipped)*
- `frontier_size` *(trivial, skipped)*
- `record_goal`
- `finished` *(trivial, skipped)*
- `_push_to_open`
- `_pop_from_open`
- `_check_closed`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.batch_size` | — | __init__ |
| `self.closed_dict` | — | __init__ |
| `self.eps` | — | __init__ |
| `self.heappush_count` | — | __init__ |
| `self.lb` | — | __init__ |
| `self.open_set` | — | __init__ |
| `self.ub` | — | __init__ |
| `self.weight` | — | __init__ |

## Source

```python
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
```
