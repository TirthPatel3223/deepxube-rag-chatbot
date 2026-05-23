---
id: "class:deepxube.base.nnet_input.DynamicNNetInput"
kind: "class"
name: "DynamicNNetInput"
qualified_name: "deepxube.base.nnet_input.DynamicNNetInput"
module: "deepxube.base.nnet_input"
file: "deepxube/base/nnet_input.py"
line_start: 127
line_end: 147
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.nnet_input.DynamicNNetInput.__init_subclass__"
  - "func:deepxube.base.nnet_input.DynamicNNetInput.register_nnet_input"
  - "func:deepxube.base.nnet_input.DynamicNNetInput.get_dynamic_nnet_inputs"
attributes:
  - name: "_nnet_input_register"
    annotation: "ClassVar[Dict[str, Type[NNetInput]]]"
    default: "dict()"
    from: "class_body"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.nnet_input.DynamicNNetInput`

**File:** [deepxube/base/nnet_input.py:127](../../../deepxube/base/nnet_input.py#L127)
**Abstract:** yes

## Docstring

Domain mixin: subclass declares which concrete ``NNetInput`` classes
it offers. A subclass-local registry is created in ``__init_subclass__``. 

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init_subclass__` *(trivial, skipped)*
- `register_nnet_input` *(trivial, skipped)*
- `get_dynamic_nnet_inputs` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `_nnet_input_register` | `ClassVar[Dict[str, Type[NNetInput]]]` | class_body |

## Source

```python
class DynamicNNetInput(Domain[S, A, G], ABC):
    """ Domain mixin: subclass declares which concrete ``NNetInput`` classes
    it offers. A subclass-local registry is created in ``__init_subclass__``. """

    _nnet_input_register: ClassVar[Dict[str, Type[NNetInput]]] = dict()

    def __init_subclass__(cls, **kwargs: Any):
        """ Give every subclass its own fresh ``_nnet_input_register`` dict. """
        super().__init_subclass__(**kwargs)
        # Create a fresh dict for THIS subclass
        cls._nnet_input_register = {}

    @classmethod
    def register_nnet_input(cls, nnet_input_t: Type[NNetInput], nnet_input_name: str) -> None:
        """ Record ``nnet_input_t`` under ``nnet_input_name`` in the subclass registry. """
        cls._nnet_input_register[nnet_input_name] = nnet_input_t

    @classmethod
    def get_dynamic_nnet_inputs(cls) -> Dict[str, Type[NNetInput]]:
        """ :return: A copy of this subclass's registered ``{nnet_input_name: cls}`` map. """
        return cls._nnet_input_register.copy()
```
