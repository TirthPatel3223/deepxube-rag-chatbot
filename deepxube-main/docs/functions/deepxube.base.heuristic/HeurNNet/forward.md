---
id: "func:deepxube.base.heuristic.HeurNNet.forward"
kind: "method"
name: "forward"
qualified_name: "deepxube.base.heuristic.HeurNNet.forward"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 82
line_end: 89
class: "HeurNNet"
visibility: "public"
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
returns: "List[Tensor]"
docstring_source: "present"
callees:
  - target: null
    expr: "inputs[-1].long"
    call_sites: [85]
  - target: "func:deepxube.base.heuristic.HeurNNet._forward"
    expr: "self._forward"
    call_sites: [86, 89]
  - target: "func:torch.gather"
    expr: "torch.gather"
    call_sites: [87]
raises: []
reads_attrs:
  - "self.q_fix"
writes_attrs: []
---

# `deepxube.base.heuristic.HeurNNet.forward`

**File:** [deepxube/base/heuristic.py:82](../../../../deepxube/base/heuristic.py#L82)
**Class:** `HeurNNet`
**Visibility:** public
**Kind:** method

## Signature

```python
def forward(self, inputs: List[Tensor]) -> List[Tensor]
```

## Docstring

Run the body and, if ``q_fix``, gather only the requested action columns. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `inputs` | `List[Tensor]` | — |

## Returns

`List[Tensor]`

## Calls

- `self._forward` → `func:deepxube.base.heuristic.HeurNNet._forward` (lines: 86, 89)
- `torch.gather` → `func:torch.gather` (lines: 87)

### Unresolved
- `inputs[-1].long` (lines: 85)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.q_fix`

## Source

```python
    def forward(self, inputs: List[Tensor]) -> List[Tensor]:
        """ Run the body and, if ``q_fix``, gather only the requested action columns. """
        if self.q_fix:
            action_idxs: Tensor = inputs[-1].long()
            x: Tensor = self._forward(inputs[:-1])
            return [torch.gather(x, 1, action_idxs)]
        else:
            return [self._forward(inputs)]
```
