---
id: "func:deepxube.pathfinding.utils.performance.PathFindPerf.update_perf"
kind: "method"
name: "update_perf"
qualified_name: "deepxube.pathfinding.utils.performance.PathFindPerf.update_perf"
module: "deepxube.pathfinding.utils.performance"
file: "deepxube/pathfinding/utils/performance.py"
line_start: 26
line_end: 33
class: "PathFindPerf"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "instance"
    annotation: "Instance"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "self.is_solved_l.append"
    call_sites: [28]
  - target: null
    expr: "instance.has_soln"
    call_sites: [28, 31]
  - target: null
    expr: "self.ctgs.append"
    call_sites: [29]
  - target: null
    expr: "self.ctgs_bkup.append"
    call_sites: [30]
  - target: null
    expr: "self.path_costs.append"
    call_sites: [32]
  - target: null
    expr: "instance.path_cost"
    call_sites: [32]
  - target: null
    expr: "self.search_itrs_l.append"
    call_sites: [33]
raises: []
reads_attrs:
  - "self.ctgs"
  - "self.ctgs_bkup"
  - "self.is_solved_l"
  - "self.path_costs"
  - "self.search_itrs_l"
writes_attrs: []
---

# `deepxube.pathfinding.utils.performance.PathFindPerf.update_perf`

**File:** [deepxube/pathfinding/utils/performance.py:26](../../../../deepxube/pathfinding/utils/performance.py#L26)
**Class:** `PathFindPerf`
**Visibility:** public
**Kind:** method

## Signature

```python
def update_perf(self, instance: Instance) -> None
```

## Docstring

Fold one finished instance's outcome into the running stats. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instance` | `Instance` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `self.is_solved_l.append` (lines: 28)
- `instance.has_soln` (lines: 28, 31)
- `self.ctgs.append` (lines: 29)
- `self.ctgs_bkup.append` (lines: 30)
- `self.path_costs.append` (lines: 32)
- `instance.path_cost` (lines: 32)
- `self.search_itrs_l.append` (lines: 33)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.ctgs`
- `self.ctgs_bkup`
- `self.is_solved_l`
- `self.path_costs`
- `self.search_itrs_l`

## Source

```python
    def update_perf(self, instance: Instance) -> None:
        """ Fold one finished instance's outcome into the running stats. """
        self.is_solved_l.append(instance.has_soln())
        self.ctgs.append(instance.root_node.heuristic)
        self.ctgs_bkup.append(instance.root_node.backup_val)
        if instance.has_soln():
            self.path_costs.append(instance.path_cost())
            self.search_itrs_l.append(instance.itr)
```
