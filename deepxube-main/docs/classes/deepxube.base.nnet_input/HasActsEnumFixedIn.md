---
id: "class:deepxube.base.nnet_input.HasActsEnumFixedIn"
kind: "class"
name: "HasActsEnumFixedIn"
qualified_name: "deepxube.base.nnet_input.HasActsEnumFixedIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 190
line_end: 196
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.HasActsEnumFixedIn.actions_to_indices"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.HasActsEnumFixedIn`

**File:** [deepxube/base/nnet_input.py:190](../../../deepxube/base/nnet_input.py#L190)
**Abstract:** yes

## Docstring

Mixin for domains whose actions can be mapped to a fixed integer index. 

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `actions_to_indices` *(trivial, skipped)*

## Source

```python
class HasActsEnumFixedIn(Domain[S, A, G]):
    """ Mixin for domains whose actions can be mapped to a fixed integer index. """

    @abstractmethod
    def actions_to_indices(self, actions: List[A]) -> List[int]:
        """ :return: Integer index of each action in the fixed action list. """
        pass
```
