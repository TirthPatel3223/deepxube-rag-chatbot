---
id: "func:deepxube.base.updater.UpdateHasHeur._get_heur_fn_from_dict"
kind: "method"
name: "_get_heur_fn_from_dict"
qualified_name: "deepxube.base.updater.UpdateHasHeur._get_heur_fn_from_dict"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 613
line_end: 615
class: "UpdateHasHeur"
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
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [615]
  - target: "func:deepxube.base.updater.UpdateHasHeur.heur_name"
    expr: "self.heur_name"
    call_sites: [615]
raises: []
reads_attrs:
  - "self.nnet_fn_dict"
writes_attrs: []
---

# `deepxube.base.updater.UpdateHasHeur._get_heur_fn_from_dict`

**File:** [deepxube/base/updater.py:613](../../../../deepxube/base/updater.py#L613)
**Class:** `UpdateHasHeur`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_heur_fn_from_dict(self) -> H
```

## Docstring

Fetch the heuristic callable from the NNet-function dict. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`H`

## Calls

- `cast` → `func:typing.cast` (lines: 615)
- `self.heur_name` → `func:deepxube.base.updater.UpdateHasHeur.heur_name` (lines: 615)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.nnet_fn_dict`

## Source

```python
    def _get_heur_fn_from_dict(self) -> H:
        """ Fetch the heuristic callable from the NNet-function dict. """
        return cast(H, self.nnet_fn_dict[self.heur_name()])
```
