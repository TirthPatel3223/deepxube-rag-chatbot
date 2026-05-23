---
id: "class:deepxube.domains.npuzzle.GridParser"
kind: "class"
name: "GridParser"
qualified_name: "deepxube.domains.npuzzle.GridParser"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 358
line_end: 365
is_abstract: false
is_dataclass: false
decorators:
  - "@domain_factory.register_parser('npuzzle')"
generic_parameters: []
bases:
  - name: "Parser"
    resolved_id: null
methods:
  - "func:deepxube.domains.npuzzle.GridParser.parse"
  - "func:deepxube.domains.npuzzle.GridParser.help"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.npuzzle.GridParser`

**File:** [deepxube/domains/npuzzle.py:358](../../../deepxube/domains/npuzzle.py#L358)
**Abstract:** no
**Decorators:** `@domain_factory.register_parser('npuzzle')`

## Docstring

CLI parser for the ``npuzzle`` domain; expects an integer dimension string. 

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
    """ CLI parser for the ``npuzzle`` domain; expects an integer dimension string. """

    def parse(self, args_str: str) -> Dict[str, Any]:
        return {"dim": int(args_str)}

    def help(self) -> str:
        return "An integer for the dimension. E.g. 'npuzzle.6'"
```
