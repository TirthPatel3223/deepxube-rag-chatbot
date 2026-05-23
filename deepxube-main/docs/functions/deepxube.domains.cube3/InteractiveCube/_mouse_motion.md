---
id: "func:deepxube.domains.cube3.InteractiveCube._mouse_motion"
kind: "method"
name: "_mouse_motion"
qualified_name: "deepxube.domains.cube3.InteractiveCube._mouse_motion"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 477
line_end: 507
class: "InteractiveCube"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "event"
    annotation: null
    default: null
  - name: "event_x"
    annotation: null
    default: "None"
  - name: "event_y"
    annotation: null
    default: "None"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "Quaternion.from_v_theta"
    call_sites: [494, 495]
  - target: "func:deepxube.domains.cube3.InteractiveCube.rotate"
    expr: "self.rotate"
    call_sites: [496]
  - target: "func:deepxube.domains.cube3.InteractiveCube._draw_cube"
    expr: "self._draw_cube"
    call_sites: [498]
  - target: "func:deepxube.domains.cube3.InteractiveCube.get_xlim"
    expr: "self.get_xlim"
    call_sites: [502]
  - target: "func:deepxube.domains.cube3.InteractiveCube.get_ylim"
    expr: "self.get_ylim"
    call_sites: [503]
  - target: "func:deepxube.domains.cube3.InteractiveCube.set_xlim"
    expr: "self.set_xlim"
    call_sites: [504]
  - target: "func:deepxube.domains.cube3.InteractiveCube.set_ylim"
    expr: "self.set_ylim"
    call_sites: [505]
  - target: null
    expr: "self.figure.canvas.draw"
    call_sites: [507]
raises: []
reads_attrs:
  - "self._ax_LR"
  - "self._ax_LR_alt"
  - "self._ax_UD"
  - "self._button1"
  - "self._button2"
  - "self._event_xy"
  - "self._step_LR"
  - "self._step_UD"
  - "self._tab"
  - "self.figure"
writes_attrs:
  - "self._event_xy"
---

# `deepxube.domains.cube3.InteractiveCube._mouse_motion`

**File:** [deepxube/domains/cube3.py:477](../../../../deepxube/domains/cube3.py#L477)
**Class:** `InteractiveCube`
**Visibility:** private
**Kind:** method

## Signature

```python
def _mouse_motion(self, event, event_x = None, event_y = None)
```

## Docstring

Rotate the view (button 1) or zoom (button 2) in response to mouse drag. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `event` | — | — |
| `event_x` | — | `None` |
| `event_y` | — | `None` |

## Returns

*(Not annotated.)*

## Calls

- `self.rotate` → `func:deepxube.domains.cube3.InteractiveCube.rotate` (lines: 496)
- `self._draw_cube` → `func:deepxube.domains.cube3.InteractiveCube._draw_cube` (lines: 498)
- `self.get_xlim` → `func:deepxube.domains.cube3.InteractiveCube.get_xlim` (lines: 502)
- `self.get_ylim` → `func:deepxube.domains.cube3.InteractiveCube.get_ylim` (lines: 503)
- `self.set_xlim` → `func:deepxube.domains.cube3.InteractiveCube.set_xlim` (lines: 504)
- `self.set_ylim` → `func:deepxube.domains.cube3.InteractiveCube.set_ylim` (lines: 505)

### Unresolved
- `Quaternion.from_v_theta` (lines: 494, 495)
- `self.figure.canvas.draw` (lines: 507)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self._event_xy`

**Reads:**
- `self._ax_LR`
- `self._ax_LR_alt`
- `self._ax_UD`
- `self._button1`
- `self._button2`
- `self._event_xy`
- `self._step_LR`
- `self._step_UD`
- `self._tab`
- `self.figure`

## Source

```python
    def _mouse_motion(self, event, event_x=None, event_y=None):  # type: ignore
        """ Rotate the view (button 1) or zoom (button 2) in response to mouse drag. """
        if self._button1 or self._button2:
            if event_x is not None and event_y is not None:
                dx = event_x - self._event_xy[0]
                dy = event_y - self._event_xy[1]
                self._event_xy = (event_x, event_y)
            else:
                dx = event.x - self._event_xy[0]
                dy = event.y - self._event_xy[1]
                self._event_xy = (event.x, event.y)

            if self._button1:
                if self._tab:
                    ax_lr = self._ax_LR_alt
                else:
                    ax_lr = self._ax_LR
                rot1 = Quaternion.from_v_theta(self._ax_UD, self._step_UD * dy)
                rot2 = Quaternion.from_v_theta(ax_lr, self._step_LR * dx)
                self.rotate(rot1 * rot2)

                self._draw_cube()

            if self._button2:
                factor = 1 - 0.003 * (dx + dy)
                xlim = self.get_xlim()
                ylim = self.get_ylim()
                self.set_xlim(factor * xlim[0], factor * xlim[1])
                self.set_ylim(factor * ylim[0], factor * ylim[1])

                self.figure.canvas.draw()
```
