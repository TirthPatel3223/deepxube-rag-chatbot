---
id: "func:deepxube.utils.data_utils.Logger.write"
kind: "method"
name: "write"
qualified_name: "deepxube.utils.data_utils.Logger.write"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 43
line_end: 52
class: "Logger"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "message"
    annotation: "str"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "self.terminal.write"
    call_sites: [50]
  - target: null
    expr: "self.log.write"
    call_sites: [51]
  - target: null
    expr: "self.log.flush"
    call_sites: [52]
raises: []
reads_attrs:
  - "self.echo"
  - "self.log"
  - "self.terminal"
writes_attrs: []
---

# `deepxube.utils.data_utils.Logger.write`

**File:** [deepxube/utils/data_utils.py:43](../../../../deepxube/utils/data_utils.py#L43)
**Class:** `Logger`
**Visibility:** public
**Kind:** method

## Signature

```python
def write(self, message: str) -> None
```

## Docstring

Write ``message`` to the log file (and to the terminal if
``echo`` is ``True``), flushing the file afterwards.

:param message: String to write.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `message` | `str` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `self.terminal.write` (lines: 50)
- `self.log.write` (lines: 51)
- `self.log.flush` (lines: 52)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.echo`
- `self.log`
- `self.terminal`

## Source

```python
    def write(self, message: str) -> None:
        """ Write ``message`` to the log file (and to the terminal if
        ``echo`` is ``True``), flushing the file afterwards.

        :param message: String to write.
        """
        if self.echo:
            self.terminal.write(message)
        self.log.write(message)
        self.log.flush()
```
