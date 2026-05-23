---
id: "class:deepxube.heuristics.resnet_fc.ResnetFCParserHeur"
kind: "class"
name: "ResnetFCParserHeur"
qualified_name: "deepxube.heuristics.resnet_fc.ResnetFCParserHeur"
module: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_start: 128
line_end: 155
is_abstract: false
is_dataclass: false
decorators:
  - "@heuristic_factory.register_parser('resnet_fc')"
generic_parameters: []
bases:
  - name: "Parser"
    resolved_id: null
methods:
  - "func:deepxube.heuristics.resnet_fc.ResnetFCParserHeur.parse"
  - "func:deepxube.heuristics.resnet_fc.ResnetFCParserHeur.help"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.heuristics.resnet_fc.ResnetFCParserHeur`

**File:** [deepxube/heuristics/resnet_fc.py:128](../../../deepxube/heuristics/resnet_fc.py#L128)
**Abstract:** no
**Decorators:** `@heuristic_factory.register_parser('resnet_fc')`

## Docstring

CLI parser for ``resnet_fc`` heuristic architecture kwargs. 

## Inheritance

**Direct bases:**
- `Parser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `parse`
- `help` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class ResnetFCParserHeur(Parser):
    """ CLI parser for ``resnet_fc`` heuristic architecture kwargs. """

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

    def help(self) -> str:
        return ("Arguments are delimited by '_' and can be in any order.\n<num>H (number of hidden units), "
                "<num>B (number of blocks), bn (batch_norm), wn (weight_norm).\n"
                "E.g. resnet_fc.1000H_4B_bn")
```
