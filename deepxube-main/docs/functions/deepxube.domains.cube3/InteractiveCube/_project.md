---
id: "func:deepxube.domains.cube3.InteractiveCube._project"
kind: "method"
name: "_project"
qualified_name: "deepxube.domains.cube3.InteractiveCube._project"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 408
line_end: 410
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
  - name: "pts"
    annotation: null
    default: null
returns: null
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.cube3.project_points"
    expr: "project_points"
    call_sites: [410]
raises: []
reads_attrs:
  - "self._current_rot"
  - "self._view"
writes_attrs: []
---

# `deepxube.domains.cube3.InteractiveCube._project`

**File:** [deepxube/domains/cube3.py:408](../../../../deepxube/domains/cube3.py#L408)
**Class:** `InteractiveCube`
**Visibility:** private
**Kind:** method

## Signature

```python
def _project(self, pts)
```

## Docstring

:return: Projected 2D coordinates of ``pts`` under the current view rotation. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `pts` | — | — |

## Returns

*(Not annotated.)*

## Calls

- `project_points` → `func:deepxube.domains.cube3.project_points` (lines: 410)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self._current_rot`
- `self._view`

## Source

```python
    def _project(self, pts):  # type: ignore
        """ :return: Projected 2D coordinates of ``pts`` under the current view rotation. """
        return project_points(pts, self._current_rot, self._view, [0, 1, 0])
```
