---
id: "class:deepxube.domains.sokoban.SkNNetInput"
kind: "class"
name: "SkNNetInput"
qualified_name: "deepxube.domains.sokoban.SkNNetInput"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 348
line_end: 365
is_abstract: false
is_dataclass: false
decorators:
  - "@register_nnet_input('sokoban', 'sokoban_nnet_input')"
generic_parameters: []
bases:
  - name: "FlatIn[Sokoban]"
    resolved_id: null
  - name: "StateGoalIn[Sokoban, SkState, SkGoal]"
    resolved_id: null
methods:
  - "func:deepxube.domains.sokoban.SkNNetInput.get_input_info"
  - "func:deepxube.domains.sokoban.SkNNetInput.to_np"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.sokoban.SkNNetInput`

**File:** [deepxube/domains/sokoban.py:348](../../../deepxube/domains/sokoban.py#L348)
**Abstract:** no
**Decorators:** `@register_nnet_input('sokoban', 'sokoban_nnet_input')`

## Docstring

Flat NNet input for Sokoban: stacks walls, boxes, agent, and targets into a 400-element vector. 

## Inheritance

**Direct bases:**
- `FlatIn[Sokoban]`
- `StateGoalIn[Sokoban, SkState, SkGoal]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_input_info` *(trivial, skipped)* — *(no docstring)*
- `to_np`

## Source

```python
class SkNNetInput(FlatIn[Sokoban], StateGoalIn[Sokoban, SkState, SkGoal]):
    """ Flat NNet input for Sokoban: stacks walls, boxes, agent, and targets into a 400-element vector. """

    def get_input_info(self) -> Tuple[List[int], List[int]]:
        return [400], [1]

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
