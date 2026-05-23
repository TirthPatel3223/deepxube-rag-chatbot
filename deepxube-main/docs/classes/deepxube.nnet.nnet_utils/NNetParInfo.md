---
id: "class:deepxube.nnet.nnet_utils.NNetParInfo"
kind: "class"
name: "NNetParInfo"
qualified_name: "deepxube.nnet.nnet_utils.NNetParInfo"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 126
line_end: 130
is_abstract: false
is_dataclass: true
decorators:
  - "@dataclass"
generic_parameters: []
bases: []
methods: []
attributes:
  - name: "nnet_i_q"
    annotation: "Queue"
    default: null
    from: "class_body"
  - name: "nnet_o_q"
    annotation: "Queue"
    default: null
    from: "class_body"
  - name: "proc_id"
    annotation: "int"
    default: null
    from: "class_body"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.nnet.nnet_utils.NNetParInfo`

**File:** [deepxube/nnet/nnet_utils.py:126](../../../deepxube/nnet/nnet_utils.py#L126)
**Abstract:** no
**Dataclass:** yes
**Decorators:** `@dataclass`

## Docstring

Routing info for a single parallel nnet worker: shared input queue, dedicated output queue, and process ID. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

*(No methods.)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `nnet_i_q` | `Queue` | class_body |
| `nnet_o_q` | `Queue` | class_body |
| `proc_id` | `int` | class_body |

## Source

```python
class NNetParInfo:
    """ Routing info for a single parallel nnet worker: shared input queue, dedicated output queue, and process ID. """
    nnet_i_q: Queue
    nnet_o_q: Queue
    proc_id: int
```
