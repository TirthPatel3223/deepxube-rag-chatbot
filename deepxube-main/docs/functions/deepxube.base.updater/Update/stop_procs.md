---
id: "func:deepxube.base.updater.Update.stop_procs"
kind: "method"
name: "stop_procs"
qualified_name: "deepxube.base.updater.Update.stop_procs"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 340
line_end: 352
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
    expr: "from_main_q.put"
    call_sites: [344]
  - target: null
    expr: "proc.join"
    call_sites: [348]
raises: []
reads_attrs:
  - "self.from_main_qs"
  - "self.from_q"
  - "self.procs"
  - "self.to_q"
writes_attrs:
  - "self.from_q"
  - "self.procs"
  - "self.to_q"
---

# `deepxube.base.updater.Update.stop_procs`

**File:** [deepxube/base/updater.py:340](../../../../deepxube/base/updater.py#L340)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def stop_procs(self) -> None
```

## Docstring

Send ``None`` to every worker's main queue and join all worker processes. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `from_main_q.put` (lines: 344)
- `proc.join` (lines: 348)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.from_q`
- `self.procs`
- `self.to_q`

**Reads:**
- `self.from_main_qs`
- `self.from_q`
- `self.procs`
- `self.to_q`

## Source

```python
    def stop_procs(self) -> None:
        """ Send ``None`` to every worker's main queue and join all worker processes. """
        # sending stop signal
        for from_main_q in self.from_main_qs:
            from_main_q.put(None)

        # clean up clean up everybody do your share
        for proc in self.procs:
            proc.join()

        self.procs = []
        self.to_q = None
        self.from_q = None
```
