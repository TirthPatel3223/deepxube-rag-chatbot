---
id: "func:deepxube.domains.cube3.Cube3._states_to_np"
kind: "method"
name: "_states_to_np"
qualified_name: "deepxube.domains.cube3.Cube3._states_to_np"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 610
line_end: 612
class: "Cube3"
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
    annotation: "List[Cube3State]"
    default: null
returns: "List[NDArray[np.uint8]]"
docstring_source: "present"
callees:
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [612]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3._states_to_np`

**File:** [deepxube/domains/cube3.py:610](../../../../deepxube/domains/cube3.py#L610)
**Class:** `Cube3`
**Visibility:** private
**Kind:** method

## Signature

```python
def _states_to_np(self, states: List[Cube3State]) -> List[NDArray[np.uint8]]
```

## Docstring

:return: Stacked colour numpy arrays. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[Cube3State]` | — |

## Returns

`List[NDArray[np.uint8]]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 612)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _states_to_np(self, states: List[Cube3State]) -> List[NDArray[np.uint8]]:
        """ :return: Stacked colour numpy arrays. """
        return [np.stack([x.colors for x in states], axis=0)]
```
