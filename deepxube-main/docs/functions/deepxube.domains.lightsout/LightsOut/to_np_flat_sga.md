---
id: "func:deepxube.domains.lightsout.LightsOut.to_np_flat_sga"
kind: "method"
name: "to_np_flat_sga"
qualified_name: "deepxube.domains.lightsout.LightsOut.to_np_flat_sga"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 112
line_end: 114
class: "LightsOut"
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
    annotation: "List[LOState]"
    default: null
  - name: "goals"
    annotation: "List[LOGoal]"
    default: null
  - name: "actions"
    annotation: "List[LOAction]"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.lightsout.LightsOut.to_np_flat_sg"
    expr: "self.to_np_flat_sg"
    call_sites: [114]
  - target: "func:numpy.expand_dims"
    expr: "np.expand_dims"
    call_sites: [114]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [114]
  - target: "func:deepxube.domains.lightsout.LightsOut.actions_to_indices"
    expr: "self.actions_to_indices"
    call_sites: [114]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.lightsout.LightsOut.to_np_flat_sga`

**File:** [deepxube/domains/lightsout.py:112](../../../../deepxube/domains/lightsout.py#L112)
**Class:** `LightsOut`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np_flat_sga(self, states: List[LOState], goals: List[LOGoal], actions: List[LOAction]) -> List[NDArray]
```

## Docstring

:return: Flat state arrays extended with action indices. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[LOState]` | — |
| `goals` | `List[LOGoal]` | — |
| `actions` | `List[LOAction]` | — |

## Returns

`List[NDArray]`

## Calls

- `self.to_np_flat_sg` → `func:deepxube.domains.lightsout.LightsOut.to_np_flat_sg` (lines: 114)
- `np.expand_dims` → `func:numpy.expand_dims` (lines: 114)
- `np.array` → `func:numpy.array` (lines: 114)
- `self.actions_to_indices` → `func:deepxube.domains.lightsout.LightsOut.actions_to_indices` (lines: 114)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_np_flat_sga(self, states: List[LOState], goals: List[LOGoal], actions: List[LOAction]) -> List[NDArray]:
        """ :return: Flat state arrays extended with action indices. """
        return self.to_np_flat_sg(states, goals) + [np.expand_dims(np.array(self.actions_to_indices(actions)), 1)]
```
