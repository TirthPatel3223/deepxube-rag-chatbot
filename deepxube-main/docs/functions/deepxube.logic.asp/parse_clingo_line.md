---
id: "func:deepxube.logic.asp.parse_clingo_line"
kind: "function"
name: "parse_clingo_line"
qualified_name: "deepxube.logic.asp.parse_clingo_line"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 26
line_end: 35
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "line"
    annotation: "str"
    default: null
returns: "str"
docstring_source: "present"
callees:
  - target: "func:re.search"
    expr: "re.search"
    call_sites: [28, 32]
  - target: null
    expr: "line.strip"
    call_sites: [31]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.asp.parse_clingo_line`

**File:** [deepxube/logic/asp.py:26](../../../../deepxube/logic/asp.py#L26)
**Visibility:** public
**Kind:** function

## Signature

```python
def parse_clingo_line(line: str) -> str
```

## Docstring

Strip ``line`` and append '.' if missing; :return: the normalised line, or '' if the line is blank. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `line` | `str` | — |

## Returns

`str`

## Calls

- `re.search` → `func:re.search` (lines: 28, 32)

### Unresolved
- `line.strip` (lines: 31)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def parse_clingo_line(line: str) -> str:
    """ Strip ``line`` and append '.' if missing; :return: the normalised line, or '' if the line is blank. """
    if re.search(r"\S", line) is None:
        return ""

    line = line.strip()
    if re.search(r"\.$", line) is None:
        line = f"{line}."

    return line
```
