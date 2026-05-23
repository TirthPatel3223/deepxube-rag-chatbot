---
id: "class:deepxube.base.domain.State"
kind: "class"
name: "State"
qualified_name: "deepxube.base.domain.State"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 25
line_end: 43
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.State.__hash__"
  - "func:deepxube.base.domain.State.__eq__"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.State`

**File:** [deepxube/base/domain.py:25](../../../deepxube/base/domain.py#L25)
**Abstract:** yes

## Docstring

State object

    

## Inheritance

**Direct bases:**
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__hash__` *(trivial, skipped)*
- `__eq__` *(trivial, skipped)*

## Source

```python
class State(ABC):
    """ State object

    """
    @abstractmethod
    def __hash__(self) -> int:
        """ For use in CLOSED dictionary for pathfinding
        :return: hash value
        """
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """ for use in state reidentification during pathfinding

        :param other: other state
        :return: true if they are equal
        """
        pass
```
