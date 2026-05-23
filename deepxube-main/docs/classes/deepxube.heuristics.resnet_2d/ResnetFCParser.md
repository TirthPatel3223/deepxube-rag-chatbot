---
id: "class:deepxube.heuristics.resnet_2d.ResnetFCParser"
kind: "class"
name: "ResnetFCParser"
qualified_name: "deepxube.heuristics.resnet_2d.ResnetFCParser"
module: "deepxube.heuristics.resnet_2d"
file: "deepxube/heuristics/resnet_2d.py"
line_start: 81
line_end: 108
is_abstract: false
is_dataclass: false
decorators:
  - "@heuristic_factory.register_parser('resnet_2d')"
generic_parameters: []
bases:
  - name: "Parser"
    resolved_id: null
methods:
  - "func:deepxube.heuristics.resnet_2d.ResnetFCParser.parse"
  - "func:deepxube.heuristics.resnet_2d.ResnetFCParser.help"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.heuristics.resnet_2d.ResnetFCParser`

**File:** [deepxube/heuristics/resnet_2d.py:81](../../../deepxube/heuristics/resnet_2d.py#L81)
**Abstract:** no
**Decorators:** `@heuristic_factory.register_parser('resnet_2d')`

## Docstring

CLI parser for ``resnet_2d`` heuristic architecture kwargs. 

## Inheritance

**Direct bases:**
- `Parser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `parse`
- `help` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class ResnetFCParser(Parser):
    """ CLI parser for ``resnet_2d`` heuristic architecture kwargs. """

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

    def help(self) -> str:
        return ("Arguments are delimited by '_' and can be in any order.\n<num>C (number of channels), "
                "<num>B (number of blocks), bn (batch_norm), wn (weight_norm).\n"
                "E.g. resnet_2d.64C_4B_bn")
```
