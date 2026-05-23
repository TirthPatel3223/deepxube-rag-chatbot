---
id: "class:deepxube.base.domain.ActsEnumFixed"
kind: "class"
name: "ActsEnumFixed"
qualified_name: "deepxube.base.domain.ActsEnumFixed"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 293
line_end: 312
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "ActsEnum[S, A, G]"
    resolved_id: null
  - name: "ActsFixed[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.ActsEnumFixed.sample_action"
  - "func:deepxube.base.domain.ActsEnumFixed.get_state_actions"
  - "func:deepxube.base.domain.ActsEnumFixed.get_actions_fixed"
  - "func:deepxube.base.domain.ActsEnumFixed.get_num_acts"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.ActsEnumFixed`

**File:** [deepxube/base/domain.py:293](../../../deepxube/base/domain.py#L293)
**Abstract:** yes

## Docstring

Action mixin: every state shares the same fixed action list. 

## Inheritance

**Direct bases:**
- `ActsEnum[S, A, G]`
- `ActsFixed[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `sample_action`
- `get_state_actions`
- `get_actions_fixed` *(trivial, skipped)*
- `get_num_acts`

## Source

```python
class ActsEnumFixed(ActsEnum[S, A, G], ActsFixed[S, A, G]):
    """ Action mixin: every state shares the same fixed action list. """

    def sample_action(self, num: int) -> List[A]:
        """ :return: ``num`` actions sampled uniformly from the fixed action list. """
        actions_fixed: List[A] = self.get_actions_fixed()
        return [random.choice(actions_fixed) for _ in range(num)]

    def get_state_actions(self, states: List[S]) -> List[List[A]]:
        """ :return: A copy of the fixed action list for every input state. """
        return [self.get_actions_fixed().copy() for _ in range(len(states))]

    @abstractmethod
    def get_actions_fixed(self) -> List[A]:
        """ :return: The fixed action list for this domain. """
        pass

    def get_num_acts(self) -> int:
        """ :return: Number of fixed actions. """
        return len(self.get_actions_fixed())
```
