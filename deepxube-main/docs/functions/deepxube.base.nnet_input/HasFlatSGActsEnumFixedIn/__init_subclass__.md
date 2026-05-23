---
id: "func:deepxube.base.nnet_input.HasFlatSGActsEnumFixedIn.__init_subclass__"
kind: "method"
name: "__init_subclass__"
qualified_name: "deepxube.base.nnet_input.HasFlatSGActsEnumFixedIn.__init_subclass__"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 222
line_end: 225
class: "HasFlatSGActsEnumFixedIn"
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
    call_sites: [224]
  - target: null
    expr: "super"
    call_sites: [224]
  - target: "func:deepxube.base.nnet_input.HasFlatSGActsEnumFixedIn.register_nnet_input"
    expr: "cls.register_nnet_input"
    call_sites: [225]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.nnet_input.HasFlatSGActsEnumFixedIn.__init_subclass__`

**File:** [deepxube/base/nnet_input.py:222](../../../../deepxube/base/nnet_input.py#L222)
**Class:** `HasFlatSGActsEnumFixedIn`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init_subclass__(cls, **kwargs: Any) -> None
```

## Docstring

Register ``FlatSGActFixConcrete`` under ``"flat_sg_actfix"``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `cls` | — | — |
| `**kwargs` | `Any` | — |

## Returns

`None`

## Calls

- `cls.register_nnet_input` → `func:deepxube.base.nnet_input.HasFlatSGActsEnumFixedIn.register_nnet_input` (lines: 225)

### Unresolved
- `super().__init_subclass__` (lines: 224)
- `super` (lines: 224)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def __init_subclass__(cls, **kwargs: Any) -> None:
        """ Register ``FlatSGActFixConcrete`` under ``"flat_sg_actfix"``. """
        super().__init_subclass__(**kwargs)
        cls.register_nnet_input(cls.FlatSGActFixConcrete, "flat_sg_actfix")
```
