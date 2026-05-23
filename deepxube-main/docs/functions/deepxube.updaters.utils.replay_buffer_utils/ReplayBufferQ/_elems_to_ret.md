---
id: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ._elems_to_ret"
kind: "method"
name: "_elems_to_ret"
qualified_name: "deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ._elems_to_ret"
module: "deepxube.updaters.utils.replay_buffer_utils"
file: "deepxube/updaters/utils/replay_buffer_utils.py"
line_start: 115
line_end: 128
class: "ReplayBufferQ"
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
    annotation: "List[ReplayQElem]"
    default: null
returns: "ReplayQRet"
docstring_source: "present"
callees: []
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ._elems_to_ret`

**File:** [deepxube/updaters/utils/replay_buffer_utils.py:115](../../../../deepxube/updaters/utils/replay_buffer_utils.py#L115)
**Class:** `ReplayBufferQ`
**Visibility:** private
**Kind:** method

## Signature

```python
def _elems_to_ret(self, elems: List[ReplayQElem]) -> ReplayQRet
```

## Docstring

Unpack the six-tuples into six parallel lists.

:param elems: Sampled six-tuples.
:return: ``(states, goals, is_solved_l, actions, tcs, states_next)``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `elems` | `List[ReplayQElem]` | — |

## Returns

`ReplayQRet`

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _elems_to_ret(self, elems: List[ReplayQElem]) -> ReplayQRet:
        """ Unpack the six-tuples into six parallel lists.

        :param elems: Sampled six-tuples.
        :return: ``(states, goals, is_solved_l, actions, tcs, states_next)``.
        """
        states: List[State] = [replay_q_elem[0] for replay_q_elem in elems]
        goals: List[Goal] = [replay_q_elem[1] for replay_q_elem in elems]
        is_solved_l: List[bool] = [replay_q_elem[2] for replay_q_elem in elems]
        actions: List[Action] = [replay_q_elem[3] for replay_q_elem in elems]
        tcs: List[float] = [replay_q_elem[4] for replay_q_elem in elems]
        states_next: List[State] = [replay_q_elem[5] for replay_q_elem in elems]

        return states, goals, is_solved_l, actions, tcs, states_next
```
