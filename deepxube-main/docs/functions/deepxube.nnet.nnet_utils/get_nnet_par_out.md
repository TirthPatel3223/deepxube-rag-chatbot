---
id: "func:deepxube.nnet.nnet_utils.get_nnet_par_out"
kind: "function"
name: "get_nnet_par_out"
qualified_name: "deepxube.nnet.nnet_utils.get_nnet_par_out"
module: "deepxube.nnet.nnet_utils"
file: "deepxube/nnet/nnet_utils.py"
line_start: 256
line_end: 270
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "inputs_nnet"
    annotation: "List[NDArray]"
    default: null
  - name: "nnet_par_info"
    annotation: "NNetParInfo"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.data_utils.np_to_shnd"
    expr: "np_to_shnd"
    call_sites: [258]
  - target: null
    expr: "enumerate"
    call_sites: [259]
  - target: null
    expr: "nnet_par_info.nnet_i_q.put"
    call_sites: [261]
  - target: null
    expr: "nnet_par_info.nnet_o_q.get"
    call_sites: [263]
  - target: null
    expr: "out_shm.array.copy"
    call_sites: [264]
  - target: null
    expr: "arr_shm.close"
    call_sites: [267]
  - target: null
    expr: "arr_shm.unlink"
    call_sites: [268]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.nnet.nnet_utils.get_nnet_par_out`

**File:** [deepxube/nnet/nnet_utils.py:256](../../../../deepxube/nnet/nnet_utils.py#L256)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_nnet_par_out(inputs_nnet: List[NDArray], nnet_par_info: NNetParInfo) -> List[NDArray]
```

## Docstring

Send ``inputs_nnet`` to the parallel worker via shared memory and :return: the output arrays. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `inputs_nnet` | `List[NDArray]` | — |
| `nnet_par_info` | `NNetParInfo` | — |

## Returns

`List[NDArray]`

## Calls

- `np_to_shnd` → `func:deepxube.utils.data_utils.np_to_shnd` (lines: 258)

### Unresolved
- `enumerate` (lines: 259)
- `nnet_par_info.nnet_i_q.put` (lines: 261)
- `nnet_par_info.nnet_o_q.get` (lines: 263)
- `out_shm.array.copy` (lines: 264)
- `arr_shm.close` (lines: 267)
- `arr_shm.unlink` (lines: 268)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_nnet_par_out(inputs_nnet: List[NDArray], nnet_par_info: NNetParInfo) -> List[NDArray]:
    """ Send ``inputs_nnet`` to the parallel worker via shared memory and :return: the output arrays. """
    inputs_nnet_shm: List[SharedNDArray] = [np_to_shnd(inputs_nnet_i)
                                            for input_idx, inputs_nnet_i in enumerate(inputs_nnet)]

    nnet_par_info.nnet_i_q.put((nnet_par_info.proc_id, inputs_nnet_shm))

    out_shm_l: List[SharedNDArray] = nnet_par_info.nnet_o_q.get()
    out_l: List[NDArray] = [out_shm.array.copy() for out_shm in out_shm_l]

    for arr_shm in inputs_nnet_shm + out_shm_l:
        arr_shm.close()
        arr_shm.unlink()

    return out_l
```
