---
id: "class:deepxube.base.domain.ActsRev"
kind: "class"
name: "ActsRev"
qualified_name: "deepxube.base.domain.ActsRev"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 223
line_end: 235
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.ActsRev.rev_action"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.ActsRev`

**File:** [deepxube/base/domain.py:223](../../../deepxube/base/domain.py#L223)
**Abstract:** yes

## Docstring

Actions are reversible.

    

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `rev_action` *(trivial, skipped)*

## Source

```python
class ActsRev(Domain[S, A, G], ABC):
    """ Actions are reversible.

    """
    @abstractmethod
    def rev_action(self, states: List[S], actions: List[A]) -> List[A]:
        """ Get the reverse of the given action

        :param states: List of states
        :param actions: List of actions
        :return: Reverse of given action in the given state
        """
        pass
```
