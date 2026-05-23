---
id: "func:deepxube.domains.cube3._get_adj"
kind: "function"
name: "_get_adj"
qualified_name: "deepxube.domains.cube3._get_adj"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 58
line_end: 67
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters: []
returns: "Dict[int, NDArray[np.int_]]"
docstring_source: "present"
callees:
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [61, 62, 63, 64, 65, 66]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3._get_adj`

**File:** [deepxube/domains/cube3.py:58](../../../../deepxube/domains/cube3.py#L58)
**Visibility:** private
**Kind:** function

## Signature

```python
def _get_adj() -> Dict[int, NDArray[np.int_]]
```

## Docstring

:return: Dict mapping each face index to its 4 adjacent face indices in clockwise order. 

## Parameters

*(No parameters.)*

## Returns

`Dict[int, NDArray[np.int_]]`

## Calls

- `np.array` → `func:numpy.array` (lines: 61, 62, 63, 64, 65, 66)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _get_adj() -> Dict[int, NDArray[np.int_]]:
    """ :return: Dict mapping each face index to its 4 adjacent face indices in clockwise order. """
    # WHITE:0, YELLOW:1, BLUE:2, GREEN:3, ORANGE: 4, RED: 5
    return {0: np.array([2, 5, 3, 4]),
            1: np.array([2, 4, 3, 5]),
            2: np.array([0, 4, 1, 5]),
            3: np.array([0, 5, 1, 4]),
            4: np.array([0, 3, 1, 2]),
            5: np.array([0, 2, 1, 3])
            }
```
