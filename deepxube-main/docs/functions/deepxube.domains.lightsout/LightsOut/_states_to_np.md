---
id: "func:deepxube.domains.lightsout.LightsOut._states_to_np"
kind: "method"
name: "_states_to_np"
qualified_name: "deepxube.domains.lightsout.LightsOut._states_to_np"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 130
line_end: 132
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
  - name: "states"
    annotation: "List[LOState]"
    default: null
returns: "List[NDArray[np.uint8]]"
docstring_source: "present"
callees:
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [132]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.lightsout.LightsOut._states_to_np`

**File:** [deepxube/domains/lightsout.py:130](../../../../deepxube/domains/lightsout.py#L130)
**Class:** `LightsOut`
**Visibility:** private
**Kind:** method

## Signature

```python
def _states_to_np(self, states: List[LOState]) -> List[NDArray[np.uint8]]
```

## Docstring

:return: Stacked tile numpy arrays. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[LOState]` | — |

## Returns

`List[NDArray[np.uint8]]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 132)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _states_to_np(self, states: List[LOState]) -> List[NDArray[np.uint8]]:
        """ :return: Stacked tile numpy arrays. """
        return [np.stack([x.tiles for x in states], axis=0)]
```
