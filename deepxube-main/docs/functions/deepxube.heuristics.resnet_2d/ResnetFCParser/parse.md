---
id: "func:deepxube.heuristics.resnet_2d.ResnetFCParser.parse"
kind: "method"
name: "parse"
qualified_name: "deepxube.heuristics.resnet_2d.ResnetFCParser.parse"
module: "deepxube.heuristics.resnet_2d"
file: "deepxube/heuristics/resnet_2d.py"
line_start: 84
line_end: 103
class: "ResnetFCParser"
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
    call_sites: [86]
  - target: null
    expr: "dict"
    call_sites: [87]
  - target: "func:re.search"
    expr: "re.search"
    call_sites: [89, 90, 91, 92]
  - target: null
    expr: "int"
    call_sites: [94, 96]
  - target: null
    expr: "chan_re.group"
    call_sites: [94]
  - target: null
    expr: "blocks_re.group"
    call_sites: [96]
  - target: null
    expr: "ValueError"
    call_sites: [102]
raises:
  - exception: "ValueError"
    call_sites: [102]
reads_attrs: []
writes_attrs: []
---

# `deepxube.heuristics.resnet_2d.ResnetFCParser.parse`

**File:** [deepxube/heuristics/resnet_2d.py:84](../../../../deepxube/heuristics/resnet_2d.py#L84)
**Class:** `ResnetFCParser`
**Visibility:** public
**Kind:** method

## Signature

```python
def parse(self, args_str: str) -> Dict[str, Any]
```

## Docstring

Parse underscore-separated arg string into ``num_chan``, ``num_blocks``, ``batch_norm``, ``weight_norm`` kwargs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `args_str` | `str` | — |

## Returns

`Dict[str, Any]`

## Calls

- `re.search` → `func:re.search` (lines: 89, 90, 91, 92)

### Unresolved
- `args_str.split` (lines: 86)
- `dict` (lines: 87)
- `int` (lines: 94, 96)
- `chan_re.group` (lines: 94)
- `blocks_re.group` (lines: 96)
- `ValueError` (lines: 102)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 102)

## Source

```python
    def parse(self, args_str: str) -> Dict[str, Any]:
        """ Parse underscore-separated arg string into ``num_chan``, ``num_blocks``, ``batch_norm``, ``weight_norm`` kwargs. """
        args_str_l: List[str] = args_str.split("_")
        kwargs: Dict[str, Any] = dict()
        for args_str_i in args_str_l:
            chan_re = re.search(r"^(\S+)C$", args_str_i)
            blocks_re = re.search(r"^(\S+)B$", args_str_i)
            bn_re = re.search(r"^bn$", args_str_i)
            wn_re = re.search(r"^wn$", args_str_i)
            if chan_re is not None:
                kwargs["num_chan"] = int(chan_re.group(1))
            elif blocks_re is not None:
                kwargs["num_blocks"] = int(blocks_re.group(1))
            elif bn_re is not None:
                kwargs["batch_norm"] = True
            elif wn_re is not None:
                kwargs["weight_norm"] = True
            else:
                raise ValueError(f"Unexpected argument {args_str_i!r}")
        return kwargs
```
