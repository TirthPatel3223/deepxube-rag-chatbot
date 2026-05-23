---
id: "func:deepxube.base.updater.Update.get_update_data"
kind: "method"
name: "get_update_data"
qualified_name: "deepxube.base.updater.Update.get_update_data"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 273
line_end: 302
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
  - name: "nowait"
    annotation: "bool"
    default: "False"
returns: "List[List[NDArray]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.data_utils.get_nowait_noerr"
    expr: "get_nowait_noerr"
    call_sites: [281]
  - target: null
    expr: "self.from_q.get"
    call_sites: [283]
  - target: null
    expr: "data_get_np.append"
    call_sites: [291]
  - target: null
    expr: "data_get_i.array.copy"
    call_sites: [291]
  - target: null
    expr: "data_l.append"
    call_sites: [292]
  - target: null
    expr: "arr_shm.close"
    call_sites: [299]
  - target: null
    expr: "arr_shm.unlink"
    call_sites: [300]
raises: []
reads_attrs:
  - "self.from_q"
  - "self.num_generated"
writes_attrs: []
---

# `deepxube.base.updater.Update.get_update_data`

**File:** [deepxube/base/updater.py:273](../../../../deepxube/base/updater.py#L273)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_update_data(self, nowait: bool = False) -> List[List[NDArray]]
```

## Docstring

Fetch one batch of training arrays from a worker via ``from_q``
(blocking unless ``nowait=True``), copy out of shared memory, and
free the shared blocks. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nowait` | `bool` | `False` |

## Returns

`List[List[NDArray]]`

## Calls

- `get_nowait_noerr` → `func:deepxube.utils.data_utils.get_nowait_noerr` (lines: 281)

### Unresolved
- `self.from_q.get` (lines: 283)
- `data_get_np.append` (lines: 291)
- `data_get_i.array.copy` (lines: 291)
- `data_l.append` (lines: 292)
- `arr_shm.close` (lines: 299)
- `arr_shm.unlink` (lines: 300)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.from_q`
- `self.num_generated`

## Source

```python
    def get_update_data(self, nowait: bool = False) -> List[List[NDArray]]:
        """ Fetch one batch of training arrays from a worker via ``from_q``
        (blocking unless ``nowait=True``), copy out of shared memory, and
        free the shared blocks. """
        assert self.from_q is not None
        data_l: List[List[NDArray]] = []
        data_get_l: Optional[List[List[SharedNDArray]]]
        if nowait:
            data_get_l = get_nowait_noerr(self.from_q)
        else:
            data_get_l = self.from_q.get()
        if data_get_l is None:
            return []

        for data_get in data_get_l:
            # to np
            data_get_np: List[NDArray] = []
            for data_get_i in data_get:
                data_get_np.append(data_get_i.array.copy())
            data_l.append(data_get_np)

            # status tracking
            self.num_generated += data_get_np[0].shape[0]

            # unlink shared mem
            for arr_shm in data_get:
                arr_shm.close()
                arr_shm.unlink()

        return data_l
```
