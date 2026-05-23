---
id: "class:deepxube.base.updater.UpdateRL"
kind: "class"
name: "UpdateRL"
qualified_name: "deepxube.base.updater.UpdateRL"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 683
line_end: 694
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Update[D, FNs, P, Inst]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.updater.UpdateRL._make_instances"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.updater.UpdateRL`

**File:** [deepxube/base/updater.py:683](../../../deepxube/base/updater.py#L683)
**Abstract:** yes

## Docstring

Reinforcement-learning updater base: builds problem instances by
sampling start/goal pairs from the domain (not random walks). 

## Inheritance

**Direct bases:**
- `Update[D, FNs, P, Inst]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_make_instances`

## Source

```python
class UpdateRL(Update[D, FNs, P, Inst], ABC):
    """ Reinforcement-learning updater base: builds problem instances by
    sampling start/goal pairs from the domain (not random walks). """

    def _make_instances(self, pathfind: P, steps_gen: List[int], inst_infos: List[Any], times: Times) -> List[Inst]:
        """ Sample start states and goals from the domain, then hand them to the pathfinder. """
        # get states/goals
        times_states: Times = Times()
        states_gen, goals_gen = self.domain.sample_problem_instances(steps_gen, times=times_states)
        times.add_times(times_states, ["get_states"])

        return pathfind.make_instances(states_gen, goals_gen, inst_infos=inst_infos, compute_root_vals=False)
```
