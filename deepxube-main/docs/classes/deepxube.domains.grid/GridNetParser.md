---
id: "class:deepxube.domains.grid.GridNetParser"
kind: "class"
name: "GridNetParser"
qualified_name: "deepxube.domains.grid.GridNetParser"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 209
line_end: 230
is_abstract: false
is_dataclass: false
decorators:
  - "@heuristic_factory.register_parser('gridnet')"
generic_parameters: []
bases:
  - name: "Parser"
    resolved_id: null
methods:
  - "func:deepxube.domains.grid.GridNetParser.parse"
  - "func:deepxube.domains.grid.GridNetParser.help"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.grid.GridNetParser`

**File:** [deepxube/domains/grid.py:209](../../../deepxube/domains/grid.py#L209)
**Abstract:** no
**Decorators:** `@heuristic_factory.register_parser('gridnet')`

## Docstring

CLI parser for ``gridnet`` architecture kwargs. 

## Inheritance

**Direct bases:**
- `Parser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `parse`
- `help` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class GridNetParser(Parser):
    """ CLI parser for ``gridnet`` architecture kwargs. """

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

    def help(self) -> str:
        return ("Arguments are delimited by '_' and can be in any order.\n<num>C (number of channels), "
                "<num>FC (width of fully-connected layer), bn (batch_norm), wn (weight_norm).\n"
                "E.g. gridnet.10CH_200FC")
```
