---
id: "func:deepxube.domains.sokoban.Sokoban.next_state"
kind: "method"
name: "next_state"
qualified_name: "deepxube.domains.sokoban.Sokoban.next_state"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 175
line_end: 226
class: "Sokoban"
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
  - name: "actions"
    annotation: "List[SkAction]"
    default: null
returns: "Tuple[List[SkState], List[float]]"
docstring_source: "present"
callees:
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [178, 179, 180]
  - target: "func:numpy.arange"
    expr: "np.arange"
    call_sites: [182]
  - target: null
    expr: "len"
    call_sites: [182, 220, 224]
  - target: "func:deepxube.domains.sokoban.Sokoban._get_next_idx"
    expr: "self._get_next_idx"
    call_sites: [183, 194]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [184]
  - target: null
    expr: "boxes.copy"
    call_sites: [186]
  - target: "func:numpy.logical_not"
    expr: "np.logical_not"
    call_sites: [204, 215]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [206]
  - target: null
    expr: "range"
    call_sites: [220, 224]
  - target: "func:deepxube.domains.sokoban.SkState"
    expr: "SkState"
    call_sites: [221]
  - target: null
    expr: "states_next.append"
    call_sites: [222]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.sokoban.Sokoban.next_state`

**File:** [deepxube/domains/sokoban.py:175](../../../../deepxube/domains/sokoban.py#L175)
**Class:** `Sokoban`
**Visibility:** public
**Kind:** method

## Signature

```python
def next_state(self, states: List[SkState], actions: List[SkAction]) -> Tuple[List[SkState], List[float]]
```

## Docstring

:return: States after applying movement rules: agent→wall stays, agent→box→obstacle stays,
agent→box→empty slides box, agent→empty moves freely. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[SkState]` | — |
| `actions` | `List[SkAction]` | — |

## Returns

`Tuple[List[SkState], List[float]]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 178, 179, 180)
- `np.arange` → `func:numpy.arange` (lines: 182)
- `self._get_next_idx` → `func:deepxube.domains.sokoban.Sokoban._get_next_idx` (lines: 183, 194)
- `np.zeros` → `func:numpy.zeros` (lines: 184)
- `np.logical_not` → `func:numpy.logical_not` (lines: 204, 215)
- `np.where` → `func:numpy.where` (lines: 206)
- `SkState` → `func:deepxube.domains.sokoban.SkState` (lines: 221)

### Unresolved
- `len` (lines: 182, 220, 224)
- `boxes.copy` (lines: 186)
- `range` (lines: 220, 224)
- `states_next.append` (lines: 222)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def next_state(self, states: List[SkState], actions: List[SkAction]) -> Tuple[List[SkState], List[float]]:
        """ :return: States after applying movement rules: agent→wall stays, agent→box→obstacle stays,
        agent→box→empty slides box, agent→empty moves freely. """
        agent = np.stack([state.agent for state in states], axis=0)
        boxes = np.stack([state.boxes for state in states], axis=0)
        walls_next = np.stack([state.walls for state in states], axis=0)

        idxs_arange = np.arange(0, len(states))
        agent_next_tmp = self._get_next_idx(agent, actions)
        agent_next = np.zeros(agent_next_tmp.shape, dtype=int)

        boxes_next = boxes.copy()

        # agent -> wall
        agent_wall = walls_next[idxs_arange, agent_next_tmp[:, 0], agent_next_tmp[:, 1]]
        agent_next[agent_wall] = agent[agent_wall]

        # agent -> box
        agent_box = boxes[idxs_arange, agent_next_tmp[:, 0], agent_next_tmp[:, 1]]
        boxes_next_tmp = self._get_next_idx(agent_next_tmp, actions)

        box_wall = walls_next[idxs_arange, boxes_next_tmp[:, 0], boxes_next_tmp[:, 1]]
        box_box = boxes[idxs_arange, boxes_next_tmp[:, 0], boxes_next_tmp[:, 1]]

        # agent -> box -> obstacle
        agent_box_obstacle = agent_box & (box_wall | box_box)
        agent_next[agent_box_obstacle] = agent[agent_box_obstacle]

        # agent -> box -> empty
        agent_box_empty = agent_box & np.logical_not(box_wall | box_box)
        agent_next[agent_box_empty] = agent_next_tmp[agent_box_empty]
        abe_idxs = np.where(agent_box_empty)[0]

        agent_next_idxs_abe = agent_next[agent_box_empty]
        boxes_next_idxs_abe = boxes_next_tmp[agent_box_empty]

        boxes_next[abe_idxs, agent_next_idxs_abe[:, 0], agent_next_idxs_abe[:, 1]] = False
        boxes_next[abe_idxs, boxes_next_idxs_abe[:, 0], boxes_next_idxs_abe[:, 1]] = True

        # agent -> empty
        agent_empty = np.logical_not(agent_wall | agent_box)
        agent_next[agent_empty] = agent_next_tmp[agent_empty]
        boxes_next[agent_empty] = boxes[agent_empty]

        states_next: List[SkState] = []
        for idx in range(len(states)):
            state_next: SkState = SkState(agent_next[idx], boxes_next[idx], walls_next[idx])
            states_next.append(state_next)

        transition_costs: List[float] = [1.0 for _ in range(len(states))]

        return states_next, transition_costs
```
