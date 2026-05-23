---
id: "func:deepxube.domains.lightsout.LightsOut._np_to_states"
kind: "method"
name: "_np_to_states"
qualified_name: "deepxube.domains.lightsout.LightsOut._np_to_states"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 134
line_end: 137
class: "LightsOut"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states_np"
    annotation: "List[NDArray]"
    default: null
returns: "List[LOState]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [136]
  - target: "func:deepxube.domains.lightsout.LOState"
    expr: "LOState"
    call_sites: [137]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.lightsout.LightsOut._np_to_states`

**File:** [deepxube/domains/lightsout.py:134](../../../../deepxube/domains/lightsout.py#L134)
**Class:** `LightsOut`
**Visibility:** private
**Kind:** method

## Signature

```python
def _np_to_states(self, states_np: List[NDArray]) -> List[LOState]
```

## Docstring

:return: List of ``LOState`` reconstructed from a stacked numpy array. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_np` | `List[NDArray]` | — |

## Returns

`List[LOState]`

## Calls

- `LOState` → `func:deepxube.domains.lightsout.LOState` (lines: 137)

### Unresolved
- `len` (lines: 136)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _np_to_states(self, states_np: List[NDArray]) -> List[LOState]:
        """ :return: List of ``LOState`` reconstructed from a stacked numpy array. """
        assert len(states_np) == 1
        return [LOState(x) for x in states_np[0]]
```
