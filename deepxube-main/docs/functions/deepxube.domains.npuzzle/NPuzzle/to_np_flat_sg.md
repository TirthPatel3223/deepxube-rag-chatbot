---
id: "func:deepxube.domains.npuzzle.NPuzzle.to_np_flat_sg"
kind: "method"
name: "to_np_flat_sg"
qualified_name: "deepxube.domains.npuzzle.NPuzzle.to_np_flat_sg"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 187
line_end: 189
class: "NPuzzle"
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
    annotation: "List[NPState]"
    default: null
  - name: "goals"
    annotation: "List[NPGoal]"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "np.stack([x.tiles for x in states], axis=0).astype"
    call_sites: [189]
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [189]
raises: []
reads_attrs:
  - "self.dtype"
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle.to_np_flat_sg`

**File:** [deepxube/domains/npuzzle.py:187](../../../../deepxube/domains/npuzzle.py#L187)
**Class:** `NPuzzle`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np_flat_sg(self, states: List[NPState], goals: List[NPGoal]) -> List[NDArray]
```

## Docstring

:return: Stacked flat tile arrays. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[NPState]` | — |
| `goals` | `List[NPGoal]` | — |

## Returns

`List[NDArray]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 189)

### Unresolved
- `np.stack([x.tiles for x in states], axis=0).astype` (lines: 189)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.dtype`

## Source

```python
    def to_np_flat_sg(self, states: List[NPState], goals: List[NPGoal]) -> List[NDArray]:
        """ :return: Stacked flat tile arrays. """
        return [np.stack([x.tiles for x in states], axis=0).astype(self.dtype)]
```
