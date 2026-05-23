---
id: "func:deepxube.pathfinding.beam_search.BeamSearchHeurNode.make_instances"
kind: "method"
name: "make_instances"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchHeurNode.make_instances"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 194
line_end: 198
class: "BeamSearchHeurNode"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states"
    annotation: "List[State]"
    default: null
  - name: "goals"
    annotation: "List[Goal]"
    default: null
  - name: "inst_infos"
    annotation: "Optional[List[Any]]"
    default: "None"
  - name: "compute_root_vals"
    annotation: "bool"
    default: "True"
  - name: "beam_size"
    annotation: "Optional[int]"
    default: "None"
  - name: "temp"
    annotation: "Optional[float]"
    default: "None"
  - name: "eps"
    annotation: "Optional[float]"
    default: "None"
returns: "List[InstanceNodeBeam]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.beam_search.BeamSearchHeurNode._create_root_nodes"
    expr: "self._create_root_nodes"
    call_sites: [197]
  - target: "func:deepxube.pathfinding.beam_search.BeamSearchHeurNode._construct_instances"
    expr: "self._construct_instances"
    call_sites: [198]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.beam_search.BeamSearchHeurNode.make_instances`

**File:** [deepxube/pathfinding/beam_search.py:194](../../../../deepxube/pathfinding/beam_search.py#L194)
**Class:** `BeamSearchHeurNode`
**Visibility:** public
**Kind:** method

## Signature

```python
def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True, beam_size: Optional[int] = None, temp: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceNodeBeam]
```

## Docstring

Build node-beam instances, optionally computing root heuristic values. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[State]` | — |
| `goals` | `List[Goal]` | — |
| `inst_infos` | `Optional[List[Any]]` | `None` |
| `compute_root_vals` | `bool` | `True` |
| `beam_size` | `Optional[int]` | `None` |
| `temp` | `Optional[float]` | `None` |
| `eps` | `Optional[float]` | `None` |

## Returns

`List[InstanceNodeBeam]`

## Calls

- `self._create_root_nodes` → `func:deepxube.pathfinding.beam_search.BeamSearchHeurNode._create_root_nodes` (lines: 197)
- `self._construct_instances` → `func:deepxube.pathfinding.beam_search.BeamSearchHeurNode._construct_instances` (lines: 198)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True,
                       beam_size: Optional[int] = None, temp: Optional[float] = None, eps: Optional[float] = None) -> List[InstanceNodeBeam]:
        """ Build node-beam instances, optionally computing root heuristic values. """
        nodes_root: List[Node] = self._create_root_nodes(states, goals, compute_root_vals)
        return self._construct_instances(InstanceNodeBeam, nodes_root, inst_infos, beam_size, temp, eps)
```
