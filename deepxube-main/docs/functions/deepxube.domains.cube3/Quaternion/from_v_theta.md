---
id: "func:deepxube.domains.cube3.Quaternion.from_v_theta"
kind: "classmethod"
name: "from_v_theta"
qualified_name: "deepxube.domains.cube3.Quaternion.from_v_theta"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 77
line_end: 106
class: "Quaternion"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators:
  - "@classmethod"
parameters:
  - name: "cls"
    annotation: null
    default: null
  - name: "v"
    annotation: null
    default: null
  - name: "theta"
    annotation: null
    default: null
returns: "'Quaternion'"
docstring_source: "present"
callees:
  - target: "func:numpy.asarray"
    expr: "np.asarray"
    call_sites: [93, 94]
  - target: "func:numpy.sin"
    expr: "np.sin"
    call_sites: [95]
  - target: "func:numpy.cos"
    expr: "np.cos"
    call_sites: [96]
  - target: "func:numpy.sqrt"
    expr: "np.sqrt"
    call_sites: [98]
  - target: "func:numpy.sum"
    expr: "np.sum"
    call_sites: [98]
  - target: null
    expr: "np.ones(x_shape).reshape"
    call_sites: [101]
  - target: "func:numpy.ones"
    expr: "np.ones"
    call_sites: [101]
  - target: null
    expr: "c.ravel"
    call_sites: [102]
  - target: null
    expr: "v.reshape"
    call_sites: [103]
  - target: null
    expr: "x.reshape"
    call_sites: [104]
  - target: "func:deepxube.domains.cube3.cls"
    expr: "cls"
    call_sites: [106]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3.Quaternion.from_v_theta`

**File:** [deepxube/domains/cube3.py:77](../../../../deepxube/domains/cube3.py#L77)
**Class:** `Quaternion`
**Visibility:** public
**Kind:** classmethod
**Decorators:** `@classmethod`

## Signature

```python
def from_v_theta(cls, v, theta) -> 'Quaternion'
```

## Docstring

Construct quaternions from unit vectors v and rotation angles theta

Parameters
----------
v : array_like
    array of vectors, last dimension 3. Vectors will be normalized.
theta : array_like
    array of rotation angles in radians, shape = v.shape[:-1].

Returns
-------
q : quaternion object
    quaternion representing the rotations

## Parameters

| Name | Type | Default |
|------|------|---------|
| `cls` | — | — |
| `v` | — | — |
| `theta` | — | — |

## Returns

`'Quaternion'`

## Calls

- `np.asarray` → `func:numpy.asarray` (lines: 93, 94)
- `np.sin` → `func:numpy.sin` (lines: 95)
- `np.cos` → `func:numpy.cos` (lines: 96)
- `np.sqrt` → `func:numpy.sqrt` (lines: 98)
- `np.sum` → `func:numpy.sum` (lines: 98)
- `np.ones` → `func:numpy.ones` (lines: 101)
- `cls` → `func:deepxube.domains.cube3.cls` (lines: 106)

### Unresolved
- `np.ones(x_shape).reshape` (lines: 101)
- `c.ravel` (lines: 102)
- `v.reshape` (lines: 103)
- `x.reshape` (lines: 104)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def from_v_theta(cls, v, theta) -> 'Quaternion':  # type: ignore
        """
        Construct quaternions from unit vectors v and rotation angles theta

        Parameters
        ----------
        v : array_like
            array of vectors, last dimension 3. Vectors will be normalized.
        theta : array_like
            array of rotation angles in radians, shape = v.shape[:-1].

        Returns
        -------
        q : quaternion object
            quaternion representing the rotations
        """
        theta = np.asarray(theta)
        v = np.asarray(v)
        s = np.sin(0.5 * theta)
        c = np.cos(0.5 * theta)

        v = v * s / np.sqrt(np.sum(v * v, -1))
        x_shape = v.shape[:-1] + (4,)

        x: NDArray = np.ones(x_shape).reshape(-1, 4)
        x[:, 0] = c.ravel()
        x[:, 1:] = v.reshape(-1, 3)
        x = x.reshape(x_shape)

        return cls(x)
```
