---
id: "func:deepxube.domains.sokoban.SkState.__hash__"
kind: "method"
name: "__hash__"
qualified_name: "deepxube.domains.sokoban.SkState.__hash__"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 34
line_end: 43
class: "SkState"
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
    expr: "self.boxes.flatten"
    call_sites: [37]
  - target: null
    expr: "self.walls.flatten"
    call_sites: [38]
  - target: "func:numpy.concatenate"
    expr: "np.concatenate"
    call_sites: [39]
  - target: null
    expr: "boxes_flat.astype"
    call_sites: [39]
  - target: null
    expr: "walls_flat.astype"
    call_sites: [39]
  - target: null
    expr: "hash"
    call_sites: [41]
  - target: null
    expr: "state.tobytes"
    call_sites: [41]
raises: []
reads_attrs:
  - "self.agent"
  - "self.boxes"
  - "self.hash"
  - "self.walls"
writes_attrs:
  - "self.hash"
---

# `deepxube.domains.sokoban.SkState.__hash__`

**File:** [deepxube/domains/sokoban.py:34](../../../../deepxube/domains/sokoban.py#L34)
**Class:** `SkState`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __hash__(self) -> int
```

## Docstring

:return: Hash of the concatenated agent + boxes + walls byte representation. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`int`

## Calls

- `np.concatenate` → `func:numpy.concatenate` (lines: 39)

### Unresolved
- `self.boxes.flatten` (lines: 37)
- `self.walls.flatten` (lines: 38)
- `boxes_flat.astype` (lines: 39)
- `walls_flat.astype` (lines: 39)
- `hash` (lines: 41)
- `state.tobytes` (lines: 41)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.hash`

**Reads:**
- `self.agent`
- `self.boxes`
- `self.hash`
- `self.walls`

## Source

```python
    def __hash__(self) -> int:
        """ :return: Hash of the concatenated agent + boxes + walls byte representation. """
        if self.hash is None:
            boxes_flat = self.boxes.flatten()
            walls_flat = self.walls.flatten()
            state: NDArray[np.int_] = np.concatenate((self.agent, boxes_flat.astype(int), walls_flat.astype(int)), axis=0)

            self.hash = hash(state.tobytes())

        return self.hash
```
