---
id: "func:deepxube.domains.sokoban.SkState.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.domains.sokoban.SkState.__init__"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 27
line_end: 32
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
  - name: "agent"
    annotation: "NDArray[np.int_]"
    default: null
  - name: "boxes"
    annotation: "NDArray[np.uint8]"
    default: null
  - name: "walls"
    annotation: "NDArray[np.uint8]"
    default: null
returns: null
docstring_source: "missing"
callees: []
raises: []
reads_attrs:
  - "self.agent"
  - "self.boxes"
  - "self.hash"
  - "self.walls"
writes_attrs:
  - "self.agent"
  - "self.boxes"
  - "self.hash"
  - "self.walls"
---

# `deepxube.domains.sokoban.SkState.__init__`

**File:** [deepxube/domains/sokoban.py:27](../../../../deepxube/domains/sokoban.py#L27)
**Class:** `SkState`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, agent: NDArray[np.int_], boxes: NDArray[np.uint8], walls: NDArray[np.uint8])
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `agent` | `NDArray[np.int_]` | — |
| `boxes` | `NDArray[np.uint8]` | — |
| `walls` | `NDArray[np.uint8]` | — |

## Returns

*(Not annotated.)*

## Calls

*(No resolved calls.)*

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.agent`
- `self.boxes`
- `self.hash`
- `self.walls`

**Reads:**
- `self.agent`
- `self.boxes`
- `self.hash`
- `self.walls`

## Source

```python
    def __init__(self, agent: NDArray[np.int_], boxes: NDArray[np.uint8], walls: NDArray[np.uint8]):
        self.agent: NDArray[np.int_] = agent
        self.boxes: NDArray[np.uint8] = boxes
        self.walls: NDArray[np.uint8] = walls

        self.hash: Optional[int] = None
```
