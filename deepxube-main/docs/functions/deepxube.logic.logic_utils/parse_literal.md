---
id: "func:deepxube.logic.logic_utils.parse_literal"
kind: "function"
name: "parse_literal"
qualified_name: "deepxube.logic.logic_utils.parse_literal"
module: "deepxube.logic.logic_utils"
file: "deepxube/logic/logic_utils.py"
line_start: 10
line_end: 36
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "lit_str"
    annotation: "str"
    default: null
returns: "Literal"
docstring_source: "present"
callees:
  - target: "func:re.match"
    expr: "re.match"
    call_sites: [13, 23]
  - target: null
    expr: "not_match.group(1).strip"
    call_sites: [19]
  - target: null
    expr: "not_match.group"
    call_sites: [19]
  - target: "func:deepxube.utils.misc_utils.remove_all_whitespace"
    expr: "misc_utils.remove_all_whitespace"
    call_sites: [22]
  - target: null
    expr: "match.group"
    call_sites: [25, 27, 28]
  - target: null
    expr: "tuple"
    call_sites: [28, 30, 35]
  - target: null
    expr: "x.strip"
    call_sites: [28]
  - target: null
    expr: "match.group(3).split"
    call_sites: [28]
  - target: null
    expr: "len"
    call_sites: [33]
  - target: "func:deepxube.logic.logic_objects.Literal"
    expr: "Literal"
    call_sites: [35]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.logic_utils.parse_literal`

**File:** [deepxube/logic/logic_utils.py:10](../../../../deepxube/logic/logic_utils.py#L10)
**Visibility:** public
**Kind:** function

## Signature

```python
def parse_literal(lit_str: str) -> Literal
```

## Docstring

Parse a literal string (e.g. ``'not foo(X,Y)'``) into a ``Literal``; all arguments default to direction 'in'. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `lit_str` | `str` | — |

## Returns

`Literal`

## Calls

- `re.match` → `func:re.match` (lines: 13, 23)
- `misc_utils.remove_all_whitespace` → `func:deepxube.utils.misc_utils.remove_all_whitespace` (lines: 22)
- `Literal` → `func:deepxube.logic.logic_objects.Literal` (lines: 35)

### Unresolved
- `not_match.group(1).strip` (lines: 19)
- `not_match.group` (lines: 19)
- `match.group` (lines: 25, 27, 28)
- `tuple` (lines: 28, 30, 35)
- `x.strip` (lines: 28)
- `match.group(3).split` (lines: 28)
- `len` (lines: 33)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def parse_literal(lit_str: str) -> Literal:
    """ Parse a literal string (e.g. ``'not foo(X,Y)'``) into a ``Literal``; all arguments default to direction 'in'. """
    # check for negation
    not_match = re.match(r"\s*not\s+(.*)", lit_str)
    positive: bool
    if not_match is None:
        positive = True
    else:
        positive = False
        lit_str = not_match.group(1).strip()

    # parse literal
    lit_str = misc_utils.remove_all_whitespace(lit_str)
    match = re.match(r"([^(]+)(\((.*)\))?", lit_str)
    assert match is not None
    pred_name: str = match.group(1)
    pred_args: Tuple[str, ...]
    if match.group(3) is not None:
        pred_args = tuple([x.strip() for x in match.group(3).split(",")])
    else:
        pred_args = tuple()

    # TODO, better way to handle directions?
    directions = ["in"] * len(pred_args)

    literal: Literal = Literal(pred_name, pred_args, tuple(directions), positive=positive)
    return literal
```
