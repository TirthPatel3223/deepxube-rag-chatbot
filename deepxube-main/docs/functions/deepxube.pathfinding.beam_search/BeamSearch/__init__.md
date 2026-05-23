---
id: "func:deepxube.pathfinding.beam_search.BeamSearch.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearch.__init__"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 96
line_end: 101
class: "BeamSearch"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "domain"
    annotation: "D"
    default: null
  - name: "functions"
    annotation: "FNs"
    default: null
  - name: "beam_size"
    annotation: "int"
    default: "1"
  - name: "temp"
    annotation: "float"
    default: "0.0"
  - name: "eps"
    annotation: "float"
    default: "0.0"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [98]
  - target: null
    expr: "super"
    call_sites: [98]
raises: []
reads_attrs:
  - "self.beam_size_default"
  - "self.eps_default"
  - "self.temp_default"
writes_attrs:
  - "self.beam_size_default"
  - "self.eps_default"
  - "self.temp_default"
---

# `deepxube.pathfinding.beam_search.BeamSearch.__init__`

**File:** [deepxube/pathfinding/beam_search.py:96](../../../../deepxube/pathfinding/beam_search.py#L96)
**Class:** `BeamSearch`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, domain: D, functions: FNs, beam_size: int = 1, temp: float = 0.0, eps: float = 0.0)
```

## Docstring

Store default beam-search parameters; per-instance overrides may be supplied to ``make_instances``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `domain` | `D` | — |
| `functions` | `FNs` | — |
| `beam_size` | `int` | `1` |
| `temp` | `float` | `0.0` |
| `eps` | `float` | `0.0` |

## Returns

*(Not annotated.)*

## Calls

*(No resolved calls.)*

### Unresolved
- `super().__init__` (lines: 98)
- `super` (lines: 98)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.beam_size_default`
- `self.eps_default`
- `self.temp_default`

**Reads:**
- `self.beam_size_default`
- `self.eps_default`
- `self.temp_default`

## Source

```python
    def __init__(self, domain: D, functions: FNs, beam_size: int = 1, temp: float = 0.0, eps: float = 0.0):
        """ Store default beam-search parameters; per-instance overrides may be supplied to ``make_instances``. """
        super().__init__(domain, functions)
        self.beam_size_default: int = beam_size
        self.temp_default: float = temp
        self.eps_default: float = eps
```
