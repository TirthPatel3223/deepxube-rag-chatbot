---
id: "class:deepxube.base.updater.UpArgs"
kind: "class"
name: "UpArgs"
qualified_name: "deepxube.base.updater.UpArgs"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 44
line_end: 79
is_abstract: false
is_dataclass: true
decorators:
  - "@dataclass"
generic_parameters: []
bases: []
methods:
  - "func:deepxube.base.updater.UpArgs.get_up_gen_itrs"
attributes:
  - name: "procs"
    annotation: "int"
    default: null
    from: "class_body"
  - name: "up_itrs"
    annotation: "int"
    default: null
    from: "class_body"
  - name: "step_max"
    annotation: "int"
    default: null
    from: "class_body"
  - name: "search_itrs"
    annotation: "int"
    default: null
    from: "class_body"
  - name: "ub_heur_solns"
    annotation: "bool"
    default: "False"
    from: "class_body"
  - name: "backup"
    annotation: "int"
    default: "1"
    from: "class_body"
  - name: "policy_rand_prob"
    annotation: "float"
    default: "0.0"
    from: "class_body"
  - name: "up_gen_itrs"
    annotation: "Optional[int]"
    default: "None"
    from: "class_body"
  - name: "up_batch_size"
    annotation: "Optional[int]"
    default: "None"
    from: "class_body"
  - name: "nnet_batch_size"
    annotation: "Optional[int]"
    default: "None"
    from: "class_body"
  - name: "sync_main"
    annotation: "bool"
    default: "False"
    from: "class_body"
  - name: "v"
    annotation: "bool"
    default: "False"
    from: "class_body"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.updater.UpArgs`

**File:** [deepxube/base/updater.py:44](../../../deepxube/base/updater.py#L44)
**Abstract:** no
**Dataclass:** yes
**Decorators:** `@dataclass`

## Docstring

Each time an instance is solved, a new one is created with the same number of steps to maintain training data
balance.

:param procs: Number of parallel workers used to compute update
:param up_itrs: How many iterations worth of training instances to obtain for each update
:param step_max: Maximum number of steps to take when generating problem instances.
:param search_itrs: Maximum number of pathfinding iterationos to take for each generated problem instances
States and corresponding goals seen during search will be added to training instances.
:param ub_heur_solns: if True, the target cost-to-go will be min(backup, path_cost_from_state)
:param backup: 1 is Bellman and -1 is tree backup (i.e. Limited Horizon Bellman-based Learning)
:param policy_rand_prob: Probability of sampling random actions for training policy (to prevent mode collapse)
:param up_gen_itrs: How many iterations worth of data to generate per udpate. If None, set to up_itrs
:param up_batch_size: Maximum number of searches to do at a time. Helps manage memory.
Decrease if memory is running out during updater. None if as large as possible
:param nnet_batch_size: Batch size of each nnet used for each process updater. Make smaller if running out
of memory. None if as large as possible.
:param v: True if update is verbose.
:param sync_main: if True, number of processes can affect order in which data is seen

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_up_gen_itrs` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `procs` | `int` | class_body |
| `up_itrs` | `int` | class_body |
| `step_max` | `int` | class_body |
| `search_itrs` | `int` | class_body |
| `ub_heur_solns` | `bool` | class_body |
| `backup` | `int` | class_body |
| `policy_rand_prob` | `float` | class_body |
| `up_gen_itrs` | `Optional[int]` | class_body |
| `up_batch_size` | `Optional[int]` | class_body |
| `nnet_batch_size` | `Optional[int]` | class_body |
| `sync_main` | `bool` | class_body |
| `v` | `bool` | class_body |

## Source

```python
class UpArgs:
    """ Each time an instance is solved, a new one is created with the same number of steps to maintain training data
    balance.

    :param procs: Number of parallel workers used to compute update
    :param up_itrs: How many iterations worth of training instances to obtain for each update
    :param step_max: Maximum number of steps to take when generating problem instances.
    :param search_itrs: Maximum number of pathfinding iterationos to take for each generated problem instances
    States and corresponding goals seen during search will be added to training instances.
    :param ub_heur_solns: if True, the target cost-to-go will be min(backup, path_cost_from_state)
    :param backup: 1 is Bellman and -1 is tree backup (i.e. Limited Horizon Bellman-based Learning)
    :param policy_rand_prob: Probability of sampling random actions for training policy (to prevent mode collapse)
    :param up_gen_itrs: How many iterations worth of data to generate per udpate. If None, set to up_itrs
    :param up_batch_size: Maximum number of searches to do at a time. Helps manage memory.
    Decrease if memory is running out during updater. None if as large as possible
    :param nnet_batch_size: Batch size of each nnet used for each process updater. Make smaller if running out
    of memory. None if as large as possible.
    :param v: True if update is verbose.
    :param sync_main: if True, number of processes can affect order in which data is seen
    """
    procs: int
    up_itrs: int
    step_max: int
    search_itrs: int
    ub_heur_solns: bool = False
    backup: int = 1
    policy_rand_prob: float = 0.0
    up_gen_itrs: Optional[int] = None
    up_batch_size: Optional[int] = None
    nnet_batch_size: Optional[int] = None
    sync_main: bool = False
    v: bool = False

    def get_up_gen_itrs(self) -> int:
        """ Return ``up_gen_itrs`` if set, else fall back to ``up_itrs``. """
        return self.up_itrs if (self.up_gen_itrs is None) else self.up_gen_itrs
```
