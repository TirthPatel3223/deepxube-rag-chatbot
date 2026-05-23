---
id: "class:deepxube.pathfinding.utils.performance.PathFindPerf"
kind: "class"
name: "PathFindPerf"
qualified_name: "deepxube.pathfinding.utils.performance.PathFindPerf"
module: "deepxube.pathfinding.utils.performance"
file: "deepxube/pathfinding/utils/performance.py"
line_start: 15
line_end: 63
is_abstract: false
is_dataclass: true
decorators:
  - "@dataclass"
generic_parameters: []
bases: []
methods:
  - "func:deepxube.pathfinding.utils.performance.PathFindPerf.__init__"
  - "func:deepxube.pathfinding.utils.performance.PathFindPerf.update_perf"
  - "func:deepxube.pathfinding.utils.performance.PathFindPerf.comb_perf"
  - "func:deepxube.pathfinding.utils.performance.PathFindPerf.per_solved"
  - "func:deepxube.pathfinding.utils.performance.PathFindPerf.stats"
  - "func:deepxube.pathfinding.utils.performance.PathFindPerf.to_string"
attributes:
  - name: "self.ctgs"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.ctgs_bkup"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.is_solved_l"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.path_costs"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.search_itrs_l"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.utils.performance.PathFindPerf`

**File:** [deepxube/pathfinding/utils/performance.py:15](../../../deepxube/pathfinding/utils/performance.py#L15)
**Abstract:** no
**Dataclass:** yes
**Decorators:** `@dataclass`

## Docstring

Aggregator for per-instance search outcomes; records solve flags, path costs, search iterations, and root heuristic / backup values. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `update_perf`
- `comb_perf`
- `per_solved`
- `stats`
- `to_string`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.ctgs` | — | __init__ |
| `self.ctgs_bkup` | — | __init__ |
| `self.is_solved_l` | — | __init__ |
| `self.path_costs` | — | __init__ |
| `self.search_itrs_l` | — | __init__ |

## Source

```python
class PathFindPerf:
    """ Aggregator for per-instance search outcomes; records solve flags, path costs, search iterations, and root heuristic / backup values. """

    def __init__(self) -> None:
        """ Initialise empty stat lists. """
        self.is_solved_l: List[bool] = []
        self.path_costs: List[float] = []
        self.search_itrs_l: List[int] = []
        self.ctgs: List[float] = []
        self.ctgs_bkup: List[float] = []

    def update_perf(self, instance: Instance) -> None:
        """ Fold one finished instance's outcome into the running stats. """
        self.is_solved_l.append(instance.has_soln())
        self.ctgs.append(instance.root_node.heuristic)
        self.ctgs_bkup.append(instance.root_node.backup_val)
        if instance.has_soln():
            self.path_costs.append(instance.path_cost())
            self.search_itrs_l.append(instance.itr)

    def comb_perf(self, search_perf2: 'PathFindPerf') -> 'PathFindPerf':
        """ Concatenate stats from another ``PathFindPerf`` into a new one. """
        search_perf_new: PathFindPerf = PathFindPerf()
        search_perf_new.is_solved_l = self.is_solved_l + search_perf2.is_solved_l
        search_perf_new.path_costs = self.path_costs + search_perf2.path_costs
        search_perf_new.search_itrs_l = self.search_itrs_l + search_perf2.search_itrs_l
        search_perf_new.ctgs = self.ctgs + search_perf2.ctgs
        search_perf_new.ctgs_bkup = self.ctgs_bkup + search_perf2.ctgs_bkup

        return search_perf_new

    def per_solved(self) -> float:
        """ :return: Percent solved across recorded instances. """
        return 100.0 * float(np.mean(self.is_solved_l))

    def stats(self) -> Tuple[float, float, float]:
        """ :return: ``(percent_solved, mean_path_cost, mean_search_itrs)`` over solved instances. """
        path_cost_ave: float = 0.0
        search_itrs_ave: float = 0.0
        if len(self.path_costs) > 0:
            path_cost_ave = float(np.mean(self.path_costs))
            search_itrs_ave = float(np.mean(self.search_itrs_l))

        return self.per_solved(), path_cost_ave, search_itrs_ave

    def to_string(self) -> str:
        """ :return: One-line human summary of the stats. """
        per_solved, path_cost_ave, search_itrs_ave = self.stats()
        return f"%solved: {per_solved:.2f}, path_costs: {path_cost_ave:.3f}, search_itrs: {search_itrs_ave:.3f}"
```
