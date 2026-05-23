---
id: "func:deepxube.domains.cube3.Quaternion.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.domains.cube3.Quaternion.__init__"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 108
line_end: 110
class: "Quaternion"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "x"
    annotation: "NDArray"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: "func:numpy.asarray"
    expr: "np.asarray"
    call_sites: [110]
raises: []
reads_attrs:
  - "self.x"
writes_attrs:
  - "self.x"
---

# `deepxube.domains.cube3.Quaternion.__init__`

**File:** [deepxube/domains/cube3.py:108](../../../../deepxube/domains/cube3.py#L108)
**Class:** `Quaternion`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, x: NDArray)
```

## Docstring

Store quaternion coefficients ``(w, xi, yj, zk)`` as a numpy array. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `x` | `NDArray` | — |

## Returns

*(Not annotated.)*

## Calls

- `np.asarray` → `func:numpy.asarray` (lines: 110)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.x`

**Reads:**
- `self.x`

## Source

```python
    def __init__(self, x: NDArray):
        """ Store quaternion coefficients ``(w, xi, yj, zk)`` as a numpy array. """
        self.x = np.asarray(x, dtype=float)
```
