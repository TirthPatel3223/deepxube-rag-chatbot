---
id: "func:deepxube.logic.asp.model_to_body"
kind: "function"
name: "model_to_body"
qualified_name: "deepxube.logic.asp.model_to_body"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 17
line_end: 19
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "model"
    annotation: "Model"
    default: null
returns: "str"
docstring_source: "present"
callees:
  - target: null
    expr: "','.join"
    call_sites: [19]
  - target: "func:deepxube.logic.logic_utils.atom_to_str"
    expr: "atom_to_str"
    call_sites: [19]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.asp.model_to_body`

**File:** [deepxube/logic/asp.py:17](../../../../deepxube/logic/asp.py#L17)
**Visibility:** public
**Kind:** function

## Signature

```python
def model_to_body(model: Model) -> str
```

## Docstring

:return: Comma-separated atom strings for every atom in ``model``, suitable as a rule body. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `model` | `Model` | — |

## Returns

`str`

## Calls

- `atom_to_str` → `func:deepxube.logic.logic_utils.atom_to_str` (lines: 19)

### Unresolved
- `','.join` (lines: 19)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def model_to_body(model: Model) -> str:
    """ :return: Comma-separated atom strings for every atom in ``model``, suitable as a rule body. """
    return ','.join([atom_to_str(atom) for atom in model])
```
