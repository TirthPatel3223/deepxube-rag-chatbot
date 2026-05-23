---
id: "func:deepxube.domains.cube3.Cube3.to_np_flat_sga"
kind: "method"
name: "to_np_flat_sga"
qualified_name: "deepxube.domains.cube3.Cube3.to_np_flat_sga"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 569
line_end: 572
class: "Cube3"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states"
    annotation: "List[Cube3State]"
    default: null
  - name: "goals"
    annotation: "List[Cube3Goal]"
    default: null
  - name: "actions"
    annotation: "List[Cube3Action]"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.cube3.Cube3.to_np_flat_sg"
    expr: "self.to_np_flat_sg"
    call_sites: [572]
  - target: "func:numpy.expand_dims"
    expr: "np.expand_dims"
    call_sites: [572]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [572]
  - target: "func:deepxube.domains.cube3.Cube3.actions_to_indices"
    expr: "self.actions_to_indices"
    call_sites: [572]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3.to_np_flat_sga`

**File:** [deepxube/domains/cube3.py:569](../../../../deepxube/domains/cube3.py#L569)
**Class:** `Cube3`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np_flat_sga(self, states: List[Cube3State], goals: List[Cube3Goal], actions: List[Cube3Action]) -> List[NDArray]
```

## Docstring

:return: Flat state arrays extended with action indices. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[Cube3State]` | — |
| `goals` | `List[Cube3Goal]` | — |
| `actions` | `List[Cube3Action]` | — |

## Returns

`List[NDArray]`

## Calls

- `self.to_np_flat_sg` → `func:deepxube.domains.cube3.Cube3.to_np_flat_sg` (lines: 572)
- `np.expand_dims` → `func:numpy.expand_dims` (lines: 572)
- `np.array` → `func:numpy.array` (lines: 572)
- `self.actions_to_indices` → `func:deepxube.domains.cube3.Cube3.actions_to_indices` (lines: 572)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_np_flat_sga(self, states: List[Cube3State], goals: List[Cube3Goal],
                       actions: List[Cube3Action]) -> List[NDArray]:
        """ :return: Flat state arrays extended with action indices. """
        return self.to_np_flat_sg(states, goals) + [np.expand_dims(np.array(self.actions_to_indices(actions)), 1)]
```
