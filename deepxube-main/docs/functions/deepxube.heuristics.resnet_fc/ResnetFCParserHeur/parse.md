---
id: "func:deepxube.heuristics.resnet_fc.ResnetFCParserHeur.parse"
kind: "method"
name: "parse"
qualified_name: "deepxube.heuristics.resnet_fc.ResnetFCParserHeur.parse"
module: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_start: 131
line_end: 150
class: "ResnetFCParserHeur"
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
    call_sites: [133]
  - target: null
    expr: "dict"
    call_sites: [134]
  - target: "func:re.search"
    expr: "re.search"
    call_sites: [136, 137, 138, 139]
  - target: null
    expr: "int"
    call_sites: [141, 143]
  - target: null
    expr: "hidden_re.group"
    call_sites: [141]
  - target: null
    expr: "blocks_re.group"
    call_sites: [143]
  - target: null
    expr: "ValueError"
    call_sites: [149]
raises:
  - exception: "ValueError"
    call_sites: [149]
reads_attrs: []
writes_attrs: []
---

# `deepxube.heuristics.resnet_fc.ResnetFCParserHeur.parse`

**File:** [deepxube/heuristics/resnet_fc.py:131](../../../../deepxube/heuristics/resnet_fc.py#L131)
**Class:** `ResnetFCParserHeur`
**Visibility:** public
**Kind:** method

## Signature

```python
def parse(self, args_str: str) -> Dict[str, Any]
```

## Docstring

Parse underscore-separated arg string into ``res_dim``, ``num_blocks``, ``batch_norm``, ``weight_norm`` kwargs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `args_str` | `str` | — |

## Returns

`Dict[str, Any]`

## Calls

- `re.search` → `func:re.search` (lines: 136, 137, 138, 139)

### Unresolved
- `args_str.split` (lines: 133)
- `dict` (lines: 134)
- `int` (lines: 141, 143)
- `hidden_re.group` (lines: 141)
- `blocks_re.group` (lines: 143)
- `ValueError` (lines: 149)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 149)

## Source

```python
    def parse(self, args_str: str) -> Dict[str, Any]:
        """ Parse underscore-separated arg string into ``res_dim``, ``num_blocks``, ``batch_norm``, ``weight_norm`` kwargs. """
        args_str_l: List[str] = args_str.split("_")
        kwargs: Dict[str, Any] = dict()
        for args_str_i in args_str_l:
            hidden_re = re.search(r"^(\S+)H$", args_str_i)
            blocks_re = re.search(r"^(\S+)B$", args_str_i)
            bn_re = re.search(r"^bn$", args_str_i)
            wn_re = re.search(r"^wn$", args_str_i)
            if hidden_re is not None:
                kwargs["res_dim"] = int(hidden_re.group(1))
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
