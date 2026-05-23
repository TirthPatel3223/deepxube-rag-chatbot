---
id: "func:deepxube._solve._get_mean"
kind: "function"
name: "_get_mean"
qualified_name: "deepxube._solve._get_mean"
module: "deepxube._solve"
file: "deepxube/_solve.py"
line_start: 219
line_end: 226
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "results"
    annotation: "Dict[str, Any]"
    default: null
  - name: "key"
    annotation: "str"
    default: null
returns: "float"
docstring_source: "present"
callees:
  - target: null
    expr: "zip"
    call_sites: [221, 225]
  - target: null
    expr: "len"
    call_sites: [222]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [225]
  - target: null
    expr: "float"
    call_sites: [226]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._solve._get_mean`

**File:** [deepxube/_solve.py:219](../../../../deepxube/_solve.py#L219)
**Visibility:** private
**Kind:** function

## Signature

```python
def _get_mean(results: Dict[str, Any], key: str) -> float
```

## Docstring

:return: Mean of ``results[key]`` restricted to solved instances, or 0 if none are solved. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `results` | `Dict[str, Any]` | — |
| `key` | `str` | — |

## Returns

`float`

## Calls

- `np.mean` → `func:numpy.mean` (lines: 225)

### Unresolved
- `zip` (lines: 221, 225)
- `len` (lines: 222)
- `float` (lines: 226)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _get_mean(results: Dict[str, Any], key: str) -> float:
    """ :return: Mean of ``results[key]`` restricted to solved instances, or 0 if none are solved. """
    vals: List = [x for x, solved in zip(results[key], results["solved"]) if solved]
    if len(vals) == 0:
        return 0
    else:
        mean_val = np.mean([x for x, solved in zip(results[key], results["solved"]) if solved])
        return float(mean_val)
```
