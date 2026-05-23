---
id: "func:deepxube.nnet.nnet_utils.get_nnet_par_infos"
kind: "function"
name: "get_nnet_par_infos"
qualified_name: "deepxube.nnet.nnet_utils.get_nnet_par_infos"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 178
line_end: 190
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "num_procs"
    annotation: "int"
    default: null
returns: "List[NNetParInfo]"
docstring_source: "present"
callees:
  - target: "func:torch.multiprocessing.get_context"
    expr: "get_context"
    call_sites: [180]
  - target: null
    expr: "ctx.Queue"
    call_sites: [182, 186]
  - target: null
    expr: "range"
    call_sites: [185]
  - target: null
    expr: "nnet_o_qs.append"
    call_sites: [187]
  - target: null
    expr: "nnet_par_infos.append"
    call_sites: [188]
  - target: "func:deepxube.nnet.nnet_utils.NNetParInfo"
    expr: "NNetParInfo"
    call_sites: [188]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.nnet_utils.get_nnet_par_infos`

**File:** [deepxube/nnet/nnet_utils.py:178](../../../../deepxube/nnet/nnet_utils.py#L178)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_nnet_par_infos(num_procs: int) -> List[NNetParInfo]
```

## Docstring

:return: One ``NNetParInfo`` per worker process, all sharing the same input queue. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `num_procs` | `int` | — |

## Returns

`List[NNetParInfo]`

## Calls

- `get_context` → `func:torch.multiprocessing.get_context` (lines: 180)
- `NNetParInfo` → `func:deepxube.nnet.nnet_utils.NNetParInfo` (lines: 188)

### Unresolved
- `ctx.Queue` (lines: 182, 186)
- `range` (lines: 185)
- `nnet_o_qs.append` (lines: 187)
- `nnet_par_infos.append` (lines: 188)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_nnet_par_infos(num_procs: int) -> List[NNetParInfo]:
    """ :return: One ``NNetParInfo`` per worker process, all sharing the same input queue. """
    ctx = get_context("spawn")

    nnet_i_q: Queue = ctx.Queue()
    nnet_o_qs: List[Queue] = []
    nnet_par_infos: List[NNetParInfo] = []
    for proc_id in range(num_procs):
        nnet_o_q: Queue = ctx.Queue(1)
        nnet_o_qs.append(nnet_o_q)
        nnet_par_infos.append(NNetParInfo(nnet_i_q, nnet_o_q, proc_id))

    return nnet_par_infos
```
