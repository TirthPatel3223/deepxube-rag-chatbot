---
id: "func:deepxube.domains.sokoban.SkNNetInput.to_np"
kind: "method"
name: "to_np"
qualified_name: "deepxube.domains.sokoban.SkNNetInput.to_np"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 354
line_end: 365
class: "SkNNetInput"
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
    annotation: "List[SkState]"
    default: null
  - name: "goals"
    annotation: "List[SkGoal]"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [356, 357, 358, 359, 363]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [360]
  - target: null
    expr: "len"
    call_sites: [360, 361]
  - target: "func:numpy.arange"
    expr: "np.arange"
    call_sites: [361]
  - target: null
    expr: "np.reshape(rep_np, (rep_np.shape[0], -1)).astype"
    call_sites: [364]
  - target: "func:numpy.reshape"
    expr: "np.reshape"
    call_sites: [364]
raises: []
reads_attrs:
  - "self.domain"
writes_attrs: []
---

# `deepxube.domains.sokoban.SkNNetInput.to_np`

**File:** [deepxube/domains/sokoban.py:354](../../../../deepxube/domains/sokoban.py#L354)
**Class:** `SkNNetInput`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_np(self, states: List[SkState], goals: List[SkGoal]) -> List[NDArray]
```

## Docstring

:return: Shape ``(N, 400)`` uint8 array of stacked ``[walls, boxes, agent, targets]`` channels. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[SkState]` | — |
| `goals` | `List[SkGoal]` | — |

## Returns

`List[NDArray]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 356, 357, 358, 359, 363)
- `np.zeros` → `func:numpy.zeros` (lines: 360)
- `np.arange` → `func:numpy.arange` (lines: 361)
- `np.reshape` → `func:numpy.reshape` (lines: 364)

### Unresolved
- `len` (lines: 360, 361)
- `np.reshape(rep_np, (rep_np.shape[0], -1)).astype` (lines: 364)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`

## Source

```python
    def to_np(self, states: List[SkState], goals: List[SkGoal]) -> List[NDArray]:
        """ :return: Shape ``(N, 400)`` uint8 array of stacked ``[walls, boxes, agent, targets]`` channels. """
        walls: NDArray = np.stack([state.walls for state in states], axis=0)
        boxes: NDArray = np.stack([state.boxes for state in states], axis=0)
        targets: NDArray = np.stack([goal.boxes for goal in goals], axis=0)
        agent_locs: NDArray = np.stack([state.agent for state in states], axis=0)
        agents: NDArray = np.zeros((len(states), self.domain.dim, self.domain.dim))
        agents[np.arange(0, len(states)), agent_locs[:, 0], agent_locs[:, 1]] = 1

        rep_np: NDArray = np.stack([walls, boxes, agents, targets], axis=1)
        rep_np = np.reshape(rep_np, (rep_np.shape[0], -1)).astype(np.uint8)
        return [rep_np]
```
