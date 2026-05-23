---
id: "class:deepxube.domains.lightsout.LightsOutParser"
kind: "class"
name: "LightsOutParser"
qualified_name: "deepxube.domains.lightsout.LightsOutParser"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 158
line_end: 165
is_abstract: false
is_dataclass: false
decorators:
  - "@domain_factory.register_parser('lightsout')"
generic_parameters: []
bases:
  - name: "Parser"
    resolved_id: null
methods:
  - "func:deepxube.domains.lightsout.LightsOutParser.parse"
  - "func:deepxube.domains.lightsout.LightsOutParser.help"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.lightsout.LightsOutParser`

**File:** [deepxube/domains/lightsout.py:158](../../../deepxube/domains/lightsout.py#L158)
**Abstract:** no
**Decorators:** `@domain_factory.register_parser('lightsout')`

## Docstring

CLI parser for the ``lightsout`` domain; expects an integer dimension string. 

## Inheritance

**Direct bases:**
- `Parser`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `parse` *(trivial, skipped)* — *(no docstring)*
- `help` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class LightsOutParser(Parser):
    """ CLI parser for the ``lightsout`` domain; expects an integer dimension string. """

    def parse(self, args_str: str) -> Dict[str, Any]:
        return {"dim": int(args_str)}

    def help(self) -> str:
        return "An integer for the dimension. E.g. '7'"
```
