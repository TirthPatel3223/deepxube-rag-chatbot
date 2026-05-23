---
id: "func:deepxube.base.updater.Update.set_nnet_par_info_l_dict"
kind: "method"
name: "set_nnet_par_info_l_dict"
qualified_name: "deepxube.base.updater.Update.set_nnet_par_info_l_dict"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 167
line_end: 170
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
    call_sites: [169]
  - target: "func:deepxube.nnet.nnet_utils.get_nnet_par_infos"
    expr: "get_nnet_par_infos"
    call_sites: [170]
raises: []
reads_attrs:
  - "self.nnet_par_dict"
  - "self.nnet_par_info_l_dict"
  - "self.up_args"
writes_attrs: []
---

# `deepxube.base.updater.Update.set_nnet_par_info_l_dict`

**File:** [deepxube/base/updater.py:167](../../../../deepxube/base/updater.py#L167)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def set_nnet_par_info_l_dict(self) -> None
```

## Docstring

Build the list of per-worker NNet queue triples for every registered NNet. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

- `get_nnet_par_infos` → `func:deepxube.nnet.nnet_utils.get_nnet_par_infos` (lines: 170)

### Unresolved
- `self.nnet_par_dict.keys` (lines: 169)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.nnet_par_dict`
- `self.nnet_par_info_l_dict`
- `self.up_args`

## Source

```python
    def set_nnet_par_info_l_dict(self) -> None:
        """ Build the list of per-worker NNet queue triples for every registered NNet. """
        for nnet_name in self.nnet_par_dict.keys():
            self.nnet_par_info_l_dict[nnet_name] = get_nnet_par_infos(self.up_args.procs)
```
