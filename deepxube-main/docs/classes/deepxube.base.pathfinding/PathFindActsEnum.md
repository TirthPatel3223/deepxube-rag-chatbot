---
id: "class:deepxube.base.pathfinding.PathFindActsEnum"
kind: "class"
name: "PathFindActsEnum"
qualified_name: "deepxube.base.pathfinding.PathFindActsEnum"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 797
line_end: 806
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFind[DActsEnum, FNs, I]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.pathfinding.PathFindActsEnum.expand_states"
  - "func:deepxube.base.pathfinding.PathFindActsEnum.get_state_actions"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.PathFindActsEnum`

**File:** [deepxube/base/pathfinding.py:797](../../../deepxube/base/pathfinding.py#L797)
**Abstract:** yes

## Docstring

Action-source mixin: pulls applicable actions from the domain (``ActsEnum``). 

## Inheritance

**Direct bases:**
- `PathFind[DActsEnum, FNs, I]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `expand_states` *(trivial, skipped)*
- `get_state_actions` *(trivial, skipped)*

## Source

```python
class PathFindActsEnum(PathFind[DActsEnum, FNs, I], ABC):
    """ Action-source mixin: pulls applicable actions from the domain (``ActsEnum``). """

    def expand_states(self, states: List[State], goals: List[Goal]) -> Tuple[List[List[State]], List[List[Action]], List[List[float]]]:
        """ Domain-driven expansion via ``Domain.expand``. """
        return self.domain.expand(states)

    def get_state_actions(self, states: List[State], goals: List[Goal]) -> List[List[Action]]:
        """ :return: All applicable actions per state from the domain. """
        return self.domain.get_state_actions(states)
```
