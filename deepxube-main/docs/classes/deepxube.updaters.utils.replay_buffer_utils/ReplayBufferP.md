---
id: "class:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP"
kind: "class"
name: "ReplayBufferP"
qualified_name: "deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP"
module: "deepxube.updaters.utils.replay_buffer_utils"
file: "deepxube/updaters/utils/replay_buffer_utils.py"
line_start: 131
line_end: 146
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "ReplayBuffer[ReplayPElem, ReplayPRet]"
    resolved_id: null
methods:
  - "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP._elems_to_ret"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.utils.replay_buffer_utils.ReplayBufferP`

**File:** [deepxube/updaters/utils/replay_buffer_utils.py:131](../../../deepxube/updaters/utils/replay_buffer_utils.py#L131)
**Abstract:** no

## Docstring

Replay buffer storing ``(state, goal, action)`` triples for policy
training.

## Inheritance

**Direct bases:**
- `ReplayBuffer[ReplayPElem, ReplayPRet]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_elems_to_ret`

## Source

```python
class ReplayBufferP(ReplayBuffer[ReplayPElem, ReplayPRet]):
    """ Replay buffer storing ``(state, goal, action)`` triples for policy
    training.
    """

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
