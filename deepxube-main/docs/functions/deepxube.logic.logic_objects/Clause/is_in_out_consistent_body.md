---
id: "func:deepxube.logic.logic_objects.Clause.is_in_out_consistent_body"
kind: "method"
name: "is_in_out_consistent_body"
qualified_name: "deepxube.logic.logic_objects.Clause.is_in_out_consistent_body"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 113
line_end: 125
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
    call_sites: [115]
  - target: null
    expr: "var_has_out.update"
    call_sites: [118]
raises: []
reads_attrs:
  - "self.body"
writes_attrs: []
---

# `deepxube.logic.logic_objects.Clause.is_in_out_consistent_body`

**File:** [deepxube/logic/logic_objects.py:113](../../../../deepxube/logic/logic_objects.py#L113)
**Class:** `Clause`
**Visibility:** public
**Kind:** method

## Signature

```python
def is_in_out_consistent_body(self) -> bool
```

## Docstring

:return: True if every 'in' variable in the body is produced (as 'out') by some other body literal. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`bool`

## Calls

*(No resolved calls.)*

### Unresolved
- `set` (lines: 115)
- `var_has_out.update` (lines: 118)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.body`

## Source

```python
    def is_in_out_consistent_body(self) -> bool:
        """ :return: True if every 'in' variable in the body is produced (as 'out') by some other body literal. """
        var_has_out: Set[str] = set()

        for body_lit in self.body:
            var_has_out.update(body_lit.outputs)

        for body_lit in self.body:
            for in_var in body_lit.inputs:
                if in_var not in var_has_out:
                    return False

        return True
```
