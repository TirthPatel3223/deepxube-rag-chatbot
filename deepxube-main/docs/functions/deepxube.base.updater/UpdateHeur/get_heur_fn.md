---
id: "func:deepxube.base.updater.UpdateHeur.get_heur_fn"
kind: "method"
name: "get_heur_fn"
qualified_name: "deepxube.base.updater.UpdateHeur.get_heur_fn"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 705
line_end: 711
class: "UpdateHeur"
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
  - target: null
    expr: "super().get_heur_fn"
    call_sites: [708]
  - target: null
    expr: "super"
    call_sites: [708]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [711]
  - target: null
    expr: "self.get_heur_nnet_par().get_nnet_par_fn"
    call_sites: [711]
  - target: "func:deepxube.base.updater.UpdateHeur.get_heur_nnet_par"
    expr: "self.get_heur_nnet_par"
    call_sites: [711]
raises: []
reads_attrs:
  - "self.nnet_par_info_main"
  - "self.up_args"
writes_attrs: []
---

# `deepxube.base.updater.UpdateHeur.get_heur_fn`

**File:** [deepxube/base/updater.py:705](../../../../deepxube/base/updater.py#L705)
**Class:** `UpdateHeur`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_heur_fn(self) -> H
```

## Docstring

:return: Heuristic function; routed through the main process when ``sync_main``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`H`

## Calls

- `cast` → `func:typing.cast` (lines: 711)
- `self.get_heur_nnet_par` → `func:deepxube.base.updater.UpdateHeur.get_heur_nnet_par` (lines: 711)

### Unresolved
- `super().get_heur_fn` (lines: 708)
- `super` (lines: 708)
- `self.get_heur_nnet_par().get_nnet_par_fn` (lines: 711)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.nnet_par_info_main`
- `self.up_args`

## Source

```python
    def get_heur_fn(self) -> H:
        """ :return: Heuristic function; routed through the main process when ``sync_main``. """
        if not self.up_args.sync_main:
            return super().get_heur_fn()
        else:
            assert self.nnet_par_info_main is not None
            return cast(H, self.get_heur_nnet_par().get_nnet_par_fn(self.nnet_par_info_main, None))
```
