---
id: "func:deepxube.base.updater.Update.start_nnet_runners"
kind: "method"
name: "start_nnet_runners"
qualified_name: "deepxube.base.updater.Update.start_nnet_runners"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 172
line_end: 179
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
  - name: "device"
    annotation: "torch.device"
    default: null
  - name: "on_gpu"
    annotation: "bool"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "self.nnet_par_dict.items"
    call_sites: [174]
  - target: "func:deepxube.nnet.nnet_utils.start_nnet_fn_runners"
    expr: "start_nnet_fn_runners"
    call_sites: [177]
raises: []
reads_attrs:
  - "self.nnet_file_dict"
  - "self.nnet_par_dict"
  - "self.nnet_par_info_l_dict"
  - "self.nnet_runner_proc_l_dict"
  - "self.up_args"
writes_attrs: []
---

# `deepxube.base.updater.Update.start_nnet_runners`

**File:** [deepxube/base/updater.py:172](../../../../deepxube/base/updater.py#L172)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def start_nnet_runners(self, device: torch.device, on_gpu: bool) -> None
```

## Docstring

Spawn one NNet runner process per worker for every registered NNet. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `device` | `torch.device` | — |
| `on_gpu` | `bool` | — |

## Returns

`None`

## Calls

- `start_nnet_fn_runners` → `func:deepxube.nnet.nnet_utils.start_nnet_fn_runners` (lines: 177)

### Unresolved
- `self.nnet_par_dict.items` (lines: 174)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.nnet_file_dict`
- `self.nnet_par_dict`
- `self.nnet_par_info_l_dict`
- `self.nnet_runner_proc_l_dict`
- `self.up_args`

## Source

```python
    def start_nnet_runners(self, device: torch.device, on_gpu: bool) -> None:
        """ Spawn one NNet runner process per worker for every registered NNet. """
        for nnet_name, nnet_par in self.nnet_par_dict.items():
            nnet_file: str = self.nnet_file_dict[nnet_name]
            nnet_par_infos: List[NNetParInfo] = self.nnet_par_info_l_dict[nnet_name]
            self.nnet_runner_proc_l_dict[nnet_name] = start_nnet_fn_runners(nnet_par.get_nnet, nnet_par_infos,
                                                                            nnet_file, device, on_gpu,
                                                                            batch_size=self.up_args.nnet_batch_size)
```
