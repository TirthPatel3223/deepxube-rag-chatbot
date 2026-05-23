---
id: "class:deepxube.base.nnet_input.FlatInPolicy"
kind: "class"
name: "FlatInPolicy"
qualified_name: "deepxube.base.nnet_input.FlatInPolicy"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 121
line_end: 123
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "FlatIn[D]"
    resolved_id: null
  - name: "PolicyNNetIn[D, S, G, A]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods: []
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.FlatInPolicy`

**File:** [deepxube/base/nnet_input.py:121](../../../deepxube/base/nnet_input.py#L121)
**Abstract:** yes

## Docstring

Combination of ``FlatIn`` and ``PolicyNNetIn`` for flat-input policy networks. 

## Inheritance

**Direct bases:**
- `FlatIn[D]`
- `PolicyNNetIn[D, S, G, A]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

*(No methods.)*

## Source

```python
class FlatInPolicy(FlatIn[D], PolicyNNetIn[D, S, G, A], ABC):
    """ Combination of ``FlatIn`` and ``PolicyNNetIn`` for flat-input policy networks. """
    pass
```
