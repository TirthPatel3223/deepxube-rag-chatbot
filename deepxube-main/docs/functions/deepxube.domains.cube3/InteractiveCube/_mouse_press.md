---
id: "func:deepxube.domains.cube3.InteractiveCube._mouse_press"
kind: "method"
name: "_mouse_press"
qualified_name: "deepxube.domains.cube3.InteractiveCube._mouse_press"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 457
line_end: 467
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
callees: []
raises: []
reads_attrs:
  - "self._button1"
  - "self._button2"
  - "self._event_xy"
writes_attrs:
  - "self._button1"
  - "self._button2"
  - "self._event_xy"
---

# `deepxube.domains.cube3.InteractiveCube._mouse_press`

**File:** [deepxube/domains/cube3.py:457](../../../../deepxube/domains/cube3.py#L457)
**Class:** `InteractiveCube`
**Visibility:** private
**Kind:** method

## Signature

```python
def _mouse_press(self, event, event_x = None, event_y = None)
```

## Docstring

Record the mouse position and which button was pressed to start a drag. 

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

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self._button1`
- `self._button2`
- `self._event_xy`

**Reads:**
- `self._button1`
- `self._button2`
- `self._event_xy`

## Source

```python
    def _mouse_press(self, event, event_x=None, event_y=None):  # type: ignore
        """ Record the mouse position and which button was pressed to start a drag. """
        if event_x is not None and event_y is not None:
            self._event_xy = (event_x, event_y)
            self._button1 = True
        else:
            self._event_xy = (event.x, event.y)
            if event.button == 1:
                self._button1 = True
            elif event.button == 3:
                self._button2 = True
```
