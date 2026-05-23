---
id: "func:deepxube.logic.logic_objects.Literal.to_code"
kind: "method"
name: "to_code"
qualified_name: "deepxube.logic.logic_objects.Literal.to_code"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 31
line_end: 40
class: "Literal"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "str"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [37]
  - target: null
    expr: "','.join"
    call_sites: [38]
raises: []
reads_attrs:
  - "self.arguments"
  - "self.positive"
  - "self.predicate"
writes_attrs: []
---

# `deepxube.logic.logic_objects.Literal.to_code`

**File:** [deepxube/logic/logic_objects.py:31](../../../../deepxube/logic/logic_objects.py#L31)
**Class:** `Literal`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_code(self) -> str
```

## Docstring

:return: Clingo-compatible string representation (prefixed with 'not ' when negative). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`str`

## Calls

*(No resolved calls.)*

### Unresolved
- `len` (lines: 37)
- `','.join` (lines: 38)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.arguments`
- `self.positive`
- `self.predicate`

## Source

```python
    def to_code(self) -> str:
        """ :return: Clingo-compatible string representation (prefixed with 'not ' when negative). """
        prefix: str = ""
        if not self.positive:
            prefix = "not "

        if len(self.arguments) > 0:
            return f'{prefix}{self.predicate}({",".join(self.arguments)})'
        else:
            return f'{prefix}{self.predicate}'
```
