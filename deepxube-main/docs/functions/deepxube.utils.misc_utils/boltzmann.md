---
id: "func:deepxube.utils.misc_utils.boltzmann"
kind: "function"
name: "boltzmann"
qualified_name: "deepxube.utils.misc_utils.boltzmann"
module: "deepxube.utils.misc_utils"
file: "deepxube/utils/misc_utils.py"
line_start: 120
line_end: 137
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "vals"
    annotation: "List[float]"
    default: null
  - name: "temp"
    annotation: "float"
    default: null
returns: "List[float]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [130]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [133]
  - target: "func:numpy.exp"
    expr: "np.exp"
    call_sites: [134]
  - target: "func:numpy.max"
    expr: "np.max"
    call_sites: [134]
  - target: "func:numpy.sum"
    expr: "np.sum"
    call_sites: [135]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [137]
  - target: null
    expr: "probs_np.tolist"
    call_sites: [137]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.misc_utils.boltzmann`

**File:** [deepxube/utils/misc_utils.py:120](../../../../deepxube/utils/misc_utils.py#L120)
**Visibility:** public
**Kind:** function

## Signature

```python
def boltzmann(vals: List[float], temp: float) -> List[float]
```

## Docstring

Return the Boltzmann (softmax) distribution over ``vals`` at the given
temperature. Numerically stable via max-subtraction.

:param vals: Scores. If length is 1, returns ``[1.0]`` without
    computation.
:param temp: Temperature; smaller values concentrate probability on the
    maxima, larger values flatten the distribution.
:return: List of probabilities summing to 1.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `vals` | `List[float]` | — |
| `temp` | `float` | — |

## Returns

`List[float]`

## Calls

- `np.array` → `func:numpy.array` (lines: 133)
- `np.exp` → `func:numpy.exp` (lines: 134)
- `np.max` → `func:numpy.max` (lines: 134)
- `np.sum` → `func:numpy.sum` (lines: 135)
- `cast` → `func:typing.cast` (lines: 137)

### Unresolved
- `len` (lines: 130)
- `probs_np.tolist` (lines: 137)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def boltzmann(vals: List[float], temp: float) -> List[float]:
    """ Return the Boltzmann (softmax) distribution over ``vals`` at the given
    temperature. Numerically stable via max-subtraction.

    :param vals: Scores. If length is 1, returns ``[1.0]`` without
        computation.
    :param temp: Temperature; smaller values concentrate probability on the
        maxima, larger values flatten the distribution.
    :return: List of probabilities summing to 1.
    """
    if len(vals) == 1:
        return [1.0]
    else:
        vals_np: NDArray[np.float64] = np.array(vals)
        exp_vals_np: NDArray[np.float64] = np.exp((1.0 / temp) * (vals_np - np.max(vals_np)))
        probs_np: NDArray[np.float64] = exp_vals_np / np.sum(exp_vals_np)

        return cast(List[float], probs_np.tolist())
```
