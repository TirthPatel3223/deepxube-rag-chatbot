---
id: "func:deepxube.logic.logic_objects.LitNode.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.logic.logic_objects.LitNode.__init__"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 67
line_end: 75
class: "LitNode"
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
  - name: "in_body"
    annotation: "bool"
    default: null
  - name: "arguments"
    annotation: "Tuple[str, ...]"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "range"
    call_sites: [74]
  - target: null
    expr: "len"
    call_sites: [74]
  - target: null
    expr: "self.var_nodes.append"
    call_sites: [75]
  - target: "func:deepxube.logic.logic_objects.VarNode"
    expr: "VarNode"
    call_sites: [75]
raises: []
reads_attrs:
  - "self.in_body"
  - "self.predicate"
  - "self.rep"
  - "self.var_names"
  - "self.var_nodes"
writes_attrs:
  - "self.in_body"
  - "self.predicate"
  - "self.rep"
  - "self.var_names"
  - "self.var_nodes"
---

# `deepxube.logic.logic_objects.LitNode.__init__`

**File:** [deepxube/logic/logic_objects.py:67](../../../../deepxube/logic/logic_objects.py#L67)
**Class:** `LitNode`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, predicate: str, in_body: bool, arguments: Tuple[str, ...])
```

## Docstring

Build the literal node with one VarNode per argument. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `predicate` | `str` | — |
| `in_body` | `bool` | — |
| `arguments` | `Tuple[str, ...]` | — |

## Returns

*(Not annotated.)*

## Calls

- `VarNode` → `func:deepxube.logic.logic_objects.VarNode` (lines: 75)

### Unresolved
- `range` (lines: 74)
- `len` (lines: 74)
- `self.var_nodes.append` (lines: 75)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.in_body`
- `self.predicate`
- `self.rep`
- `self.var_names`
- `self.var_nodes`

**Reads:**
- `self.in_body`
- `self.predicate`
- `self.rep`
- `self.var_names`
- `self.var_nodes`

## Source

```python
    def __init__(self, predicate: str, in_body: bool, arguments: Tuple[str, ...]):
        """ Build the literal node with one VarNode per argument. """
        self.rep: int = 0
        self.predicate: str = predicate
        self.in_body: bool = in_body
        self.var_nodes: List[VarNode] = []
        self.var_names: Tuple[str, ...] = arguments
        for _ in range(len(arguments)):
            self.var_nodes.append(VarNode())
```
