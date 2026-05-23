---
id: "func:deepxube.domains.lightsout.LightsOut.to_np_2d_sg"
kind: "method"
name: "to_np_2d_sg"
qualified_name: "deepxube.domains.lightsout.LightsOut.to_np_2d_sg"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 119
line_end: 122
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
    call_sites: [121]
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [121]
  - target: null
    expr: "tiles_flat.reshape"
    call_sites: [122]
raises: []
reads_attrs:
  - "self.dim"
writes_attrs: []
---

# `deepxube.domains.lightsout.LightsOut.to_np_2d_sg`

**File:** [deepxube/domains/lightsout.py:119](../../../../deepxube/domains/lightsout.py#L119)
**Class:** `LightsOut`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np_2d_sg(self, states: List[LOState], goals: List[LOGoal]) -> List[NDArray]
```

## Docstring

:return: Shape ``(N, 1, dim, dim)`` tile arrays for 2-D NNet inputs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[LOState]` | — |
| `goals` | `List[LOGoal]` | — |

## Returns

`List[NDArray]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 121)

### Unresolved
- `np.stack([x.tiles for x in states], axis=0).astype` (lines: 121)
- `tiles_flat.reshape` (lines: 122)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.dim`

## Source

```python
    def to_np_2d_sg(self, states: List[LOState], goals: List[LOGoal]) -> List[NDArray]:
        """ :return: Shape ``(N, 1, dim, dim)`` tile arrays for 2-D NNet inputs. """
        tiles_flat: NDArray[np.uint8] = np.stack([x.tiles for x in states], axis=0).astype(np.uint8)
        return [tiles_flat.reshape((-1, 1, self.dim, self.dim))]
```
