---
id: "func:deepxube.base.trainer.Status.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.base.trainer.Status.__init__"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 136
line_end: 154
class: "Status"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "step_max"
    annotation: "int"
    default: null
  - name: "balance_steps"
    annotation: "bool"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [149]
  - target: "func:numpy.ones"
    expr: "np.ones"
    call_sites: [153]
raises: []
reads_attrs:
  - "self.itr"
  - "self.per_solved_best"
  - "self.step_max"
  - "self.step_max_curr"
  - "self.step_probs"
  - "self.targ_update_num"
  - "self.update_num"
writes_attrs:
  - "self.itr"
  - "self.per_solved_best"
  - "self.step_max"
  - "self.step_max_curr"
  - "self.step_probs"
  - "self.targ_update_num"
  - "self.update_num"
---

# `deepxube.base.trainer.Status.__init__`

**File:** [deepxube/base/trainer.py:136](../../../../deepxube/base/trainer.py#L136)
**Class:** `Status`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, step_max: int, balance_steps: bool)
```

## Docstring

Initialise iteration counters and the step distribution.

:param step_max: Maximum number of random-walk steps for problem instances.
:param balance_steps: If True, start with all weight on the very-easy instances and grow ``step_max_curr`` as solve rate rises.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `step_max` | `int` | — |
| `balance_steps` | `bool` | — |

## Returns

*(Not annotated.)*

## Calls

- `np.zeros` → `func:numpy.zeros` (lines: 149)
- `np.ones` → `func:numpy.ones` (lines: 153)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.itr`
- `self.per_solved_best`
- `self.step_max`
- `self.step_max_curr`
- `self.step_probs`
- `self.targ_update_num`
- `self.update_num`

**Reads:**
- `self.itr`
- `self.per_solved_best`
- `self.step_max`
- `self.step_max_curr`
- `self.step_probs`
- `self.targ_update_num`
- `self.update_num`

## Source

```python
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
```
