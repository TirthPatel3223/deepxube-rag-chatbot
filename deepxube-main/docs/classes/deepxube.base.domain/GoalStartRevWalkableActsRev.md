---
id: "class:deepxube.base.domain.GoalStartRevWalkableActsRev"
kind: "class"
name: "GoalStartRevWalkableActsRev"
qualified_name: "deepxube.base.domain.GoalStartRevWalkableActsRev"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 472
line_end: 477
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "GoalStartRevWalkable[S, A, G]"
    resolved_id: null
  - name: "ActsRev[S, A, G]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.GoalStartRevWalkableActsRev.random_walk_rev"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.GoalStartRevWalkableActsRev`

**File:** [deepxube/base/domain.py:472](../../../deepxube/base/domain.py#L472)
**Abstract:** yes

## Docstring

Reverse-walk variant for domains whose actions are reversible: a forward random walk on the reversible domain is equivalent to a reverse walk. 

## Inheritance

**Direct bases:**
- `GoalStartRevWalkable[S, A, G]`
- `ActsRev[S, A, G]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `random_walk_rev`

## Source

```python
class GoalStartRevWalkableActsRev(GoalStartRevWalkable[S, A, G], ActsRev[S, A, G], ABC):
    """ Reverse-walk variant for domains whose actions are reversible: a forward random walk on the reversible domain is equivalent to a reverse walk. """

    def random_walk_rev(self, states: List[S], num_steps_l: List[int]) -> List[S]:
        """ Forward random walk that doubles as a reverse walk via action reversibility. """
        return self.random_walk(states, num_steps_l)[0]
```
