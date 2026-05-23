---
id: "func:deepxube.base.updater._put_from_q"
kind: "function"
name: "_put_from_q"
qualified_name: "deepxube.base.updater._put_from_q"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 82
line_end: 97
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "data_l"
    annotation: "List[List[NDArray]]"
    default: null
  - name: "from_q"
    annotation: "Queue"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [85, 97]
  - target: null
    expr: "data_shm_l.append"
    call_sites: [89]
  - target: "func:deepxube.utils.data_utils.np_to_shnd"
    expr: "np_to_shnd"
    call_sites: [89]
  - target: null
    expr: "from_q.put"
    call_sites: [91]
  - target: null
    expr: "arr_shm.close"
    call_sites: [95]
  - target: null
    expr: "times.record_time"
    call_sites: [97]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.updater._put_from_q`

**File:** [deepxube/base/updater.py:82](../../../../deepxube/base/updater.py#L82)
**Visibility:** private
**Kind:** function

## Signature

```python
def _put_from_q(data_l: List[List[NDArray]], from_q: Queue, times: Times) -> None
```

## Docstring

Copy each ndarray in ``data_l`` into fresh shared memory and push the
resulting ``SharedNDArray`` handles onto ``from_q`` for the main process. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `data_l` | `List[List[NDArray]]` | — |
| `from_q` | `Queue` | — |
| `times` | `Times` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 85, 97)
- `np_to_shnd` → `func:deepxube.utils.data_utils.np_to_shnd` (lines: 89)

### Unresolved
- `data_shm_l.append` (lines: 89)
- `from_q.put` (lines: 91)
- `arr_shm.close` (lines: 95)
- `times.record_time` (lines: 97)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _put_from_q(data_l: List[List[NDArray]], from_q: Queue, times: Times) -> None:
    """ Copy each ndarray in ``data_l`` into fresh shared memory and push the
    resulting ``SharedNDArray`` handles onto ``from_q`` for the main process. """
    start_time = time.time()

    data_shm_l: List[List[SharedNDArray]] = []
    for data in data_l:
        data_shm_l.append([np_to_shnd(data_i) for data_i in data])

    from_q.put(data_shm_l)

    for data_shm in data_shm_l:
        for arr_shm in data_shm:
            arr_shm.close()

    times.record_time("put", time.time() - start_time)
```
