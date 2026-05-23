---
id: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferV._elems_to_ret"
kind: "method"
name: "_elems_to_ret"
qualified_name: "deepxube.updaters.utils.replay_buffer_utils.ReplayBufferV._elems_to_ret"
module: "deepxube.updaters.utils.replay_buffer_utils"
file: "deepxube/updaters/utils/replay_buffer_utils.py"
line_start: 95
line_end: 106
class: "ReplayBufferV"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "elems"
    annotation: "List[ReplayVElem]"
    default: null
returns: "ReplayVRet"
docstring_source: "present"
callees: []
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.utils.replay_buffer_utils.ReplayBufferV._elems_to_ret`

**File:** [deepxube/updaters/utils/replay_buffer_utils.py:95](../../../../deepxube/updaters/utils/replay_buffer_utils.py#L95)
**Class:** `ReplayBufferV`
**Visibility:** private
**Kind:** method

## Signature

```python
def _elems_to_ret(self, elems: List[ReplayVElem]) -> ReplayVRet
```

## Docstring

Unpack ``(state, goal, is_solved)`` tuples into three parallel
lists.

:param elems: Sampled triples.
:return: ``(states, goals, is_solved_l)``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `elems` | `List[ReplayVElem]` | — |

## Returns

`ReplayVRet`

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _elems_to_ret(self, elems: List[ReplayVElem]) -> ReplayVRet:
        """ Unpack ``(state, goal, is_solved)`` tuples into three parallel
        lists.

        :param elems: Sampled triples.
        :return: ``(states, goals, is_solved_l)``.
        """
        states: List[State] = [replay_q_elem[0] for replay_q_elem in elems]
        goals: List[Goal] = [replay_q_elem[1] for replay_q_elem in elems]
        is_solved_l: List[bool] = [replay_q_elem[2] for replay_q_elem in elems]

        return states, goals, is_solved_l
```
