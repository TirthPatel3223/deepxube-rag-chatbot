---
id: "func:deepxube.base.updater.Update._update_perf"
kind: "staticmethod"
name: "_update_perf"
qualified_name: "deepxube.base.updater.Update._update_perf"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 128
line_end: 134
class: "Update"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators:
  - "@staticmethod"
parameters:
  - name: "insts"
    annotation: "List[Inst]"
    default: null
  - name: "step_to_pathperf"
    annotation: "Dict[int, PathFindPerf]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "int"
    call_sites: [131]
  - target: null
    expr: "step_to_pathperf.keys"
    call_sites: [132]
  - target: "func:deepxube.pathfinding.utils.performance.PathFindPerf"
    expr: "PathFindPerf"
    call_sites: [133]
  - target: null
    expr: "step_to_pathperf[step_num_inst].update_perf"
    call_sites: [134]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.Update._update_perf`

**File:** [deepxube/base/updater.py:128](../../../../deepxube/base/updater.py#L128)
**Class:** `Update`
**Visibility:** private
**Kind:** staticmethod
**Decorators:** `@staticmethod`

## Signature

```python
def _update_perf(insts: List[Inst], step_to_pathperf: Dict[int, PathFindPerf]) -> None
```

## Docstring

Per-step performance bookkeeping: fold each instance's stats into the map keyed by its step count. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `insts` | `List[Inst]` | — |
| `step_to_pathperf` | `Dict[int, PathFindPerf]` | — |

## Returns

`None`

## Calls

- `PathFindPerf` → `func:deepxube.pathfinding.utils.performance.PathFindPerf` (lines: 133)

### Unresolved
- `int` (lines: 131)
- `step_to_pathperf.keys` (lines: 132)
- `step_to_pathperf[step_num_inst].update_perf` (lines: 134)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _update_perf(insts: List[Inst], step_to_pathperf: Dict[int, PathFindPerf]) -> None:
        """ Per-step performance bookkeeping: fold each instance's stats into the map keyed by its step count. """
        for inst in insts:
            step_num_inst: int = int(inst.inst_info[0])
            if step_num_inst not in step_to_pathperf.keys():
                step_to_pathperf[step_num_inst] = PathFindPerf()
            step_to_pathperf[step_num_inst].update_perf(inst)
```
