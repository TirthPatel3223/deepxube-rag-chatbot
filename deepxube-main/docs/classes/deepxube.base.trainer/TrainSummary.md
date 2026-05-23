---
id: "class:deepxube.base.trainer.TrainSummary"
kind: "class"
name: "TrainSummary"
qualified_name: "deepxube.base.trainer.TrainSummary"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 167
line_end: 185
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.base.trainer.TrainSummary.__init__"
  - "func:deepxube.base.trainer.TrainSummary.update_pathfindstats"
attributes:
  - name: "self.itr_to_in_out"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.itr_to_steps_to_pathfindstats"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.trainer.TrainSummary`

**File:** [deepxube/base/trainer.py:167](../../../deepxube/base/trainer.py#L167)
**Abstract:** no

## Docstring

Persisted record of per-iteration training summaries (solve rates,
path costs, search iters, mean backups) used by the ``train_summary`` CLI. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*
- `update_pathfindstats`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.itr_to_in_out` | — | __init__ |
| `self.itr_to_steps_to_pathfindstats` | — | __init__ |

## Source

```python
class TrainSummary:
    """ Persisted record of per-iteration training summaries (solve rates,
    path costs, search iters, mean backups) used by the ``train_summary`` CLI. """

    def __init__(self) -> None:
        """ Initialise empty per-iteration record dicts. """
        self.itr_to_in_out: Dict[int, Tuple[NDArray, NDArray]] = dict()
        self.itr_to_steps_to_pathfindstats: Dict[int, Dict[int, Dict]] = dict()

    def update_pathfindstats(self, step_to_pathfindperf: Dict[int, PathFindPerf], itr: int) -> None:
        """ Snapshot per-step solve rate / path cost / search iter / backup stats at training iteration ``itr``. """
        self.itr_to_steps_to_pathfindstats[itr] = dict()
        for step, pathfindperf in step_to_pathfindperf.items():
            self.itr_to_steps_to_pathfindstats[itr][step] = dict()
            self.itr_to_steps_to_pathfindstats[itr][step]["per_solved"] = pathfindperf.per_solved()
            self.itr_to_steps_to_pathfindstats[itr][step]["path_costs"] = pathfindperf.stats()[1]
            self.itr_to_steps_to_pathfindstats[itr][step]["search_itrs"] = pathfindperf.stats()[2]
            self.itr_to_steps_to_pathfindstats[itr][step]["ctgs_backup"] = float(np.mean(pathfindperf.ctgs_bkup))
            self.itr_to_steps_to_pathfindstats[itr][step]["num_instances"] = len(pathfindperf.ctgs_bkup)
```
