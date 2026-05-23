---
id: "func:deepxube.logic.logic_objects.prop_across"
kind: "function"
name: "prop_across"
qualified_name: "deepxube.logic.logic_objects.prop_across"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 86
line_end: 94
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "var_nodes"
    annotation: "List[VarNode]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "sum"
    call_sites: [90]
  - target: null
    expr: "reps_new.append"
    call_sites: [91]
  - target: null
    expr: "zip"
    call_sites: [93]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.logic_objects.prop_across`

**File:** [deepxube/logic/logic_objects.py:86](../../../../deepxube/logic/logic_objects.py#L86)
**Visibility:** public
**Kind:** function

## Signature

```python
def prop_across(var_nodes: List[VarNode]) -> None
```

## Docstring

Accumulate neighbour reps into each variable node (one WL message-passing step). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `var_nodes` | `List[VarNode]` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `sum` (lines: 90)
- `reps_new.append` (lines: 91)
- `zip` (lines: 93)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def prop_across(var_nodes: List[VarNode]) -> None:
    """ Accumulate neighbour reps into each variable node (one WL message-passing step). """
    reps_new: List[int] = []
    for var_node in var_nodes:
        rep_new: int = sum([x.rep for x in var_node.neighbors])
        reps_new.append(rep_new)

    for var_node, rep_new in zip(var_nodes, reps_new):
        var_node.rep = rep_new
```
