---
id: "func:deepxube.domains.lightsout.LightsOut.to_np_flat_sg"
kind: "method"
name: "to_np_flat_sg"
qualified_name: "deepxube.domains.lightsout.LightsOut.to_np_flat_sg"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 108
line_end: 110
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
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "np.stack([x.tiles for x in states], axis=0).astype"
    call_sites: [110]
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [110]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.lightsout.LightsOut.to_np_flat_sg`

**File:** [deepxube/domains/lightsout.py:108](../../../../deepxube/domains/lightsout.py#L108)
**Class:** `LightsOut`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np_flat_sg(self, states: List[LOState], goals: List[LOGoal]) -> List[NDArray]
```

## Docstring

:return: Stacked uint8 tile arrays (state only; goal is always all-zeros). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[LOState]` | — |
| `goals` | `List[LOGoal]` | — |

## Returns

`List[NDArray]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 110)

### Unresolved
- `np.stack([x.tiles for x in states], axis=0).astype` (lines: 110)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_np_flat_sg(self, states: List[LOState], goals: List[LOGoal]) -> List[NDArray]:
        """ :return: Stacked uint8 tile arrays (state only; goal is always all-zeros). """
        return [np.stack([x.tiles for x in states], axis=0).astype(np.uint8)]
```
