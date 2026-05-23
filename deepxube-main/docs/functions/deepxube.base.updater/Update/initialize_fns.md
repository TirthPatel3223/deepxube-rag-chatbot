---
id: "func:deepxube.base.updater.Update.initialize_fns"
kind: "method"
name: "initialize_fns"
qualified_name: "deepxube.base.updater.Update.initialize_fns"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 354
line_end: 361
class: "Update"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "self.nnet_par_dict.keys"
    call_sites: [356]
  - target: null
    expr: "self.targ_update_nums.get"
    call_sites: [359]
  - target: null
    expr: "nnet.get_nnet_par_fn"
    call_sites: [360]
  - target: null
    expr: "self.domain.set_nnet_fns"
    call_sites: [361]
raises: []
reads_attrs:
  - "self.domain"
  - "self.nnet_fn_dict"
  - "self.nnet_par_dict"
  - "self.nnet_par_info_dict"
  - "self.targ_update_nums"
writes_attrs: []
---

# `deepxube.base.updater.Update.initialize_fns`

**File:** [deepxube/base/updater.py:354](../../../../deepxube/base/updater.py#L354)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def initialize_fns(self) -> None
```

## Docstring

Build concrete NNet callables for every registered NNet and bind them to the domain. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `self.nnet_par_dict.keys` (lines: 356)
- `self.targ_update_nums.get` (lines: 359)
- `nnet.get_nnet_par_fn` (lines: 360)
- `self.domain.set_nnet_fns` (lines: 361)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`
- `self.nnet_fn_dict`
- `self.nnet_par_dict`
- `self.nnet_par_info_dict`
- `self.targ_update_nums`

## Source

```python
    def initialize_fns(self) -> None:
        """ Build concrete NNet callables for every registered NNet and bind them to the domain. """
        for nnet_name in self.nnet_par_dict.keys():
            nnet: NNetPar = self.nnet_par_dict[nnet_name]
            nnet_par_info: NNetParInfo = self.nnet_par_info_dict[nnet_name]
            targ_update_num: Optional[int] = self.targ_update_nums.get(nnet_name)
            self.nnet_fn_dict[nnet_name] = nnet.get_nnet_par_fn(nnet_par_info, targ_update_num)
        self.domain.set_nnet_fns(self.nnet_fn_dict)
```
