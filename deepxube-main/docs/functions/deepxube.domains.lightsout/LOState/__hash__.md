---
id: "func:deepxube.domains.lightsout.LOState.__hash__"
kind: "method"
name: "__hash__"
qualified_name: "deepxube.domains.lightsout.LOState.__hash__"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 22
line_end: 27
class: "LOState"
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
    call_sites: [25]
  - target: null
    expr: "self.tiles.tobytes"
    call_sites: [25]
raises: []
reads_attrs:
  - "self.hash"
  - "self.tiles"
writes_attrs:
  - "self.hash"
---

# `deepxube.domains.lightsout.LOState.__hash__`

**File:** [deepxube/domains/lightsout.py:22](../../../../deepxube/domains/lightsout.py#L22)
**Class:** `LOState`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __hash__(self) -> int
```

## Docstring

:return: Hash of the tile bytes. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`int`

## Calls

*(No resolved calls.)*

### Unresolved
- `hash` (lines: 25)
- `self.tiles.tobytes` (lines: 25)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.hash`

**Reads:**
- `self.hash`
- `self.tiles`

## Source

```python
    def __hash__(self) -> int:
        """ :return: Hash of the tile bytes. """
        if self.hash is None:
            self.hash = hash(self.tiles.tobytes())

        return self.hash
```
