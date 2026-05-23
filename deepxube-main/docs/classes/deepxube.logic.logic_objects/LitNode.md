---
id: "class:deepxube.logic.logic_objects.LitNode"
kind: "class"
name: "LitNode"
qualified_name: "deepxube.logic.logic_objects.LitNode"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 64
line_end: 83
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.logic.logic_objects.LitNode.__init__"
  - "func:deepxube.logic.logic_objects.LitNode.prop_up"
  - "func:deepxube.logic.logic_objects.LitNode.prop_down"
attributes:
  - name: "self.in_body"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.predicate"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.rep"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.var_names"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.var_nodes"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.logic.logic_objects.LitNode`

**File:** [deepxube/logic/logic_objects.py:64](../../../deepxube/logic/logic_objects.py#L64)
**Abstract:** no

## Docstring

Node in the clause literal graph used by ``Clause.__hash__``; owns one ``VarNode`` per argument position. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `prop_up` *(trivial, skipped)* — *(no docstring)*
- `prop_down`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.in_body` | — | __init__ |
| `self.predicate` | — | __init__ |
| `self.rep` | — | __init__ |
| `self.var_names` | — | __init__ |
| `self.var_nodes` | — | __init__ |

## Source

```python
class LitNode:
    """ Node in the clause literal graph used by ``Clause.__hash__``; owns one ``VarNode`` per argument position. """

    def __init__(self, predicate: str, in_body: bool, arguments: Tuple[str, ...]):
        """ Build the literal node with one VarNode per argument. """
        self.rep: int = 0
        self.predicate: str = predicate
        self.in_body: bool = in_body
        self.var_nodes: List[VarNode] = []
        self.var_names: Tuple[str, ...] = arguments
        for _ in range(len(arguments)):
            self.var_nodes.append(VarNode())

    def prop_up(self) -> None:
        self.rep = hash((self.predicate, self.in_body) + tuple(x.rep for x in self.var_nodes))

    def prop_down(self) -> None:
        """ Propagate this literal's rep down into its variable nodes. """
        for var_idx, var_node in enumerate(self.var_nodes):
            var_node.rep = hash((self.rep, var_idx))
```
