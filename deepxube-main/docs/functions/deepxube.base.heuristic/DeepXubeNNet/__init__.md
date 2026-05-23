---
id: "func:deepxube.base.heuristic.DeepXubeNNet.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.base.heuristic.DeepXubeNNet.__init__"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 41
line_end: 47
class: "DeepXubeNNet"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "nnet_input"
    annotation: "In"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [43]
  - target: null
    expr: "super"
    call_sites: [43]
  - target: null
    expr: "isinstance"
    call_sites: [44]
  - target: "func:deepxube.base.heuristic.DeepXubeNNet.nnet_input_type"
    expr: "self.nnet_input_type"
    call_sites: [44]
raises: []
reads_attrs:
  - "self.lr"
  - "self.lr_d"
  - "self.nnet_input"
writes_attrs:
  - "self.lr"
  - "self.lr_d"
  - "self.nnet_input"
---

# `deepxube.base.heuristic.DeepXubeNNet.__init__`

**File:** [deepxube/base/heuristic.py:41](../../../../deepxube/base/heuristic.py#L41)
**Class:** `DeepXubeNNet`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, nnet_input: In)
```

## Docstring

Bind the ``NNetInput`` and initialise default learning-rate parameters. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet_input` | `In` | — |

## Returns

*(Not annotated.)*

## Calls

- `self.nnet_input_type` → `func:deepxube.base.heuristic.DeepXubeNNet.nnet_input_type` (lines: 44)

### Unresolved
- `super().__init__` (lines: 43)
- `super` (lines: 43)
- `isinstance` (lines: 44)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.lr`
- `self.lr_d`
- `self.nnet_input`

**Reads:**
- `self.lr`
- `self.lr_d`
- `self.nnet_input`

## Source

```python
    def __init__(self, nnet_input: In):
        """ Bind the ``NNetInput`` and initialise default learning-rate parameters. """
        super().__init__()
        assert isinstance(nnet_input, self.nnet_input_type()), f"NNetInput {nnet_input} must be an instance of {self.nnet_input_type()}."
        self.nnet_input: In = nnet_input
        self.lr: float = 0.001
        self.lr_d: float = 0.9999993
```
