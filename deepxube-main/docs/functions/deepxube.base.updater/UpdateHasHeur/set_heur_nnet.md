---
id: "func:deepxube.base.updater.UpdateHasHeur.set_heur_nnet"
kind: "method"
name: "set_heur_nnet"
qualified_name: "deepxube.base.updater.UpdateHasHeur.set_heur_nnet"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 597
line_end: 599
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
  - name: "heur_nnet"
    annotation: "HNet"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.updater.UpdateHasHeur.add_nnet_par"
    expr: "self.add_nnet_par"
    call_sites: [599]
  - target: "func:deepxube.base.updater.UpdateHasHeur.heur_name"
    expr: "self.heur_name"
    call_sites: [599]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.UpdateHasHeur.set_heur_nnet`

**File:** [deepxube/base/updater.py:597](../../../../deepxube/base/updater.py#L597)
**Class:** `UpdateHasHeur`
**Visibility:** public
**Kind:** method

## Signature

```python
def set_heur_nnet(self, heur_nnet: HNet) -> None
```

## Docstring

Register the heuristic NNet parameter object. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `heur_nnet` | `HNet` | — |

## Returns

`None`

## Calls

- `self.add_nnet_par` → `func:deepxube.base.updater.UpdateHasHeur.add_nnet_par` (lines: 599)
- `self.heur_name` → `func:deepxube.base.updater.UpdateHasHeur.heur_name` (lines: 599)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def set_heur_nnet(self, heur_nnet: HNet) -> None:
        """ Register the heuristic NNet parameter object. """
        self.add_nnet_par(self.heur_name(), heur_nnet)
```
