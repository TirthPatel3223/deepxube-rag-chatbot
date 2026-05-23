---
id: "func:deepxube.pathfinding.beam_search.BeamSearchHeurNode._compute_costs"
kind: "method"
name: "_compute_costs"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchHeurNode._compute_costs"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 200
line_end: 214
class: "BeamSearchHeurNode"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "instances"
    annotation: "List[InstanceNodeBeam]"
    default: null
  - name: "nodes_by_inst"
    annotation: "List[List[Node]]"
    default: null
returns: "List[List[float]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [202, 212]
  - target: null
    expr: "logits.append"
    call_sites: [208]
  - target: null
    expr: "logits_by_inst.append"
    call_sites: [210]
  - target: null
    expr: "self.times.record_time"
    call_sites: [212]
raises: []
reads_attrs:
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.beam_search.BeamSearchHeurNode._compute_costs`

**File:** [deepxube/pathfinding/beam_search.py:200](../../../../deepxube/pathfinding/beam_search.py#L200)
**Class:** `BeamSearchHeurNode`
**Visibility:** private
**Kind:** method

## Signature

```python
def _compute_costs(self, instances: List[InstanceNodeBeam], nodes_by_inst: List[List[Node]]) -> List[List[float]]
```

## Docstring

:return: Per-instance logits = -(transition_cost + heuristic); higher is better. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceNodeBeam]` | — |
| `nodes_by_inst` | `List[List[Node]]` | — |

## Returns

`List[List[float]]`

## Calls

- `time.time` → `func:time.time` (lines: 202, 212)

### Unresolved
- `logits.append` (lines: 208)
- `logits_by_inst.append` (lines: 210)
- `self.times.record_time` (lines: 212)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.times`

## Source

```python
    def _compute_costs(self, instances: List[InstanceNodeBeam], nodes_by_inst: List[List[Node]]) -> List[List[float]]:
        """ :return: Per-instance logits = -(transition_cost + heuristic); higher is better. """
        start_time = time.time()
        logits_by_inst: List[List[float]] = []
        for nodes in nodes_by_inst:
            logits: List[float] = []
            for node in nodes:
                assert node.parent_t_cost is not None
                logits.append(-(node.parent_t_cost + node.heuristic))

            logits_by_inst.append(logits)

        self.times.record_time("logits", time.time() - start_time)

        return logits_by_inst
```
