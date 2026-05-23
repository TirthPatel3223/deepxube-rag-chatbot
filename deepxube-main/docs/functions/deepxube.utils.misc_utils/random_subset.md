---
id: "func:deepxube.utils.misc_utils.random_subset"
kind: "function"
name: "random_subset"
qualified_name: "deepxube.utils.misc_utils.random_subset"
module: "deepxube.utils.misc_utils"
file: "deepxube/utils/misc_utils.py"
line_start: 105
line_end: 117
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "set_orig"
    annotation: "Union[Set[Any], frozenset[Any]]"
    default: null
  - name: "keep_prob"
    annotation: "bool"
    default: null
returns: "Set[Any]"
docstring_source: "present"
callees:
  - target: null
    expr: "np.random.rand"
    call_sites: [113]
  - target: null
    expr: "len"
    call_sites: [113]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [114]
  - target: null
    expr: "set"
    call_sites: [115]
  - target: null
    expr: "zip"
    call_sites: [115]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.misc_utils.random_subset`

**File:** [deepxube/utils/misc_utils.py:105](../../../../deepxube/utils/misc_utils.py#L105)
**Visibility:** public
**Kind:** function

## Signature

```python
def random_subset(set_orig: Union[Set[Any], frozenset[Any]], keep_prob: bool) -> Set[Any]
```

## Docstring

Return a Bernoulli-sampled subset of ``set_orig`` where each element
is kept independently with probability ``keep_prob``.

:param set_orig: Input set (or frozenset).
:param keep_prob: Per-element keep probability in [0, 1].
:return: A new set containing the retained elements.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `set_orig` | `Union[Set[Any], frozenset[Any]]` | — |
| `keep_prob` | `bool` | — |

## Returns

`Set[Any]`

## Calls

- `np.array` → `func:numpy.array` (lines: 114)

### Unresolved
- `np.random.rand` (lines: 113)
- `len` (lines: 113)
- `set` (lines: 115)
- `zip` (lines: 115)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def random_subset(set_orig: Union[Set[Any], frozenset[Any]], keep_prob: bool) -> Set[Any]:
    """ Return a Bernoulli-sampled subset of ``set_orig`` where each element
    is kept independently with probability ``keep_prob``.

    :param set_orig: Input set (or frozenset).
    :param keep_prob: Per-element keep probability in [0, 1].
    :return: A new set containing the retained elements.
    """
    rand_vals: NDArray[Any] = np.random.rand(len(set_orig))
    keep_arr: NDArray[np.bool_] = np.array(rand_vals < keep_prob)
    rand_subset: Set[Any] = set(elem for elem, keep_i in zip(set_orig, keep_arr) if keep_i)

    return rand_subset
```
