---
id: "func:deepxube.nnet.nnet_utils.stop_nnet_runners"
kind: "function"
name: "stop_nnet_runners"
qualified_name: "deepxube.nnet.nnet_utils.stop_nnet_runners"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 220
line_end: 226
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "nnet_fn_procs"
    annotation: "List[BaseProcess]"
    default: null
  - name: "nnet_par_infos"
    annotation: "List[NNetParInfo]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "nnet_par_infos[0].nnet_i_q.put"
    call_sites: [223]
  - target: null
    expr: "heur_fn_proc.join"
    call_sites: [226]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.nnet_utils.stop_nnet_runners`

**File:** [deepxube/nnet/nnet_utils.py:220](../../../../deepxube/nnet/nnet_utils.py#L220)
**Visibility:** public
**Kind:** function

## Signature

```python
def stop_nnet_runners(nnet_fn_procs: List[BaseProcess], nnet_par_infos: List[NNetParInfo]) -> None
```

## Docstring

Send a termination sentinel to each worker and wait for all processes to exit. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `nnet_fn_procs` | `List[BaseProcess]` | — |
| `nnet_par_infos` | `List[NNetParInfo]` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `nnet_par_infos[0].nnet_i_q.put` (lines: 223)
- `heur_fn_proc.join` (lines: 226)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def stop_nnet_runners(nnet_fn_procs: List[BaseProcess], nnet_par_infos: List[NNetParInfo]) -> None:
    """ Send a termination sentinel to each worker and wait for all processes to exit. """
    for _ in nnet_fn_procs:
        nnet_par_infos[0].nnet_i_q.put((None, None))

    for heur_fn_proc in nnet_fn_procs:
        heur_fn_proc.join()
```
