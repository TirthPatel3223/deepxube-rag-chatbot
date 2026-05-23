---
id: "func:deepxube.base.updater.UpdateHeur._get_targ_heur_fn"
kind: "method"
name: "_get_targ_heur_fn"
qualified_name: "deepxube.base.updater.UpdateHeur._get_targ_heur_fn"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 713
line_end: 715
class: "UpdateHeur"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "H"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.updater.UpdateHeur._get_heur_fn_from_dict"
    expr: "self._get_heur_fn_from_dict"
    call_sites: [715]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.UpdateHeur._get_targ_heur_fn`

**File:** [deepxube/base/updater.py:713](../../../../deepxube/base/updater.py#L713)
**Class:** `UpdateHeur`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_targ_heur_fn(self) -> H
```

## Docstring

:return: The target-network heuristic function (from the NNet-fn dict). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`H`

## Calls

- `self._get_heur_fn_from_dict` → `func:deepxube.base.updater.UpdateHeur._get_heur_fn_from_dict` (lines: 715)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_targ_heur_fn(self) -> H:
        """ :return: The target-network heuristic function (from the NNet-fn dict). """
        return self._get_heur_fn_from_dict()
```
