---
id: "class:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferV"
kind: "class"
name: "ReplayBufferV"
qualified_name: "deepxube.updaters.utils.replay_buffer_utils.ReplayBufferV"
module: "deepxube.updaters.utils.replay_buffer_utils"
file: "deepxube/updaters/utils/replay_buffer_utils.py"
line_start: 90
line_end: 106
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "ReplayBuffer[ReplayVElem, ReplayVRet]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferV._elems_to_ret"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.utils.replay_buffer_utils.ReplayBufferV`

**File:** [deepxube/updaters/utils/replay_buffer_utils.py:90](../../../deepxube/updaters/utils/replay_buffer_utils.py#L90)
**Abstract:** no

## Docstring

Replay buffer storing ``(state, goal, is_solved)`` triples for V-based
RL.

## Inheritance

**Direct bases:**
- `ReplayBuffer[ReplayVElem, ReplayVRet]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_elems_to_ret`

## Source

```python
class ReplayBufferV(ReplayBuffer[ReplayVElem, ReplayVRet]):
    """ Replay buffer storing ``(state, goal, is_solved)`` triples for V-based
    RL.
    """

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
