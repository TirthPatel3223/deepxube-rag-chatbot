---
id: "func:deepxube.domains.cube3.InteractiveCube._mouse_release"
kind: "method"
name: "_mouse_release"
qualified_name: "deepxube.domains.cube3.InteractiveCube._mouse_release"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 469
line_end: 475
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

# `deepxube.domains.cube3.InteractiveCube._mouse_release`

**File:** [deepxube/domains/cube3.py:469](../../../../deepxube/domains/cube3.py#L469)
**Class:** `InteractiveCube`
**Visibility:** private
**Kind:** method

## Signature

```python
def _mouse_release(self, event)
```

## Docstring

Clear drag state when a mouse button is released. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `event` | — | — |

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
    def _mouse_release(self, event):  # type: ignore
        """ Clear drag state when a mouse button is released. """
        self._event_xy = None  # type: ignore
        if event.button == 1:
            self._button1 = False
        elif event.button == 3:
            self._button2 = False
```
