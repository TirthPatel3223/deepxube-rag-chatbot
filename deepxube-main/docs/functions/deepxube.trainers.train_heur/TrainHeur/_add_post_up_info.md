---
id: "func:deepxube.trainers.train_heur.TrainHeur._add_post_up_info"
kind: "method"
name: "_add_post_up_info"
qualified_name: "deepxube.trainers.train_heur.TrainHeur._add_post_up_info"
module: "deepxube.trainers.train_heur"
file: "deepxube/trainers/train_heur.py"
line_start: 43
line_end: 49
class: "TrainHeur"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "List[str]"
docstring_source: "present"
callees:
  - target: "func:deepxube.trainers.utils.train_utils.ctgs_summary"
    expr: "ctgs_summary"
    call_sites: [45]
  - target: null
    expr: "self.writer.add_scalar"
    call_sites: [46, 47, 48]
raises: []
reads_attrs:
  - "self.db"
  - "self.status"
  - "self.writer"
writes_attrs: []
---

# `deepxube.trainers.train_heur.TrainHeur._add_post_up_info`

**File:** [deepxube/trainers/train_heur.py:43](../../../../deepxube/trainers/train_heur.py#L43)
**Class:** `TrainHeur`
**Visibility:** private
**Kind:** method

## Signature

```python
def _add_post_up_info(self) -> List[str]
```

## Docstring

:return: Summary strings for cost-to-go mean/min/max from the latest data-generation update. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`List[str]`

## Calls

- `ctgs_summary` → `func:deepxube.trainers.utils.train_utils.ctgs_summary` (lines: 45)

### Unresolved
- `self.writer.add_scalar` (lines: 46, 47, 48)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.db`
- `self.status`
- `self.writer`

## Source

```python
    def _add_post_up_info(self) -> List[str]:
        """ :return: Summary strings for cost-to-go mean/min/max from the latest data-generation update. """
        ctgs_mean, ctgs_min, ctgs_max = ctgs_summary([self.db.arrays[-1]])
        self.writer.add_scalar("train/ctgs/mean", ctgs_mean, self.status.itr)
        self.writer.add_scalar("train/ctgs/min", ctgs_min, self.status.itr)
        self.writer.add_scalar("train/ctgs/max", ctgs_max, self.status.itr)
        return [f"cost-to-go (mean/min/max): {ctgs_mean:.2f}/{ctgs_min:.2f}/{ctgs_max:.2f}"]
```
