---
id: "func:deepxube.base.updater.UpdateHasHeur.get_heur_fn"
kind: "method"
name: "get_heur_fn"
qualified_name: "deepxube.base.updater.UpdateHasHeur.get_heur_fn"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 609
line_end: 611
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
returns: "H"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.updater.UpdateHasHeur._get_heur_fn_from_dict"
    expr: "self._get_heur_fn_from_dict"
    call_sites: [611]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater.UpdateHasHeur.get_heur_fn`

**File:** [deepxube/base/updater.py:609](../../../../deepxube/base/updater.py#L609)
**Class:** `UpdateHasHeur`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_heur_fn(self) -> H
```

## Docstring

:return: Current heuristic-function callable. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`H`

## Calls

- `self._get_heur_fn_from_dict` → `func:deepxube.base.updater.UpdateHasHeur._get_heur_fn_from_dict` (lines: 611)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def get_heur_fn(self) -> H:
        """ :return: Current heuristic-function callable. """
        return self._get_heur_fn_from_dict()
```
