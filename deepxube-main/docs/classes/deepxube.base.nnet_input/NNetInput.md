---
id: "class:deepxube.base.nnet_input.NNetInput"
kind: "class"
name: "NNetInput"
qualified_name: "deepxube.base.nnet_input.NNetInput"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 26
line_end: 41
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters:
  - "D"
bases:
  - name: "ABC"
    resolved_id: null
  - name: "Generic[D]"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.NNetInput.__init__"
  - "func:deepxube.base.nnet_input.NNetInput.get_input_info"
  - "func:deepxube.base.nnet_input.NNetInput.to_np"
attributes:
  - name: "self.domain"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.NNetInput`

**File:** [deepxube/base/nnet_input.py:26](../../../deepxube/base/nnet_input.py#L26)
**Abstract:** yes
**Generic parameters:** `D`

## Docstring

Abstract base: knows how to describe the network input shape and convert objects to numpy. 

## Inheritance

**Direct bases:**
- `ABC`
- `Generic[D]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*
- `get_input_info` *(trivial, skipped)*
- `to_np` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.domain` | — | __init__ |

## Source

```python
class NNetInput(ABC, Generic[D]):
    """ Abstract base: knows how to describe the network input shape and convert objects to numpy. """

    def __init__(self, domain: D):
        """ Bind to its domain. """
        self.domain: D = domain

    @abstractmethod
    def get_input_info(self) -> Any:
        """ :return: Subclass-specific tuple describing input shapes / one-hot depths. """
        pass

    @abstractmethod
    def to_np(self, *args: Any) -> List[NDArray]:
        """ Convert input objects to a list of numpy arrays (one per network tensor slot). """
        pass
```
