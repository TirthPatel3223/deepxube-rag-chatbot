---
id: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP._elems_to_ret"
kind: "method"
name: "_elems_to_ret"
qualified_name: "deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP._elems_to_ret"
module: "deepxube.updaters.utils.replay_buffer_utils"
file: "deepxube/updaters/utils/replay_buffer_utils.py"
line_start: 136
line_end: 146
class: "ReplayBufferP"
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
    annotation: "List[ReplayPElem]"
    default: null
returns: "ReplayPRet"
docstring_source: "present"
callees: []
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP._elems_to_ret`

**File:** [deepxube/updaters/utils/replay_buffer_utils.py:136](../../../../deepxube/updaters/utils/replay_buffer_utils.py#L136)
**Class:** `ReplayBufferP`
**Visibility:** private
**Kind:** method

## Signature

```python
def _elems_to_ret(self, elems: List[ReplayPElem]) -> ReplayPRet
```

## Docstring

Unpack ``(state, goal, action)`` tuples into three parallel lists.

:param elems: Sampled triples.
:return: ``(states, goals, actions)``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `elems` | `List[ReplayPElem]` | — |

## Returns

`ReplayPRet`

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _elems_to_ret(self, elems: List[ReplayPElem]) -> ReplayPRet:
        """ Unpack ``(state, goal, action)`` tuples into three parallel lists.

        :param elems: Sampled triples.
        :return: ``(states, goals, actions)``.
        """
        states: List[State] = [replay_q_elem[0] for replay_q_elem in elems]
        goals: List[Goal] = [replay_q_elem[1] for replay_q_elem in elems]
        actions: List[Action] = [replay_q_elem[2] for replay_q_elem in elems]

        return states, goals, actions
```
