---
id: "func:deepxube.domains.grid.GridNetParser.parse"
kind: "method"
name: "parse"
qualified_name: "deepxube.domains.grid.GridNetParser.parse"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 212
line_end: 225
class: "GridNetParser"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "args_str"
    annotation: "str"
    default: null
returns: "Dict[str, Any]"
docstring_source: "present"
callees:
  - target: null
    expr: "args_str.split"
    call_sites: [214]
  - target: null
    expr: "dict"
    call_sites: [215]
  - target: "func:re.search"
    expr: "re.search"
    call_sites: [217, 218]
  - target: null
    expr: "int"
    call_sites: [220, 222]
  - target: null
    expr: "channel_re.group"
    call_sites: [220]
  - target: null
    expr: "fc_re.group"
    call_sites: [222]
  - target: null
    expr: "ValueError"
    call_sites: [224]
raises:
  - exception: "ValueError"
    call_sites: [224]
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.grid.GridNetParser.parse`

**File:** [deepxube/domains/grid.py:212](../../../../deepxube/domains/grid.py#L212)
**Class:** `GridNetParser`
**Visibility:** public
**Kind:** method

## Signature

```python
def parse(self, args_str: str) -> Dict[str, Any]
```

## Docstring

Parse underscore-separated arg string into ``chan_size`` and ``fc_size`` kwargs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `args_str` | `str` | — |

## Returns

`Dict[str, Any]`

## Calls

- `re.search` → `func:re.search` (lines: 217, 218)

### Unresolved
- `args_str.split` (lines: 214)
- `dict` (lines: 215)
- `int` (lines: 220, 222)
- `channel_re.group` (lines: 220)
- `fc_re.group` (lines: 222)
- `ValueError` (lines: 224)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 224)

## Source

```python
    def parse(self, args_str: str) -> Dict[str, Any]:
        """ Parse underscore-separated arg string into ``chan_size`` and ``fc_size`` kwargs. """
        args_str_l: List[str] = args_str.split("_")
        kwargs: Dict[str, Any] = dict()
        for args_str_i in args_str_l:
            channel_re = re.search(r"^(\S+)CH$", args_str_i)
            fc_re = re.search(r"^(\S+)FC$", args_str_i)
            if channel_re is not None:
                kwargs["chan_size"] = int(channel_re.group(1))
            elif fc_re is not None:
                kwargs["fc_size"] = int(fc_re.group(1))
            else:
                raise ValueError(f"Unexpected argument {args_str_i!r}")
        return kwargs
```
