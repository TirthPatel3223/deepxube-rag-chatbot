---
id: "func:deepxube.base.pathfinding.PathFind._verbose"
kind: "method"
name: "_verbose"
qualified_name: "deepxube.base.pathfinding.PathFind._verbose"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 383
line_end: 397
class: "PathFind"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "instances"
    annotation: "List[I]"
    default: null
  - name: "nodes_by_inst"
    annotation: "List[List[Node]]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "misc_utils.flatten"
    call_sites: [385]
  - target: null
    expr: "len"
    call_sites: [386]
  - target: null
    expr: "instance.frontier_size"
    call_sites: [389]
  - target: null
    expr: "float"
    call_sites: [390, 391, 394, 395]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [390, 391]
  - target: null
    expr: "inst.has_soln"
    call_sites: [390]
  - target: null
    expr: "inst.finished"
    call_sites: [391]
  - target: null
    expr: "print"
    call_sites: [393, 397]
  - target: "func:numpy.min"
    expr: "np.min"
    call_sites: [394]
  - target: "func:numpy.argmin"
    expr: "np.argmin"
    call_sites: [394]
  - target: "func:numpy.max"
    expr: "np.max"
    call_sites: [395]
  - target: "func:numpy.argmax"
    expr: "np.argmax"
    call_sites: [395]
  - target: null
    expr: "min"
    call_sites: [396]
  - target: null
    expr: "max"
    call_sites: [396]
  - target: null
    expr: "self.times.get_time_str"
    call_sites: [397]
raises: []
reads_attrs:
  - "self.itr"
  - "self.times"
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFind._verbose`

**File:** [deepxube/base/pathfinding.py:383](../../../../deepxube/base/pathfinding.py#L383)
**Class:** `PathFind`
**Visibility:** private
**Kind:** method

## Signature

```python
def _verbose(self, instances: List[I], nodes_by_inst: List[List[Node]]) -> None
```

## Docstring

Print per-iteration summary stats (heuristic min/max, frontier sizes, solve rate). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[I]` | — |
| `nodes_by_inst` | `List[List[Node]]` | — |

## Returns

`None`

## Calls

- `misc_utils.flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 385)
- `np.mean` → `func:numpy.mean` (lines: 390, 391)
- `np.min` → `func:numpy.min` (lines: 394)
- `np.argmin` → `func:numpy.argmin` (lines: 394)
- `np.max` → `func:numpy.max` (lines: 395)
- `np.argmax` → `func:numpy.argmax` (lines: 395)

### Unresolved
- `len` (lines: 386)
- `instance.frontier_size` (lines: 389)
- `float` (lines: 390, 391, 394, 395)
- `inst.has_soln` (lines: 390)
- `inst.finished` (lines: 391)
- `print` (lines: 393, 397)
- `min` (lines: 396)
- `max` (lines: 396)
- `self.times.get_time_str` (lines: 397)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.itr`
- `self.times`

## Source

```python
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
