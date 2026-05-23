---
id: "class:deepxube.base.factory.Parser"
kind: "class"
name: "Parser"
qualified_name: "deepxube.base.factory.Parser"
module: "deepxube.base.factory"
file: "deepxube/base/factory.py"
line_start: 21
line_end: 49
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.factory.Parser.parse"
  - "func:deepxube.base.factory.Parser.help"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.factory.Parser`

**File:** [deepxube/base/factory.py:21](../../../deepxube/base/factory.py#L21)
**Abstract:** yes

## Docstring

Abstract base for a factory argument parser.

A concrete ``Parser`` turns the dotted suffix of a CLI argument (the part
after the first ``.``, e.g. ``"7"`` in ``grid.7``) into a dictionary of
keyword arguments to pass to the constructor of the class registered under
the same name.

## Inheritance

**Direct bases:**
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `parse` *(trivial, skipped)*
- `help` *(trivial, skipped)*

## Source

```python
class Parser(ABC):
    """ Abstract base for a factory argument parser.

    A concrete ``Parser`` turns the dotted suffix of a CLI argument (the part
    after the first ``.``, e.g. ``"7"`` in ``grid.7``) into a dictionary of
    keyword arguments to pass to the constructor of the class registered under
    the same name.
    """

    @abstractmethod
    def parse(self, args_str: str) -> Dict[str, Any]:
        """ Parse a dotted argument string into constructor keyword arguments.

        :param args_str: The portion of the CLI argument following the leading
            name and dot, e.g. for ``--domain grid.7`` this receives ``"7"``.
        :return: A dictionary of keyword arguments suitable for passing to
            the constructor of the factory-registered class.
        """
        pass

    @abstractmethod
    def help(self) -> str:
        """ Return a human-readable help string describing the accepted argument
        format.

        :return: A multi-line string explaining the syntax and the meaning of
            each sub-argument.
        """
        pass
```
