---
id: "func:deepxube.domains.cube3.Quaternion.as_v_theta"
kind: "method"
name: "as_v_theta"
qualified_name: "deepxube.domains.cube3.Quaternion.as_v_theta"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 138
line_end: 154
class: "Quaternion"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "Tuple[NDArray, NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "self.x.reshape"
    call_sites: [140]
  - target: "func:numpy.sqrt"
    expr: "np.sqrt"
    call_sites: [143, 148]
  - target: null
    expr: "(x ** 2).sum"
    call_sites: [143]
  - target: "func:numpy.arccos"
    expr: "np.arccos"
    call_sites: [144]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [147]
  - target: "func:numpy.sum"
    expr: "np.sum"
    call_sites: [148]
  - target: null
    expr: "v.T.reshape"
    call_sites: [151]
  - target: null
    expr: "theta.reshape"
    call_sites: [152]
raises: []
reads_attrs:
  - "self.x"
writes_attrs: []
---

# `deepxube.domains.cube3.Quaternion.as_v_theta`

**File:** [deepxube/domains/cube3.py:138](../../../../deepxube/domains/cube3.py#L138)
**Class:** `Quaternion`
**Visibility:** public
**Kind:** method

## Signature

```python
def as_v_theta(self) -> Tuple[NDArray, NDArray]
```

## Docstring

Return the v, theta equivalent of the (normalized) quaternion

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`Tuple[NDArray, NDArray]`

## Calls

- `np.sqrt` → `func:numpy.sqrt` (lines: 143, 148)
- `np.arccos` → `func:numpy.arccos` (lines: 144)
- `np.array` → `func:numpy.array` (lines: 147)
- `np.sum` → `func:numpy.sum` (lines: 148)

### Unresolved
- `self.x.reshape` (lines: 140)
- `(x ** 2).sum` (lines: 143)
- `v.T.reshape` (lines: 151)
- `theta.reshape` (lines: 152)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.x`

## Source

```python
    def as_v_theta(self) -> Tuple[NDArray, NDArray]:
        """Return the v, theta equivalent of the (normalized) quaternion"""
        x = self.x.reshape((-1, 4)).T

        # compute theta
        norm = np.sqrt((x ** 2).sum(0))
        theta = 2 * np.arccos(x[0] / norm)

        # compute the unit vector
        v = np.array(x[1:], order='F', copy=True)
        v /= np.sqrt(np.sum(v ** 2, 0))

        # reshape the results
        v = v.T.reshape(self.x.shape[:-1] + (3,))
        theta = theta.reshape(self.x.shape[:-1])

        return v, theta
```
