---
id: "func:deepxube.base.updater.UpdateRL._make_instances"
kind: "method"
name: "_make_instances"
qualified_name: "deepxube.base.updater.UpdateRL._make_instances"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 687
line_end: 694
class: "UpdateRL"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "pathfind"
    annotation: "P"
    default: null
  - name: "steps_gen"
    annotation: "List[int]"
    default: null
  - name: "inst_infos"
    annotation: "List[Any]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[Inst]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.timing_utils.Times"
    expr: "Times"
    call_sites: [690]
  - target: null
    expr: "self.domain.sample_problem_instances"
    call_sites: [691]
  - target: null
    expr: "times.add_times"
    call_sites: [692]
  - target: null
    expr: "pathfind.make_instances"
    call_sites: [694]
raises: []
reads_attrs:
  - "self.domain"
writes_attrs: []
---

# `deepxube.base.updater.UpdateRL._make_instances`

**File:** [deepxube/base/updater.py:687](../../../../deepxube/base/updater.py#L687)
**Class:** `UpdateRL`
**Visibility:** private
**Kind:** method

## Signature

```python
def _make_instances(self, pathfind: P, steps_gen: List[int], inst_infos: List[Any], times: Times) -> List[Inst]
```

## Docstring

Sample start states and goals from the domain, then hand them to the pathfinder. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `pathfind` | `P` | — |
| `steps_gen` | `List[int]` | — |
| `inst_infos` | `List[Any]` | — |
| `times` | `Times` | — |

## Returns

`List[Inst]`

## Calls

- `Times` → `func:deepxube.utils.timing_utils.Times` (lines: 690)

### Unresolved
- `self.domain.sample_problem_instances` (lines: 691)
- `times.add_times` (lines: 692)
- `pathfind.make_instances` (lines: 694)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`

## Source

```python
    def _make_instances(self, pathfind: P, steps_gen: List[int], inst_infos: List[Any], times: Times) -> List[Inst]:
        """ Sample start states and goals from the domain, then hand them to the pathfinder. """
        # get states/goals
        times_states: Times = Times()
        states_gen, goals_gen = self.domain.sample_problem_instances(steps_gen, times=times_states)
        times.add_times(times_states, ["get_states"])

        return pathfind.make_instances(states_gen, goals_gen, inst_infos=inst_infos, compute_root_vals=False)
```
