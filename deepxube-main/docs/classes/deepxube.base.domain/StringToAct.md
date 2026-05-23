---
id: "class:deepxube.base.domain.StringToAct"
kind: "class"
name: "StringToAct"
qualified_name: "deepxube.base.domain.StringToAct"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 189
line_end: 206
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.StringToAct.string_to_action"
  - "func:deepxube.base.domain.StringToAct.string_to_action_help"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.StringToAct`

**File:** [deepxube/base/domain.py:189](../../../deepxube/base/domain.py#L189)
**Abstract:** yes

## Docstring

Can get an action from a string. Used when visualizing problem instances.

    

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `string_to_action` *(trivial, skipped)*
- `string_to_action_help` *(trivial, skipped)*

## Source

```python
class StringToAct(Domain[S, A, G]):
    """ Can get an action from a string. Used when visualizing problem instances.

    """
    @abstractmethod
    def string_to_action(self, act_str: str) -> Optional[A]:
        """
        :param act_str: A string representation of an action
        :return: The action represented by the string, if it is a valid representation, None otherwise
        """
        pass

    @abstractmethod
    def string_to_action_help(self) -> str:
        """
        :return: A description of how actions are represented as strings
        """
        pass
```
