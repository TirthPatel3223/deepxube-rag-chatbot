---
id: "func:deepxube.base.nnet_input.HasTwoDSGActsEnumFixedIn.__init_subclass__"
kind: "method"
name: "__init_subclass__"
qualified_name: "deepxube.base.nnet_input.HasTwoDSGActsEnumFixedIn.__init_subclass__"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 329
line_end: 332
class: "HasTwoDSGActsEnumFixedIn"
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
    call_sites: [331]
  - target: null
    expr: "super"
    call_sites: [331]
  - target: "func:deepxube.base.nnet_input.HasTwoDSGActsEnumFixedIn.register_nnet_input"
    expr: "cls.register_nnet_input"
    call_sites: [332]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.nnet_input.HasTwoDSGActsEnumFixedIn.__init_subclass__`

**File:** [deepxube/base/nnet_input.py:329](../../../../deepxube/base/nnet_input.py#L329)
**Class:** `HasTwoDSGActsEnumFixedIn`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init_subclass__(cls, **kwargs: Any) -> None
```

## Docstring

Register ``TwoDSGActFixConcrete`` under ``"2d_sg_actfix"``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `cls` | — | — |
| `**kwargs` | `Any` | — |

## Returns

`None`

## Calls

- `cls.register_nnet_input` → `func:deepxube.base.nnet_input.HasTwoDSGActsEnumFixedIn.register_nnet_input` (lines: 332)

### Unresolved
- `super().__init_subclass__` (lines: 331)
- `super` (lines: 331)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``TwoDSGActFixConcrete`` under ``"2d_sg_actfix"``. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.TwoDSGActFixConcrete, "2d_sg_actfix")
```
