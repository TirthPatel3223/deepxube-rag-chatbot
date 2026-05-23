---
id: "class:deepxube.base.trainer.Status"
kind: "class"
name: "Status"
qualified_name: "deepxube.base.trainer.Status"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 132
line_end: 164
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.base.trainer.Status.__init__"
  - "func:deepxube.base.trainer.Status.update_step_probs"
attributes:
  - name: "self.itr"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.per_solved_best"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.step_max"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.step_max_curr"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.step_probs"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.targ_update_num"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.update_num"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.trainer.Status`

**File:** [deepxube/base/trainer.py:132](../../../deepxube/base/trainer.py#L132)
**Abstract:** no

## Docstring

Persistent training status: iteration counters, target-update counters,
and the per-step sampling distribution used by the updater. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `update_step_probs`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.itr` | — | __init__ |
| `self.per_solved_best` | — | __init__ |
| `self.step_max` | — | __init__ |
| `self.step_max_curr` | — | __init__ |
| `self.step_probs` | — | __init__ |
| `self.targ_update_num` | — | __init__ |
| `self.update_num` | — | __init__ |

## Source

```python
class Status:
    """ Persistent training status: iteration counters, target-update counters,
    and the per-step sampling distribution used by the updater. """

    def __init__(self, step_max: int, balance_steps: bool):
        """ Initialise iteration counters and the step distribution.

        :param step_max: Maximum number of random-walk steps for problem instances.
        :param balance_steps: If True, start with all weight on the very-easy instances and grow ``step_max_curr`` as solve rate rises.
        """
        self.itr: int = 0
        self.update_num: int = 0
        self.targ_update_num: int = 0
        self.step_max: int = step_max
        self.step_probs: NDArray
        self.step_max_curr: int = 1
        if balance_steps:
            self.step_probs = np.zeros(self.step_max + 1)
            self.step_probs[0:2] = 0.5
            self.step_probs[2:] = 0
        else:
            self.step_probs = np.ones(self.step_max + 1)/(self.step_max + 1)
        self.per_solved_best: float = 0.0

    def update_step_probs(self, step_to_search_perf: Dict[int, PathFindPerf]) -> None:
        """ Adapt the step-count sampling distribution based on the latest solve rate. """
        ave_solve: float = float(np.mean([step_to_search_perf[step].per_solved()
                                          for step in step_to_search_perf.keys()]))
        if ave_solve >= 50.0:
            self.step_max_curr = min(self.step_max_curr * 2, self.step_max)

        self.step_probs = np.zeros(self.step_max + 1)
        self.step_probs[np.arange(0, self.step_max_curr + 1)] = 1 / (self.step_max_curr + 1)
```
