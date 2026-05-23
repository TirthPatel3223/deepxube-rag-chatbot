---
id: "func:deepxube.domains.cube3.Cube3State.__hash__"
kind: "method"
name: "__hash__"
qualified_name: "deepxube.domains.cube3.Cube3State.__hash__"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 24
line_end: 28
class: "Cube3State"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "int"
docstring_source: "present"
callees:
  - target: null
    expr: "hash"
    call_sites: [27]
  - target: null
    expr: "self.colors.tobytes"
    call_sites: [27]
raises: []
reads_attrs:
  - "self.colors"
  - "self.hash"
writes_attrs:
  - "self.hash"
---

# `deepxube.domains.cube3.Cube3State.__hash__`

**File:** [deepxube/domains/cube3.py:24](../../../../deepxube/domains/cube3.py#L24)
**Class:** `Cube3State`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __hash__(self) -> int
```

## Docstring

:return: Hash of the colour byte representation. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`int`

## Calls

*(No resolved calls.)*

### Unresolved
- `hash` (lines: 27)
- `self.colors.tobytes` (lines: 27)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.hash`

**Reads:**
- `self.colors`
- `self.hash`

## Source

```python
    def __hash__(self) -> int:
        """ :return: Hash of the colour byte representation. """
        if self.hash is None:
            self.hash = hash(self.colors.tobytes())
        return self.hash
```
