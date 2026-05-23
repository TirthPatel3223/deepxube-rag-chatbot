---
id: "func:deepxube.base.updater.Update.set_nnet_par_info"
kind: "method"
name: "set_nnet_par_info"
qualified_name: "deepxube.base.updater.Update.set_nnet_par_info"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 181
line_end: 186
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
  - name: "nnet_name"
    annotation: "str"
    default: null
  - name: "nnet_par_info"
    annotation: "NNetParInfo"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "self.nnet_par_dict.keys"
    call_sites: [183]
  - target: null
    expr: "self.nnet_file_dict.keys"
    call_sites: [184]
  - target: null
    expr: "self.nnet_par_info_dict.keys"
    call_sites: [185]
raises: []
reads_attrs:
  - "self.nnet_file_dict"
  - "self.nnet_par_dict"
  - "self.nnet_par_info_dict"
writes_attrs: []
---

# `deepxube.base.updater.Update.set_nnet_par_info`

**File:** [deepxube/base/updater.py:181](../../../../deepxube/base/updater.py#L181)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def set_nnet_par_info(self, nnet_name: str, nnet_par_info: NNetParInfo) -> None
```

## Docstring

Assign a single worker's NNet queue triple for ``nnet_name``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet_name` | `str` | — |
| `nnet_par_info` | `NNetParInfo` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `self.nnet_par_dict.keys` (lines: 183)
- `self.nnet_file_dict.keys` (lines: 184)
- `self.nnet_par_info_dict.keys` (lines: 185)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.nnet_file_dict`
- `self.nnet_par_dict`
- `self.nnet_par_info_dict`

## Source

```python
    def set_nnet_par_info(self, nnet_name: str, nnet_par_info: NNetParInfo) -> None:
        """ Assign a single worker's NNet queue triple for ``nnet_name``. """
        assert nnet_name in self.nnet_par_dict.keys(), f"{nnet_name} not in dict"
        assert nnet_name in self.nnet_file_dict.keys(), f"{nnet_name} not in dict"
        assert nnet_name not in self.nnet_par_info_dict.keys(), f"{nnet_name} already in dict"
        self.nnet_par_info_dict[nnet_name] = nnet_par_info
```
