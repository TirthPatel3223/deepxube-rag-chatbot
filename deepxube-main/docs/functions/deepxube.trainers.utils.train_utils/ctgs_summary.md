---
id: "func:deepxube.trainers.utils.train_utils.ctgs_summary"
kind: "function"
name: "ctgs_summary"
qualified_name: "deepxube.trainers.utils.train_utils.ctgs_summary"
module: "deepxube.trainers.utils.train_utils"
file: "deepxube/trainers/utils/train_utils.py"
line_start: 19
line_end: 33
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "ctgs_l"
    annotation: "List[NDArray]"
    default: null
returns: "Tuple[float, float, float]"
docstring_source: "present"
callees:
  - target: null
    expr: "min"
    call_sites: [27]
  - target: null
    expr: "ctgs.min"
    call_sites: [27]
  - target: null
    expr: "max"
    call_sites: [28]
  - target: null
    expr: "ctgs.max"
    call_sites: [28]
  - target: null
    expr: "ctgs.sum"
    call_sites: [29]
  - target: null
    expr: "float"
    call_sites: [31]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.trainers.utils.train_utils.ctgs_summary`

**File:** [deepxube/trainers/utils/train_utils.py:19](../../../../deepxube/trainers/utils/train_utils.py#L19)
**Visibility:** public
**Kind:** function

## Signature

```python
def ctgs_summary(ctgs_l: List[NDArray]) -> Tuple[float, float, float]
```

## Docstring

:return: ``(mean, min, max)`` aggregated across all cost-to-go arrays in ``ctgs_l``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `ctgs_l` | `List[NDArray]` | — |

## Returns

`Tuple[float, float, float]`

## Calls

*(No resolved calls.)*

### Unresolved
- `min` (lines: 27)
- `ctgs.min` (lines: 27)
- `max` (lines: 28)
- `ctgs.max` (lines: 28)
- `ctgs.sum` (lines: 29)
- `float` (lines: 31)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def ctgs_summary(ctgs_l: List[NDArray]) -> Tuple[float, float, float]:
    """ :return: ``(mean, min, max)`` aggregated across all cost-to-go arrays in ``ctgs_l``. """
    ctgs_min: float = np.inf
    ctgs_max: float = -np.inf
    ctgs_mean: float = 0

    num_tot: int = 0
    for ctgs in ctgs_l:
        ctgs_min = min(ctgs.min(), ctgs_min)
        ctgs_max = max(ctgs.max(), ctgs_max)
        ctgs_mean += ctgs.sum()
        num_tot += ctgs.shape[0]
    ctgs_mean = ctgs_mean/float(num_tot)

    return ctgs_mean, ctgs_min, ctgs_max
```
