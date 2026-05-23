---
id: "func:deepxube.base.updater.UpdateHasHeur.set_heur_file"
kind: "method"
name: "set_heur_file"
qualified_name: "deepxube.base.updater.UpdateHasHeur.set_heur_file"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 601
line_end: 603
class: "UpdateHasHeur"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "heur_file"
    annotation: "str"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.updater.UpdateHasHeur.set_nnet_file"
    expr: "self.set_nnet_file"
    call_sites: [603]
  - target: "func:deepxube.base.updater.UpdateHasHeur.heur_name"
    expr: "self.heur_name"
    call_sites: [603]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.UpdateHasHeur.set_heur_file`

**File:** [deepxube/base/updater.py:601](../../../../deepxube/base/updater.py#L601)
**Class:** `UpdateHasHeur`
**Visibility:** public
**Kind:** method

## Signature

```python
def set_heur_file(self, heur_file: str) -> None
```

## Docstring

Record the heuristic network's checkpoint path. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `heur_file` | `str` | — |

## Returns

`None`

## Calls

- `self.set_nnet_file` → `func:deepxube.base.updater.UpdateHasHeur.set_nnet_file` (lines: 603)
- `self.heur_name` → `func:deepxube.base.updater.UpdateHasHeur.heur_name` (lines: 603)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def set_heur_file(self, heur_file: str) -> None:
        """ Record the heuristic network's checkpoint path. """
        self.set_nnet_file(self.heur_name(), heur_file)
```
