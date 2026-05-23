---
id: "func:deepxube.domains.cube3.Cube3._np_to_states"
kind: "method"
name: "_np_to_states"
qualified_name: "deepxube.domains.cube3.Cube3._np_to_states"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 614
line_end: 617
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
  - name: "states_np"
    annotation: "List[NDArray]"
    default: null
returns: "List[Cube3State]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [616]
  - target: "func:deepxube.domains.cube3.Cube3State"
    expr: "Cube3State"
    call_sites: [617]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3._np_to_states`

**File:** [deepxube/domains/cube3.py:614](../../../../deepxube/domains/cube3.py#L614)
**Class:** `Cube3`
**Visibility:** private
**Kind:** method

## Signature

```python
def _np_to_states(self, states_np: List[NDArray]) -> List[Cube3State]
```

## Docstring

:return: List of ``Cube3State`` reconstructed from a stacked numpy array. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states_np` | `List[NDArray]` | — |

## Returns

`List[Cube3State]`

## Calls

- `Cube3State` → `func:deepxube.domains.cube3.Cube3State` (lines: 617)

### Unresolved
- `len` (lines: 616)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _np_to_states(self, states_np: List[NDArray]) -> List[Cube3State]:
        """ :return: List of ``Cube3State`` reconstructed from a stacked numpy array. """
        assert len(states_np) == 1
        return [Cube3State(x) for x in states_np[0]]
```
