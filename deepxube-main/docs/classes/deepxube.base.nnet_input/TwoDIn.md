---
id: "class:deepxube.base.nnet_input.TwoDIn"
kind: "class"
name: "TwoDIn"
qualified_name: "deepxube.base.nnet_input.TwoDIn"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 57
line_end: 67
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "NNetInput[D]"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.TwoDIn.get_input_info"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.TwoDIn`

**File:** [deepxube/base/nnet_input.py:57](../../../deepxube/base/nnet_input.py#L57)
**Abstract:** yes

## Docstring

Marker mixin: the network input is a (channels, height, width) tensor. 

## Inheritance

**Direct bases:**
- `NNetInput[D]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_input_info` *(trivial, skipped)*

## Source

```python
class TwoDIn(NNetInput[D]):
    """ Marker mixin: the network input is a (channels, height, width) tensor. """

    @abstractmethod
    def get_input_info(self) -> Tuple[List[int], Tuple[int, int], List[int], Optional[int]]:
        """
        :return: A list of channels of the arrays given to the neural network (pre one_hot), (height, width),
        a list of depths for performing a one_hot representation on that corresponding input, optional 1x1 conv channel out for qfix.
        The one_hot is applied to the channel dimension. If 1, then no one_hot is performed.
        """
        pass
```
