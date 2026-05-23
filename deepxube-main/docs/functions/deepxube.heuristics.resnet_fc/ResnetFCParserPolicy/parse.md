---
id: "func:deepxube.heuristics.resnet_fc.ResnetFCParserPolicy.parse"
kind: "method"
name: "parse"
qualified_name: "deepxube.heuristics.resnet_fc.ResnetFCParserPolicy.parse"
module: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_start: 162
line_end: 188
class: "ResnetFCParserPolicy"
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
    call_sites: [164]
  - target: null
    expr: "dict"
    call_sites: [165]
  - target: "func:re.search"
    expr: "re.search"
    call_sites: [168, 169, 170, 171, 172, 173]
  - target: null
    expr: "int"
    call_sites: [175, 177, 183]
  - target: null
    expr: "hidden_re.group"
    call_sites: [175]
  - target: null
    expr: "blocks_re.group"
    call_sites: [177]
  - target: null
    expr: "enc_dim_re.group"
    call_sites: [183]
  - target: null
    expr: "float"
    call_sites: [185]
  - target: null
    expr: "kl_re.group"
    call_sites: [185]
  - target: null
    expr: "ValueError"
    call_sites: [187]
raises:
  - exception: "ValueError"
    call_sites: [187]
reads_attrs: []
writes_attrs: []
---

# `deepxube.heuristics.resnet_fc.ResnetFCParserPolicy.parse`

**File:** [deepxube/heuristics/resnet_fc.py:162](../../../../deepxube/heuristics/resnet_fc.py#L162)
**Class:** `ResnetFCParserPolicy`
**Visibility:** public
**Kind:** method

## Signature

```python
def parse(self, args_str: str) -> Dict[str, Any]
```

## Docstring

Parse arg string into ``res_dim``, ``num_blocks``, ``enc_dim``, ``kl_weight``, ``batch_norm``, ``weight_norm`` kwargs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `args_str` | `str` | — |

## Returns

`Dict[str, Any]`

## Calls

- `re.search` → `func:re.search` (lines: 168, 169, 170, 171, 172, 173)

### Unresolved
- `args_str.split` (lines: 164)
- `dict` (lines: 165)
- `int` (lines: 175, 177, 183)
- `hidden_re.group` (lines: 175)
- `blocks_re.group` (lines: 177)
- `enc_dim_re.group` (lines: 183)
- `float` (lines: 185)
- `kl_re.group` (lines: 185)
- `ValueError` (lines: 187)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 187)

## Source

```python
    def parse(self, args_str: str) -> Dict[str, Any]:
        """ Parse arg string into ``res_dim``, ``num_blocks``, ``enc_dim``, ``kl_weight``, ``batch_norm``, ``weight_norm`` kwargs. """
        args_str_l: List[str] = args_str.split("_")
        kwargs: Dict[str, Any] = dict()
        kwargs["kl_weight"] = 1.0
        for args_str_i in args_str_l:
            hidden_re = re.search(r"^(\S+)H$", args_str_i)
            blocks_re = re.search(r"^(\S+)B$", args_str_i)
            enc_dim_re = re.search(r"^(\S+)E$", args_str_i)
            kl_re = re.search(r"^(\S+)KL$", args_str_i)
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
            elif enc_dim_re is not None:
                kwargs["enc_dim"] = int(enc_dim_re.group(1))
            elif kl_re is not None:
                kwargs["kl_weight"] = float(kl_re.group(1))
            else:
                raise ValueError(f"Unexpected argument {args_str_i!r}")
        return kwargs
```
