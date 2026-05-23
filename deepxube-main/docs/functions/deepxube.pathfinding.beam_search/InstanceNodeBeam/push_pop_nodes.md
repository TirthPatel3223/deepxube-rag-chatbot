---
id: "func:deepxube.pathfinding.beam_search.InstanceNodeBeam.push_pop_nodes"
kind: "method"
name: "push_pop_nodes"
qualified_name: "deepxube.pathfinding.beam_search.InstanceNodeBeam.push_pop_nodes"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 132
line_end: 135
class: "InstanceNodeBeam"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "nodes"
    annotation: "List[Node]"
    default: null
  - name: "costs"
    annotation: "List[float]"
    default: null
returns: "List[Node]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.beam_search.InstanceNodeBeam.select_idxs_from_logits"
    expr: "self.select_idxs_from_logits"
    call_sites: [134]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.beam_search.InstanceNodeBeam.push_pop_nodes`

**File:** [deepxube/pathfinding/beam_search.py:132](../../../../deepxube/pathfinding/beam_search.py#L132)
**Class:** `InstanceNodeBeam`
**Visibility:** public
**Kind:** method

## Signature

```python
def push_pop_nodes(self, nodes: List[Node], costs: List[float]) -> List[Node]
```

## Docstring

Pick the beam from the expanded nodes by their costs (logits). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nodes` | `List[Node]` | — |
| `costs` | `List[float]` | — |

## Returns

`List[Node]`

## Calls

- `self.select_idxs_from_logits` → `func:deepxube.pathfinding.beam_search.InstanceNodeBeam.select_idxs_from_logits` (lines: 134)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def push_pop_nodes(self, nodes: List[Node], costs: List[float]) -> List[Node]:
        """ Pick the beam from the expanded nodes by their costs (logits). """
        next_idxs: List[int] = self.select_idxs_from_logits(costs)
        return [nodes[idx] for idx in next_idxs]
```
