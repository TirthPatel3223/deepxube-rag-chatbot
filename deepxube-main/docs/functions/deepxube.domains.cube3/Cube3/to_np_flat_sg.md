---
id: "func:deepxube.domains.cube3.Cube3.to_np_flat_sg"
kind: "method"
name: "to_np_flat_sg"
qualified_name: "deepxube.domains.cube3.Cube3.to_np_flat_sg"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 565
line_end: 567
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
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "np.stack([x.colors for x in states], axis=0).astype"
    call_sites: [567]
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [567]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3.to_np_flat_sg`

**File:** [deepxube/domains/cube3.py:565](../../../../deepxube/domains/cube3.py#L565)
**Class:** `Cube3`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np_flat_sg(self, states: List[Cube3State], goals: List[Cube3Goal]) -> List[NDArray]
```

## Docstring

:return: Stacked uint8 colour arrays (state only; goal is always solved). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[Cube3State]` | — |
| `goals` | `List[Cube3Goal]` | — |

## Returns

`List[NDArray]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 567)

### Unresolved
- `np.stack([x.colors for x in states], axis=0).astype` (lines: 567)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def to_np_flat_sg(self, states: List[Cube3State], goals: List[Cube3Goal]) -> List[NDArray]:
        """ :return: Stacked uint8 colour arrays (state only; goal is always solved). """
        return [np.stack([x.colors for x in states], axis=0).astype(np.uint8)]
```
