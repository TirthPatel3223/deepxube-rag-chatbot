---
id: "func:deepxube.domains.cube3.InteractiveCube.set_rot"
kind: "method"
name: "set_rot"
qualified_name: "deepxube.domains.cube3.InteractiveCube.set_rot"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 344
line_end: 351
class: "InteractiveCube"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "rot"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "Quaternion.from_v_theta"
    call_sites: [347, 349]
  - target: "func:numpy.asarray"
    expr: "np.asarray"
    call_sites: [347, 349]
  - target: "func:deepxube.domains.cube3.InteractiveCube._draw_cube"
    expr: "self._draw_cube"
    call_sites: [351]
raises: []
reads_attrs:
  - "self._current_rot"
writes_attrs:
  - "self._current_rot"
---

# `deepxube.domains.cube3.InteractiveCube.set_rot`

**File:** [deepxube/domains/cube3.py:344](../../../../deepxube/domains/cube3.py#L344)
**Class:** `InteractiveCube`
**Visibility:** public
**Kind:** method

## Signature

```python
def set_rot(self, rot: int) -> None
```

## Docstring

Set a preset camera orientation (``rot=0`` or ``rot=1``) and redraw. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `rot` | `int` | — |

## Returns

`None`

## Calls

- `np.asarray` → `func:numpy.asarray` (lines: 347, 349)
- `self._draw_cube` → `func:deepxube.domains.cube3.InteractiveCube._draw_cube` (lines: 351)

### Unresolved
- `Quaternion.from_v_theta` (lines: 347, 349)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self._current_rot`

**Reads:**
- `self._current_rot`

## Source

```python
    def set_rot(self, rot: int) -> None:
        """ Set a preset camera orientation (``rot=0`` or ``rot=1``) and redraw. """
        if rot == 0:
            self._current_rot = Quaternion.from_v_theta(np.asarray((-0.53180525, 0.83020462, 0.16716299)), np.asarray(0.95063829))
        elif rot == 1:
            self._current_rot = Quaternion.from_v_theta(np.asarray((0.9248325, 0.14011997, -0.35362584)), np.asarray(2.49351394))

        self._draw_cube()
```
