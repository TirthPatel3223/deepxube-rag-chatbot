---
id: "func:deepxube.pathfinding.beam_search.InstanceEdgeBeam.push_pop_edges"
kind: "method"
name: "push_pop_edges"
qualified_name: "deepxube.pathfinding.beam_search.InstanceEdgeBeam.push_pop_edges"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 150
line_end: 153
class: "InstanceEdgeBeam"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "edges"
    annotation: "List[EdgeQ]"
    default: null
  - name: "costs"
    annotation: "List[float]"
    default: null
returns: "List[EdgeQ]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.beam_search.InstanceEdgeBeam.select_idxs_from_logits"
    expr: "self.select_idxs_from_logits"
    call_sites: [152]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.beam_search.InstanceEdgeBeam.push_pop_edges`

**File:** [deepxube/pathfinding/beam_search.py:150](../../../../deepxube/pathfinding/beam_search.py#L150)
**Class:** `InstanceEdgeBeam`
**Visibility:** public
**Kind:** method

## Signature

```python
def push_pop_edges(self, edges: List[EdgeQ], costs: List[float]) -> List[EdgeQ]
```

## Docstring

Pick the beam from candidate edges by their logits. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `edges` | `List[EdgeQ]` | — |
| `costs` | `List[float]` | — |

## Returns

`List[EdgeQ]`

## Calls

- `self.select_idxs_from_logits` → `func:deepxube.pathfinding.beam_search.InstanceEdgeBeam.select_idxs_from_logits` (lines: 152)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def push_pop_edges(self, edges: List[EdgeQ], costs: List[float]) -> List[EdgeQ]:
        """ Pick the beam from candidate edges by their logits. """
        next_idxs: List[int] = self.select_idxs_from_logits(costs)
        return [edges[idx] for idx in next_idxs]
```
