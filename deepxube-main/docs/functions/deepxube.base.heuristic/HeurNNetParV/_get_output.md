---
id: "func:deepxube.base.heuristic.HeurNNetParV._get_output"
kind: "staticmethod"
name: "_get_output"
qualified_name: "deepxube.base.heuristic.HeurNNetParV._get_output"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 263
line_end: 268
class: "HeurNNetParV"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators:
  - "@staticmethod"
parameters:
  - name: "heurs"
    annotation: "NDArray[np.float64]"
    default: null
  - name: "update_num"
    annotation: "Optional[int]"
    default: null
returns: "List[float]"
docstring_source: "present"
callees:
  - target: "func:numpy.maximum"
    expr: "np.maximum"
    call_sites: [265]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [268]
  - target: null
    expr: "heurs.astype(np.float64).tolist"
    call_sites: [268]
  - target: null
    expr: "heurs.astype"
    call_sites: [268]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNetParV._get_output`

**File:** [deepxube/base/heuristic.py:263](../../../../deepxube/base/heuristic.py#L263)
**Class:** `HeurNNetParV`
**Visibility:** private
**Kind:** staticmethod
**Decorators:** `@staticmethod`

## Signature

```python
def _get_output(heurs: NDArray[np.float64], update_num: Optional[int]) -> List[float]
```

## Docstring

Clamp to non-negative; on ``update_num == 0`` return all zeros (warmup). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `heurs` | `NDArray[np.float64]` | — |
| `update_num` | `Optional[int]` | — |

## Returns

`List[float]`

## Calls

- `np.maximum` → `func:numpy.maximum` (lines: 265)
- `cast` → `func:typing.cast` (lines: 268)

### Unresolved
- `heurs.astype(np.float64).tolist` (lines: 268)
- `heurs.astype` (lines: 268)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_output(heurs: NDArray[np.float64], update_num: Optional[int]) -> List[float]:
        """ Clamp to non-negative; on ``update_num == 0`` return all zeros (warmup). """
        heurs = np.maximum(heurs[:, 0], 0)
        if (update_num is not None) and (update_num == 0):
            heurs = heurs * 0
        return cast(List[float], heurs.astype(np.float64).tolist())
```
