---
id: "func:deepxube.domains.sokoban.SkState.__eq__"
kind: "method"
name: "__eq__"
qualified_name: "deepxube.domains.sokoban.SkState.__eq__"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 45
line_end: 52
class: "SkState"
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
    annotation: "object"
    default: null
returns: "bool"
docstring_source: "missing"
callees:
  - target: null
    expr: "isinstance"
    call_sites: [46]
  - target: "func:numpy.array_equal"
    expr: "np.array_equal"
    call_sites: [47, 48, 49]
raises: []
reads_attrs:
  - "self.agent"
  - "self.boxes"
  - "self.walls"
writes_attrs: []
---

# `deepxube.domains.sokoban.SkState.__eq__`

**File:** [deepxube/domains/sokoban.py:45](../../../../deepxube/domains/sokoban.py#L45)
**Class:** `SkState`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __eq__(self, other: object) -> bool
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `other` | `object` | — |

## Returns

`bool`

## Calls

- `np.array_equal` → `func:numpy.array_equal` (lines: 47, 48, 49)

### Unresolved
- `isinstance` (lines: 46)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.agent`
- `self.boxes`
- `self.walls`

## Source

```python
    def __eq__(self, other: object) -> bool:
        if isinstance(other, SkState):
            agents_eq: bool = np.array_equal(self.agent, other.agent)
            boxes_eq: bool = np.array_equal(self.boxes, other.boxes)
            walls_eq: bool = np.array_equal(self.walls, other.walls)

            return agents_eq and boxes_eq and walls_eq
        return NotImplemented
```
