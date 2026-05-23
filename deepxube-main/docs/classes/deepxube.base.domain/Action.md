---
id: "class:deepxube.base.domain.Action"
kind: "class"
name: "Action"
qualified_name: "deepxube.base.domain.Action"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 46
line_end: 65
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.Action.__hash__"
  - "func:deepxube.base.domain.Action.__eq__"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.Action`

**File:** [deepxube/base/domain.py:46](../../../deepxube/base/domain.py#L46)
**Abstract:** yes

## Docstring

Action object

    

## Inheritance

**Direct bases:**
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__hash__` *(trivial, skipped)*
- `__eq__` *(trivial, skipped)*

## Source

```python
class Action(ABC):
    """ Action object

    """

    @abstractmethod
    def __hash__(self) -> int:
        """ For use in backup for Q* search
        :return: hash value
        """
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """ for use in backup for Q* search

        :param other: other state
        :return: true if they are equal
        """
        pass
```
