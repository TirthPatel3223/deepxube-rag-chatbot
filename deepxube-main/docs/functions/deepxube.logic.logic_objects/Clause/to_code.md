---
id: "func:deepxube.logic.logic_objects.Clause.to_code"
kind: "method"
name: "to_code"
qualified_name: "deepxube.logic.logic_objects.Clause.to_code"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 147
line_end: 155
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
returns: "str"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [149]
  - target: null
    expr: "self.head.to_code"
    call_sites: [151, 155]
  - target: null
    expr: "','.join"
    call_sites: [152]
  - target: null
    expr: "blit.to_code"
    call_sites: [152]
raises: []
reads_attrs:
  - "self.body"
  - "self.head"
writes_attrs: []
---

# `deepxube.logic.logic_objects.Clause.to_code`

**File:** [deepxube/logic/logic_objects.py:147](../../../../deepxube/logic/logic_objects.py#L147)
**Class:** `Clause`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_code(self) -> str
```

## Docstring

:return: Clingo rule string ``'head :- body'``, or just ``'head'`` for facts. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`str`

## Calls

*(No resolved calls.)*

### Unresolved
- `len` (lines: 149)
- `self.head.to_code` (lines: 151, 155)
- `','.join` (lines: 152)
- `blit.to_code` (lines: 152)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.body`
- `self.head`

## Source

```python
    def to_code(self) -> str:
        """ :return: Clingo rule string ``'head :- body'``, or just ``'head'`` for facts. """
        if len(self.body) > 0:
            return (
                f'{self.head.to_code()}:- '
                f'{",".join([blit.to_code() for blit in self.body])}'
            )
        else:
            return self.head.to_code()
```
