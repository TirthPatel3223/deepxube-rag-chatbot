---
id: "func:deepxube.logic.logic_objects.Literal.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.logic.logic_objects.Literal.__init__"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 10
line_end: 29
class: "Literal"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "predicate"
    annotation: "str"
    default: null
  - name: "arguments"
    annotation: "Tuple[str, ...]"
    default: null
  - name: "directions"
    annotation: "Tuple[str, ...]"
    default: null
  - name: "positive"
    annotation: "bool"
    default: "True"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [20]
  - target: null
    expr: "set"
    call_sites: [23, 24, 27]
  - target: null
    expr: "zip"
    call_sites: [23, 24, 28]
  - target: null
    expr: "self.in_out.add"
    call_sites: [29]
raises: []
reads_attrs:
  - "self.arguments"
  - "self.arity"
  - "self.directions"
  - "self.in_out"
  - "self.inputs"
  - "self.outputs"
  - "self.positive"
  - "self.predicate"
writes_attrs:
  - "self.arguments"
  - "self.arity"
  - "self.directions"
  - "self.in_out"
  - "self.inputs"
  - "self.outputs"
  - "self.positive"
  - "self.predicate"
---

# `deepxube.logic.logic_objects.Literal.__init__`

**File:** [deepxube/logic/logic_objects.py:10](../../../../deepxube/logic/logic_objects.py#L10)
**Class:** `Literal`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, predicate: str, arguments: Tuple[str, ...], directions: Tuple[str, ...], positive: bool = True)
```

## Docstring

Build the literal, compute input/output argument sets and the in_out relation; validate directions.
:raises AssertionError: If any direction is not 'in' or 'out'.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `predicate` | `str` | — |
| `arguments` | `Tuple[str, ...]` | — |
| `directions` | `Tuple[str, ...]` | — |
| `positive` | `bool` | `True` |

## Returns

*(Not annotated.)*

## Calls

*(No resolved calls.)*

### Unresolved
- `len` (lines: 20)
- `set` (lines: 23, 24, 27)
- `zip` (lines: 23, 24, 28)
- `self.in_out.add` (lines: 29)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.arguments`
- `self.arity`
- `self.directions`
- `self.in_out`
- `self.inputs`
- `self.outputs`
- `self.positive`
- `self.predicate`

**Reads:**
- `self.arguments`
- `self.arity`
- `self.directions`
- `self.in_out`
- `self.inputs`
- `self.outputs`
- `self.positive`
- `self.predicate`

## Source

```python
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
```
