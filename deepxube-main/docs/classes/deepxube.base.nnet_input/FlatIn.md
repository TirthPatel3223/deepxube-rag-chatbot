---
id: "class:deepxube.base.nnet_input.FlatIn"
kind: "class"
name: "FlatIn"
qualified_name: "deepxube.base.nnet_input.FlatIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 44
line_end: 54
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "NNetInput[D]"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.FlatIn.get_input_info"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.FlatIn`

**File:** [deepxube/base/nnet_input.py:44](../../../deepxube/base/nnet_input.py#L44)
**Abstract:** yes

## Docstring

Marker mixin: the network input is a flat (1-D) vector. 

## Inheritance

**Direct bases:**
- `NNetInput[D]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_input_info` *(trivial, skipped)*

## Source

```python
class FlatIn(NNetInput[D]):
    """ Marker mixin: the network input is a flat (1-D) vector. """

    @abstractmethod
    def get_input_info(self) -> Tuple[List[int], List[int]]:
        """
        :return: A list of dimensions of the arrays given to the neural network (pre one_hot), A list of depths for performing a one_hot representation on
        that corresponding input.
        If 1, then no one_hot is performed.
        """
        pass
```
