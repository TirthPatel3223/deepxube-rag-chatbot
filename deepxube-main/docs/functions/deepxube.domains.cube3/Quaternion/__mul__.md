---
id: "func:deepxube.domains.cube3.Quaternion.__mul__"
kind: "method"
name: "__mul__"
qualified_name: "deepxube.domains.cube3.Quaternion.__mul__"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 115
line_end: 136
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
  - name: "other"
    annotation: "'Quaternion'"
    default: null
returns: "'Quaternion'"
docstring_source: "present"
callees:
  - target: null
    expr: "self.x.reshape"
    call_sites: [119]
  - target: null
    expr: "other.x.reshape"
    call_sites: [120]
  - target: null
    expr: "prod.reshape((-1, 4, 4)).transpose"
    call_sites: [124]
  - target: null
    expr: "prod.reshape"
    call_sites: [124]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [126]
  - target: "func:deepxube.domains.cube3.Quaternion.__class__"
    expr: "self.__class__"
    call_sites: [136]
  - target: null
    expr: "ret.reshape"
    call_sites: [136]
raises: []
reads_attrs:
  - "self.x"
writes_attrs: []
---

# `deepxube.domains.cube3.Quaternion.__mul__`

**File:** [deepxube/domains/cube3.py:115](../../../../deepxube/domains/cube3.py#L115)
**Class:** `Quaternion`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __mul__(self, other: 'Quaternion') -> 'Quaternion'
```

## Docstring

:return: Hamilton product of two quaternions. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `other` | `'Quaternion'` | — |

## Returns

`'Quaternion'`

## Calls

- `np.array` → `func:numpy.array` (lines: 126)
- `self.__class__` → `func:deepxube.domains.cube3.Quaternion.__class__` (lines: 136)

### Unresolved
- `self.x.reshape` (lines: 119)
- `other.x.reshape` (lines: 120)
- `prod.reshape((-1, 4, 4)).transpose` (lines: 124)
- `prod.reshape` (lines: 124)
- `ret.reshape` (lines: 136)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.x`

## Source

```python
    def __mul__(self, other: 'Quaternion') -> 'Quaternion':
        """ :return: Hamilton product of two quaternions. """
        # multiplication of two quaternions.
        # we don't implement multiplication by a scalar
        sxr = self.x.reshape(self.x.shape[:-1] + (4, 1))
        oxr = other.x.reshape(other.x.shape[:-1] + (1, 4))

        prod = sxr * oxr
        return_shape = prod.shape[:-1]
        prod = prod.reshape((-1, 4, 4)).transpose((1, 2, 0))

        ret = np.array([(prod[0, 0] - prod[1, 1]
                         - prod[2, 2] - prod[3, 3]),
                        (prod[0, 1] + prod[1, 0]
                         + prod[2, 3] - prod[3, 2]),
                        (prod[0, 2] - prod[1, 3]
                         + prod[2, 0] + prod[3, 1]),
                        (prod[0, 3] + prod[1, 2]
                         - prod[2, 1] + prod[3, 0])],
                       dtype=float,
                       order='F').T
        return self.__class__(ret.reshape(return_shape))
```
