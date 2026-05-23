---
id: "class:deepxube.base.trainer.TrainArgs"
kind: "class"
name: "TrainArgs"
qualified_name: "deepxube.base.trainer.TrainArgs"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 37
line_end: 59
is_abstract: false
is_dataclass: true
decorators:
  - "@dataclass"
generic_parameters: []
bases: []
methods: []
attributes:
  - name: "batch_size"
    annotation: "int"
    default: null
    from: "class_body"
  - name: "max_itrs"
    annotation: "int"
    default: null
    from: "class_body"
  - name: "balance_steps"
    annotation: "bool"
    default: null
    from: "class_body"
  - name: "rb"
    annotation: "int"
    default: "1"
    from: "class_body"
  - name: "loss_thresh"
    annotation: "float"
    default: "np.inf"
    from: "class_body"
  - name: "targ_up_searches"
    annotation: "int"
    default: "0"
    from: "class_body"
  - name: "skip_heur"
    annotation: "bool"
    default: "False"
    from: "class_body"
  - name: "skip_policy"
    annotation: "bool"
    default: "False"
    from: "class_body"
  - name: "display"
    annotation: "int"
    default: "100"
    from: "class_body"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.trainer.TrainArgs`

**File:** [deepxube/base/trainer.py:37](../../../deepxube/base/trainer.py#L37)
**Abstract:** no
**Dataclass:** yes
**Decorators:** `@dataclass`

## Docstring

:param batch_size: Batch size
:param max_itrs: Maximum number of iterations
:param balance_steps: If true, steps are balanced based on solve percentage
:param rb: amount of data generated from previous updates to keep in replay buffer. Total replay buffer size will
then be train_args.batch_size * up_args.up_gen_itrs * rb.
:param loss_thresh: Loss threshold for updating.
:param targ_up_searches: If > 0, do a greedy search with updater for minimum given number of searches to test
if target network should be updated. Otherwise, it will be updated automatically.
:param display: Number of iterations to display progress when training nnet. No display if 0.
:param skip_heur: Skip training of heuristic function
:param skip_policy: Skip training of policy

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

*(No methods.)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `batch_size` | `int` | class_body |
| `max_itrs` | `int` | class_body |
| `balance_steps` | `bool` | class_body |
| `rb` | `int` | class_body |
| `loss_thresh` | `float` | class_body |
| `targ_up_searches` | `int` | class_body |
| `skip_heur` | `bool` | class_body |
| `skip_policy` | `bool` | class_body |
| `display` | `int` | class_body |

## Source

```python
class TrainArgs:
    """
    :param batch_size: Batch size
    :param max_itrs: Maximum number of iterations
    :param balance_steps: If true, steps are balanced based on solve percentage
    :param rb: amount of data generated from previous updates to keep in replay buffer. Total replay buffer size will
    then be train_args.batch_size * up_args.up_gen_itrs * rb.
    :param loss_thresh: Loss threshold for updating.
    :param targ_up_searches: If > 0, do a greedy search with updater for minimum given number of searches to test
    if target network should be updated. Otherwise, it will be updated automatically.
    :param display: Number of iterations to display progress when training nnet. No display if 0.
    :param skip_heur: Skip training of heuristic function
    :param skip_policy: Skip training of policy
    """
    batch_size: int
    max_itrs: int
    balance_steps: bool
    rb: int = 1
    loss_thresh: float = np.inf
    targ_up_searches: int = 0
    skip_heur: bool = False
    skip_policy: bool = False
    display: int = 100
```
