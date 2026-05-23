---
id: "func:deepxube.base.updater.UpdateHasHeur.get_heur_nnet_par"
kind: "method"
name: "get_heur_nnet_par"
qualified_name: "deepxube.base.updater.UpdateHasHeur.get_heur_nnet_par"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 605
line_end: 607
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
returns: "HNet"
docstring_source: "present"
callees:
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [607]
  - target: "func:deepxube.base.updater.UpdateHasHeur.heur_name"
    expr: "self.heur_name"
    call_sites: [607]
raises: []
reads_attrs:
  - "self.nnet_par_dict"
writes_attrs: []
---

# `deepxube.base.updater.UpdateHasHeur.get_heur_nnet_par`

**File:** [deepxube/base/updater.py:605](../../../../deepxube/base/updater.py#L605)
**Class:** `UpdateHasHeur`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_heur_nnet_par(self) -> HNet
```

## Docstring

:return: Registered heuristic NNet parameter object. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`HNet`

## Calls

- `cast` → `func:typing.cast` (lines: 607)
- `self.heur_name` → `func:deepxube.base.updater.UpdateHasHeur.heur_name` (lines: 607)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.nnet_par_dict`

## Source

```python
    def get_heur_nnet_par(self) -> HNet:
        """ :return: Registered heuristic NNet parameter object. """
        return cast(HNet, self.nnet_par_dict[self.heur_name()])
```
