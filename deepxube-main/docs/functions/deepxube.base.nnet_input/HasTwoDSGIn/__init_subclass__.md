---
id: "func:deepxube.base.nnet_input.HasTwoDSGIn.__init_subclass__"
kind: "method"
name: "__init_subclass__"
qualified_name: "deepxube.base.nnet_input.HasTwoDSGIn.__init_subclass__"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 282
line_end: 285
class: "HasTwoDSGIn"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "cls"
    annotation: null
    default: null
  - name: "**kwargs"
    annotation: "Any"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init_subclass__"
    call_sites: [284]
  - target: null
    expr: "super"
    call_sites: [284]
  - target: "func:deepxube.base.nnet_input.HasTwoDSGIn.register_nnet_input"
    expr: "cls.register_nnet_input"
    call_sites: [285]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.nnet_input.HasTwoDSGIn.__init_subclass__`

**File:** [deepxube/base/nnet_input.py:282](../../../../deepxube/base/nnet_input.py#L282)
**Class:** `HasTwoDSGIn`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init_subclass__(cls, **kwargs: Any) -> None
```

## Docstring

Register ``TwoDSGConcrete`` under ``"2d_sg"``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `cls` | — | — |
| `**kwargs` | `Any` | — |

## Returns

`None`

## Calls

- `cls.register_nnet_input` → `func:deepxube.base.nnet_input.HasTwoDSGIn.register_nnet_input` (lines: 285)

### Unresolved
- `super().__init_subclass__` (lines: 284)
- `super` (lines: 284)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``TwoDSGConcrete`` under ``"2d_sg"``. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.TwoDSGConcrete, "2d_sg")
```
