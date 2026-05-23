---
id: "class:deepxube.logic.logic_objects.Literal"
kind: "class"
name: "Literal"
qualified_name: "deepxube.logic.logic_objects.Literal"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 7
line_end: 50
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.logic.logic_objects.Literal.__init__"
  - "func:deepxube.logic.logic_objects.Literal.to_code"
  - "func:deepxube.logic.logic_objects.Literal.get_pred_arity_pos_id"
  - "func:deepxube.logic.logic_objects.Literal.__str__"
  - "func:deepxube.logic.logic_objects.Literal.__repr__"
attributes:
  - name: "self.arguments"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.arity"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.directions"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.in_out"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.inputs"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.outputs"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.positive"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.predicate"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.logic.logic_objects.Literal`

**File:** [deepxube/logic/logic_objects.py:7](../../../deepxube/logic/logic_objects.py#L7)
**Abstract:** no

## Docstring

A first-order literal: predicate name, positional arguments with in/out direction tags, and polarity. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `to_code`
- `get_pred_arity_pos_id` *(trivial, skipped)* — *(no docstring)*
- `__str__` *(trivial, skipped)* — *(no docstring)*
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.arguments` | — | __init__ |
| `self.arity` | — | __init__ |
| `self.directions` | — | __init__ |
| `self.in_out` | — | __init__ |
| `self.inputs` | — | __init__ |
| `self.outputs` | — | __init__ |
| `self.positive` | — | __init__ |
| `self.predicate` | — | __init__ |

## Source

```python
class Literal:
    """ A first-order literal: predicate name, positional arguments with in/out direction tags, and polarity. """

    def __init__(self, predicate: str, arguments: Tuple[str, ...], directions: Tuple[str, ...], positive: bool = True):
        """ Build the literal, compute input/output argument sets and the in_out relation; validate directions.
        :raises AssertionError: If any direction is not 'in' or 'out'.
        """
        self.predicate: str = predicate
        self.arguments: Tuple[str, ...] = arguments
        self.directions: Tuple[str, ...] = directions
        for direction in self.directions:
            assert direction in ["in", "out"], f"Direction must be 'in' or 'out' but is {direction}"

        self.arity: int = len(self.arguments)
        self.positive: bool = positive

        self.inputs: Set[str] = set(arg for direction, arg in zip(self.directions, self.arguments) if direction == 'in')
        self.outputs: Set[str] = set(arg for direction, arg in zip(self.directions, self.arguments)
                                     if direction == 'out')

        self.in_out: Set[Tuple[str, str]] = set()
        for arg, direction in zip(self.arguments, self.directions):
            self.in_out.add((arg, direction))

    def to_code(self) -> str:
        """ :return: Clingo-compatible string representation (prefixed with 'not ' when negative). """
        prefix: str = ""
        if not self.positive:
            prefix = "not "

        if len(self.arguments) > 0:
            return f'{prefix}{self.predicate}({",".join(self.arguments)})'
        else:
            return f'{prefix}{self.predicate}'

    def get_pred_arity_pos_id(self) -> Tuple[str, int, bool]:
        tup: Tuple[str, int, bool] = (self.predicate, len(self.arguments), self.positive)
        return tup

    def __str__(self) -> str:
        return self.to_code()

    def __repr__(self) -> str:
        return self.__str__()
```
