---
id: "func:deepxube.utils.misc_utils.remove_all_whitespace"
kind: "function"
name: "remove_all_whitespace"
qualified_name: "deepxube.utils.misc_utils.remove_all_whitespace"
module: "deepxube.utils.misc_utils"
file: "deepxube/utils/misc_utils.py"
line_start: 93
line_end: 102
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "val"
    annotation: "str"
    default: null
returns: "str"
docstring_source: "present"
callees:
  - target: "func:re.compile"
    expr: "re.compile"
    call_sites: [99]
  - target: "func:re.sub"
    expr: "re.sub"
    call_sites: [100]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.misc_utils.remove_all_whitespace`

**File:** [deepxube/utils/misc_utils.py:93](../../../../deepxube/utils/misc_utils.py#L93)
**Visibility:** public
**Kind:** function

## Signature

```python
def remove_all_whitespace(val: str) -> str
```

## Docstring

Return ``val`` with every whitespace character removed.

:param val: Input string.
:return: ``val`` stripped of all whitespace.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `val` | `str` | — |

## Returns

`str`

## Calls

- `re.compile` → `func:re.compile` (lines: 99)
- `re.sub` → `func:re.sub` (lines: 100)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def remove_all_whitespace(val: str) -> str:
    """ Return ``val`` with every whitespace character removed.

    :param val: Input string.
    :return: ``val`` stripped of all whitespace.
    """
    pattern = re.compile(r'\s+')
    val = re.sub(pattern, '', val)

    return val
```
