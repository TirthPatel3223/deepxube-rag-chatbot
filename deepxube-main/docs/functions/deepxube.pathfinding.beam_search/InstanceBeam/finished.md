---
id: "func:deepxube.pathfinding.beam_search.InstanceBeam.finished"
kind: "method"
name: "finished"
qualified_name: "deepxube.pathfinding.beam_search.InstanceBeam.finished"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 84
line_end: 86
class: "InstanceBeam"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "bool"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.beam_search.InstanceBeam.has_soln"
    expr: "self.has_soln"
    call_sites: [86]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.beam_search.InstanceBeam.finished`

**File:** [deepxube/pathfinding/beam_search.py:84](../../../../deepxube/pathfinding/beam_search.py#L84)
**Class:** `InstanceBeam`
**Visibility:** public
**Kind:** method

## Signature

```python
def finished(self) -> bool
```

## Docstring

:return: True once a solved goal has been recorded. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`bool`

## Calls

- `self.has_soln` → `func:deepxube.pathfinding.beam_search.InstanceBeam.has_soln` (lines: 86)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def finished(self) -> bool:
        """ :return: True once a solved goal has been recorded. """
        return self.has_soln()
```
