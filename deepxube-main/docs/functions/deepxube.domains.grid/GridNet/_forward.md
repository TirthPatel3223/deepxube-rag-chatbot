---
id: "func:deepxube.domains.grid.GridNet._forward"
kind: "method"
name: "_forward"
qualified_name: "deepxube.domains.grid.GridNet._forward"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 202
line_end: 205
class: "GridNet"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "inputs"
    annotation: "List[Tensor]"
    default: null
returns: "Tensor"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.grid.GridNet.heur"
    expr: "self.heur"
    call_sites: [204]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.grid.GridNet._forward`

**File:** [deepxube/domains/grid.py:202](../../../../deepxube/domains/grid.py#L202)
**Class:** `GridNet`
**Visibility:** private
**Kind:** method

## Signature

```python
def _forward(self, inputs: List[Tensor]) -> Tensor
```

## Docstring

:return: Heuristic value from the 2-channel spatial input. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `inputs` | `List[Tensor]` | — |

## Returns

`Tensor`

## Calls

- `self.heur` → `func:deepxube.domains.grid.GridNet.heur` (lines: 204)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _forward(self, inputs: List[Tensor]) -> Tensor:
        """ :return: Heuristic value from the 2-channel spatial input. """
        x: Tensor = self.heur(inputs[0])
        return x
```
