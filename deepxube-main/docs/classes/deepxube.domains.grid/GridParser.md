---
id: "class:deepxube.domains.grid.GridParser"
kind: "class"
name: "GridParser"
qualified_name: "deepxube.domains.grid.GridParser"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 153
line_end: 160
is_abstract: false
is_dataclass: false
decorators:
  - "@domain_factory.register_parser('grid')"
generic_parameters: []
bases:
  - name: "Parser"
    resolved_id: null
methods:
  - "func:deepxube.domains.grid.GridParser.parse"
  - "func:deepxube.domains.grid.GridParser.help"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.grid.GridParser`

**File:** [deepxube/domains/grid.py:153](../../../deepxube/domains/grid.py#L153)
**Abstract:** no
**Decorators:** `@domain_factory.register_parser('grid')`

## Docstring

CLI parser for the ``grid`` domain; expects an integer dimension string. 

## Inheritance

**Direct bases:**
- `Parser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `parse` *(trivial, skipped)* — *(no docstring)*
- `help` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class GridParser(Parser):
    """ CLI parser for the ``grid`` domain; expects an integer dimension string. """

    def parse(self, args_str: str) -> Dict[str, Any]:
        return {"dim": int(args_str)}

    def help(self) -> str:
        return "An integer for the dimension. E.g. 'grid.7'"
```
