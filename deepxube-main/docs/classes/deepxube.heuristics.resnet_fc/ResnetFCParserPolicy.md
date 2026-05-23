---
id: "class:deepxube.heuristics.resnet_fc.ResnetFCParserPolicy"
kind: "class"
name: "ResnetFCParserPolicy"
qualified_name: "deepxube.heuristics.resnet_fc.ResnetFCParserPolicy"
module: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_start: 159
line_end: 193
is_abstract: false
is_dataclass: false
decorators:
  - "@policy_factory.register_parser('resnet_fc')"
generic_parameters: []
bases:
  - name: "ResnetFCParserHeur"
    resolved_id: null
methods:
  - "func:deepxube.heuristics.resnet_fc.ResnetFCParserPolicy.parse"
  - "func:deepxube.heuristics.resnet_fc.ResnetFCParserPolicy.help"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.heuristics.resnet_fc.ResnetFCParserPolicy`

**File:** [deepxube/heuristics/resnet_fc.py:159](../../../deepxube/heuristics/resnet_fc.py#L159)
**Abstract:** no
**Decorators:** `@policy_factory.register_parser('resnet_fc')`

## Docstring

CLI parser for ``resnet_fc`` policy architecture kwargs; extends the heuristic parser with ``enc_dim`` and ``kl_weight``. 

## Inheritance

**Direct bases:**
- `ResnetFCParserHeur`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `parse`
- `help` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class ResnetFCParserPolicy(ResnetFCParserHeur):
    """ CLI parser for ``resnet_fc`` policy architecture kwargs; extends the heuristic parser with ``enc_dim`` and ``kl_weight``. """

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

    def help(self) -> str:
        return ("Arguments are delimited by '_' and can be in any order.\n<num>H (number of hidden units), "
                "<num>B (number of blocks), <enc_dim>E (encoding dimensionality), bn (batch_norm), wn (weight_norm).\n"
                "E.g. resnet_fc.1000H_4B_10E_bn")
```
