---
id: "func:deepxube.factories.nnet_input_factory.register_nnet_input_dynamic"
kind: "function"
name: "register_nnet_input_dynamic"
qualified_name: "deepxube.factories.nnet_input_factory.register_nnet_input_dynamic"
module: "deepxube.factories.nnet_input_factory"
file: "deepxube/factories/nnet_input_factory.py"
line_start: 60
line_end: 74
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters: []
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.factories.domain_factory.domain_factory.get_all_class_names"
    expr: "domain_factory.get_all_class_names"
    call_sites: [69]
  - target: "func:deepxube.factories.domain_factory.domain_factory.get_type"
    expr: "domain_factory.get_type"
    call_sites: [70]
  - target: null
    expr: "issubclass"
    call_sites: [71]
  - target: null
    expr: "domain_t.get_dynamic_nnet_inputs"
    call_sites: [72]
  - target: null
    expr: "nnet_input_t_dict.items"
    call_sites: [73]
  - target: null
    expr: "register_nnet_input(domain_name, f'{nnet_input_name}')"
    call_sites: [74]
  - target: "func:deepxube.factories.nnet_input_factory.register_nnet_input"
    expr: "register_nnet_input"
    call_sites: [74]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.nnet_input_factory.register_nnet_input_dynamic`

**File:** [deepxube/factories/nnet_input_factory.py:60](../../../../deepxube/factories/nnet_input_factory.py#L60)
**Visibility:** public
**Kind:** function

## Signature

```python
def register_nnet_input_dynamic() -> None
```

## Docstring

Register ``NNetInput`` classes for every domain implementing
``DynamicNNetInput``.

Iterates ``domain_factory``, and for each domain that subclasses
``DynamicNNetInput`` calls ``get_dynamic_nnet_inputs()`` and registers
every returned ``(nnet_input_name, cls)`` pair under the domain's name.
Called once during CLI startup after domain modules have been imported.

## Parameters

*(No parameters.)*

## Returns

`None`

## Calls

- `domain_factory.get_all_class_names` → `func:deepxube.factories.domain_factory.domain_factory.get_all_class_names` (lines: 69)
- `domain_factory.get_type` → `func:deepxube.factories.domain_factory.domain_factory.get_type` (lines: 70)
- `register_nnet_input` → `func:deepxube.factories.nnet_input_factory.register_nnet_input` (lines: 74)

### Unresolved
- `issubclass` (lines: 71)
- `domain_t.get_dynamic_nnet_inputs` (lines: 72)
- `nnet_input_t_dict.items` (lines: 73)
- `register_nnet_input(domain_name, f'{nnet_input_name}')` (lines: 74)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def register_nnet_input_dynamic() -> None:
    """ Register ``NNetInput`` classes for every domain implementing
    ``DynamicNNetInput``.

    Iterates ``domain_factory``, and for each domain that subclasses
    ``DynamicNNetInput`` calls ``get_dynamic_nnet_inputs()`` and registers
    every returned ``(nnet_input_name, cls)`` pair under the domain's name.
    Called once during CLI startup after domain modules have been imported.
    """
    for domain_name in domain_factory.get_all_class_names():
        domain_t: Type[Domain] = domain_factory.get_type(domain_name)
        if issubclass(domain_t, DynamicNNetInput):
            nnet_input_t_dict: Dict[str, Type[NNetInput]] = domain_t.get_dynamic_nnet_inputs()
            for nnet_input_name, nnet_input_t in nnet_input_t_dict.items():
                register_nnet_input(domain_name, f"{nnet_input_name}")(nnet_input_t)
```
