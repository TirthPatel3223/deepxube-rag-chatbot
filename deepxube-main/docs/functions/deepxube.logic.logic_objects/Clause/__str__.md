---
id: "func:deepxube.logic.logic_objects.Clause.__str__"
kind: "method"
name: "__str__"
qualified_name: "deepxube.logic.logic_objects.Clause.__str__"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 207
line_end: 219
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
returns: "str"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [209]
  - target: null
    expr: "self.head.to_code"
    call_sites: [215, 219]
  - target: null
    expr: "','.join"
    call_sites: [216]
  - target: null
    expr: "blit.to_code"
    call_sites: [216]
raises: []
reads_attrs:
  - "self.body"
  - "self.head"
writes_attrs: []
---

# `deepxube.logic.logic_objects.Clause.__str__`

**File:** [deepxube/logic/logic_objects.py:207](../../../../deepxube/logic/logic_objects.py#L207)
**Class:** `Clause`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __str__(self) -> str
```

## Docstring

:return: Human-readable 'head :- body' rule string. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`str`

## Calls

*(No resolved calls.)*

### Unresolved
- `len` (lines: 209)
- `self.head.to_code` (lines: 215, 219)
- `','.join` (lines: 216)
- `blit.to_code` (lines: 216)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.body`
- `self.head`

## Source

```python
    def __str__(self) -> str:
        """ :return: Human-readable 'head :- body' rule string. """
        if len(self.body) > 0:
            # return (
            #    f'{self.head.to_code()}:- '
            #    f'{",".join([blit.to_code() for blit in self.body if blit.predicate[:4] != "dif_"])}'
            # )
            return (
                f'{self.head.to_code()}:- '
                f'{",".join([blit.to_code() for blit in self.body])}'
            )
        else:
            return self.head.to_code()
```
