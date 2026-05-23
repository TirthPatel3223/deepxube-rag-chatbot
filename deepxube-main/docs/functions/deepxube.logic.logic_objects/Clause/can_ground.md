---
id: "func:deepxube.logic.logic_objects.Clause.can_ground"
kind: "method"
name: "can_ground"
qualified_name: "deepxube.logic.logic_objects.Clause.can_ground"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 127
line_end: 145
class: "Clause"
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
  - target: null
    expr: "set"
    call_sites: [130]
  - target: null
    expr: "len"
    call_sites: [132]
  - target: null
    expr: "literal.inputs.issubset"
    call_sites: [135]
  - target: null
    expr: "grounded_variables.union"
    call_sites: [142]
  - target: null
    expr: "body_literals.difference"
    call_sites: [143]
raises: []
reads_attrs:
  - "self.body"
  - "self.head"
writes_attrs: []
---

# `deepxube.logic.logic_objects.Clause.can_ground`

**File:** [deepxube/logic/logic_objects.py:127](../../../../deepxube/logic/logic_objects.py#L127)
**Class:** `Clause`
**Visibility:** public
**Kind:** method

## Signature

```python
def can_ground(self) -> bool
```

## Docstring

:return: True if the body literals can be ordered so that all 'in' variables are bound before use. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`bool`

## Calls

*(No resolved calls.)*

### Unresolved
- `set` (lines: 130)
- `len` (lines: 132)
- `literal.inputs.issubset` (lines: 135)
- `grounded_variables.union` (lines: 142)
- `body_literals.difference` (lines: 143)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.body`
- `self.head`

## Source

```python
    def can_ground(self) -> bool:
        """ :return: True if the body literals can be ordered so that all 'in' variables are bound before use. """
        grounded_variables = self.head.inputs
        body_literals = set(self.body)

        while len(body_literals) > 0:
            selected_literal = None
            for literal in body_literals:
                if literal.inputs.issubset(grounded_variables):
                    selected_literal = literal
                    break

            if selected_literal is None:
                return False

            grounded_variables = grounded_variables.union(selected_literal.outputs)
            body_literals = body_literals.difference({selected_literal})

        return True
```
