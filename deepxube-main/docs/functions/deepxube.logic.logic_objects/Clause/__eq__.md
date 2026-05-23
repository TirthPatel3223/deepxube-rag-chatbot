---
id: "func:deepxube.logic.logic_objects.Clause.__eq__"
kind: "method"
name: "__eq__"
qualified_name: "deepxube.logic.logic_objects.Clause.__eq__"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 273
line_end: 290
class: "Clause"
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
docstring_source: "present"
callees:
  - target: null
    expr: "isinstance"
    call_sites: [275]
  - target: "func:deepxube.logic.logic_objects.Clause.theta_sub"
    expr: "self.theta_sub"
    call_sites: [284]
  - target: null
    expr: "other.theta_sub"
    call_sites: [287]
raises: []
reads_attrs:
  - "self.head"
writes_attrs: []
---

# `deepxube.logic.logic_objects.Clause.__eq__`

**File:** [deepxube/logic/logic_objects.py:273](../../../../deepxube/logic/logic_objects.py#L273)
**Class:** `Clause`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __eq__(self, other: object) -> bool
```

## Docstring

:return: True when ``self`` and ``other`` mutually theta-subsume each other. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `other` | `object` | — |

## Returns

`bool`

## Calls

- `self.theta_sub` → `func:deepxube.logic.logic_objects.Clause.theta_sub` (lines: 284)

### Unresolved
- `isinstance` (lines: 275)
- `other.theta_sub` (lines: 287)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.head`

## Source

```python
    def __eq__(self, other: object) -> bool:
        """ :return: True when ``self`` and ``other`` mutually theta-subsume each other. """
        if not isinstance(other, Clause):
            return NotImplemented

        # assuming no repeats
        if (self.head is None) != (other.head is None):
            return False
        if self.head.predicate != other.head.predicate:
            return False

        if self.theta_sub(other) is None:
            return False

        if other.theta_sub(self) is None:
            return False

        return True
```
