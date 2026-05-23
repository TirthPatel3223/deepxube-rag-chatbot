---
id: "func:deepxube.trainers.utils.train_loop.get_curr_update_num"
kind: "function"
name: "get_curr_update_num"
qualified_name: "deepxube.trainers.utils.train_loop.get_curr_update_num"
module: "deepxube.trainers.utils.train_loop"
file: "deepxube/trainers/utils/train_loop.py"
line_start: 55
line_end: 61
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "train_heur"
    annotation: "Optional[TrainHeur]"
    default: null
  - name: "train_policy"
    annotation: "Optional[TrainPolicy]"
    default: null
returns: "int"
docstring_source: "present"
callees: []
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.trainers.utils.train_loop.get_curr_update_num`

**File:** [deepxube/trainers/utils/train_loop.py:55](../../../../deepxube/trainers/utils/train_loop.py#L55)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_curr_update_num(train_heur: Optional[TrainHeur], train_policy: Optional[TrainPolicy]) -> int
```

## Docstring

:return: Current update number from whichever trainer is active. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `train_heur` | `Optional[TrainHeur]` | — |
| `train_policy` | `Optional[TrainPolicy]` | — |

## Returns

`int`

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_curr_update_num(train_heur: Optional[TrainHeur], train_policy: Optional[TrainPolicy]) -> int:
    """ :return: Current update number from whichever trainer is active. """
    if train_policy is not None:
        return train_policy.status.update_num
    else:
        assert train_heur is not None
        return train_heur.status.update_num
```
