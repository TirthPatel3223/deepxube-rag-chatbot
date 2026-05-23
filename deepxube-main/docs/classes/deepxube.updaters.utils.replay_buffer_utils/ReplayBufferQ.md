---
id: "class:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ"
kind: "class"
name: "ReplayBufferQ"
qualified_name: "deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ"
module: "deepxube.updaters.utils.replay_buffer_utils"
file: "deepxube/updaters/utils/replay_buffer_utils.py"
line_start: 109
line_end: 128
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "ReplayBuffer[ReplayQElem, ReplayQRet]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ._elems_to_ret"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.utils.replay_buffer_utils.ReplayBufferQ`

**File:** [deepxube/updaters/utils/replay_buffer_utils.py:109](../../../deepxube/updaters/utils/replay_buffer_utils.py#L109)
**Abstract:** no

## Docstring

Replay buffer storing
``(state, goal, is_solved, action, tc, next_state)`` six-tuples for
Q-learning.

## Inheritance

**Direct bases:**
- `ReplayBuffer[ReplayQElem, ReplayQRet]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_elems_to_ret`

## Source

```python
class ReplayBufferQ(ReplayBuffer[ReplayQElem, ReplayQRet]):
    """ Replay buffer storing
    ``(state, goal, is_solved, action, tc, next_state)`` six-tuples for
    Q-learning.
    """

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
