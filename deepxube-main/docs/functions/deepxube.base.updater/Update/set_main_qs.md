---
id: "func:deepxube.base.updater.Update.set_main_qs"
kind: "method"
name: "set_main_qs"
qualified_name: "deepxube.base.updater.Update.set_main_qs"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 202
line_end: 207
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
  - name: "to_main_q"
    annotation: "Queue"
    default: null
  - name: "from_main_q"
    annotation: "Queue"
    default: null
  - name: "q_id"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.nnet.nnet_utils.NNetParInfo"
    expr: "NNetParInfo"
    call_sites: [207]
raises: []
reads_attrs:
  - "self.from_main_q"
  - "self.nnet_par_info_main"
  - "self.q_id"
  - "self.to_main_q"
writes_attrs:
  - "self.from_main_q"
  - "self.nnet_par_info_main"
  - "self.q_id"
  - "self.to_main_q"
---

# `deepxube.base.updater.Update.set_main_qs`

**File:** [deepxube/base/updater.py:202](../../../../deepxube/base/updater.py#L202)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def set_main_qs(self, to_main_q: Queue, from_main_q: Queue, q_id: int) -> None
```

## Docstring

Wire this updater to the main-process inference queues (used when ``sync_main``). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `to_main_q` | `Queue` | — |
| `from_main_q` | `Queue` | — |
| `q_id` | `int` | — |

## Returns

`None`

## Calls

- `NNetParInfo` → `func:deepxube.nnet.nnet_utils.NNetParInfo` (lines: 207)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.from_main_q`
- `self.nnet_par_info_main`
- `self.q_id`
- `self.to_main_q`

**Reads:**
- `self.from_main_q`
- `self.nnet_par_info_main`
- `self.q_id`
- `self.to_main_q`

## Source

```python
    def set_main_qs(self, to_main_q: Queue, from_main_q: Queue, q_id: int) -> None:
        """ Wire this updater to the main-process inference queues (used when ``sync_main``). """
        self.to_main_q = to_main_q
        self.from_main_q = from_main_q
        self.q_id = q_id
        self.nnet_par_info_main = NNetParInfo(self.to_main_q, self.from_main_q, self.q_id)
```
