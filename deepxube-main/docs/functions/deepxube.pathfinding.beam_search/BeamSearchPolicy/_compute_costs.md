---
id: "func:deepxube.pathfinding.beam_search.BeamSearchPolicy._compute_costs"
kind: "method"
name: "_compute_costs"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchPolicy._compute_costs"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 177
line_end: 187
class: "BeamSearchPolicy"
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
    annotation: "List[InstanceEdgeBeam]"
    default: null
  - name: "edges_by_inst"
    annotation: "List[List[EdgeQ]]"
    default: null
returns: "List[List[float]]"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [179, 185]
  - target: null
    expr: "logits_by_inst.append"
    call_sites: [183]
  - target: null
    expr: "self.times.record_time"
    call_sites: [185]
raises: []
reads_attrs:
  - "self.times"
writes_attrs: []
---

# `deepxube.pathfinding.beam_search.BeamSearchPolicy._compute_costs`

**File:** [deepxube/pathfinding/beam_search.py:177](../../../../deepxube/pathfinding/beam_search.py#L177)
**Class:** `BeamSearchPolicy`
**Visibility:** private
**Kind:** method

## Signature

```python
def _compute_costs(self, instances: List[InstanceEdgeBeam], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]
```

## Docstring

Logits = the policy's per-edge log-probabilities (already in ``edge.q_val``). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceEdgeBeam]` | — |
| `edges_by_inst` | `List[List[EdgeQ]]` | — |

## Returns

`List[List[float]]`

## Calls

- `time.time` → `func:time.time` (lines: 179, 185)

### Unresolved
- `logits_by_inst.append` (lines: 183)
- `self.times.record_time` (lines: 185)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.times`

## Source

```python
    def _compute_costs(self, instances: List[InstanceEdgeBeam], edges_by_inst: List[List[EdgeQ]]) -> List[List[float]]:
        """ Logits = the policy's per-edge log-probabilities (already in ``edge.q_val``). """
        start_time = time.time()
        logits_by_inst: List[List[float]] = []
        for edges in edges_by_inst:
            logits: List[float] = [edge.q_val for edge in edges]  # corresponds to prob densities
            logits_by_inst.append(logits)

        self.times.record_time("logits", time.time() - start_time)

        return logits_by_inst
```
