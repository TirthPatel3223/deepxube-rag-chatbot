---
id: "func:deepxube.base.factory.Factory.get_kwargs"
kind: "method"
name: "get_kwargs"
qualified_name: "deepxube.base.factory.Factory.get_kwargs"
module: "deepxube.base.factory"
file: "deepxube/base/factory.py"
line_start: 123
line_end: 148
class: "Factory"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "name"
    annotation: "str"
    default: null
  - name: "args_str"
    annotation: "Optional[str]"
    default: null
returns: "Dict[str, Any]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.factory.Factory.get_type"
    expr: "self.get_type"
    call_sites: [137]
  - target: null
    expr: "dict"
    call_sites: [138]
  - target: "func:deepxube.base.factory.Factory.get_parser"
    expr: "self.get_parser"
    call_sites: [139]
  - target: null
    expr: "parser.parse"
    call_sites: [142]
  - target: "func:logging.exception"
    expr: "logging.exception"
    call_sites: [144]
  - target: null
    expr: "ValueError"
    call_sites: [145]
  - target: null
    expr: "parser.help"
    call_sites: [145]
raises:
  - exception: "ValueError"
    call_sites: [145]
reads_attrs:
  - "self._class_type_str"
writes_attrs: []
---

# `deepxube.base.factory.Factory.get_kwargs`

**File:** [deepxube/base/factory.py:123](../../../../deepxube/base/factory.py#L123)
**Class:** `Factory`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_kwargs(self, name: str, args_str: Optional[str]) -> Dict[str, Any]
```

## Docstring

Resolve a CLI argument suffix into constructor keyword arguments.

Asserts that the class ``name`` is registered, then routes ``args_str``
through the corresponding parser if one exists. If no parser is
registered for ``name``, ``args_str`` must be ``None``.

:param name: The registered class name.
:param args_str: The dotted argument suffix following ``name``
    (e.g. ``"7"`` in ``grid.7``), or ``None`` if the argument had no
    suffix.
:return: A dictionary of keyword arguments for the class constructor.
    Empty if no parser exists or ``args_str`` is ``None``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `name` | `str` | — |
| `args_str` | `Optional[str]` | — |

## Returns

`Dict[str, Any]`

## Calls

- `self.get_type` → `func:deepxube.base.factory.Factory.get_type` (lines: 137)
- `self.get_parser` → `func:deepxube.base.factory.Factory.get_parser` (lines: 139)
- `logging.exception` → `func:logging.exception` (lines: 144)

### Unresolved
- `dict` (lines: 138)
- `parser.parse` (lines: 142)
- `ValueError` (lines: 145)
- `parser.help` (lines: 145)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 145)

## Attribute access

**Reads:**
- `self._class_type_str`

## Source

```python
    def get_kwargs(self, name: str, args_str: Optional[str]) -> Dict[str, Any]:
        """ Resolve a CLI argument suffix into constructor keyword arguments.

        Asserts that the class ``name`` is registered, then routes ``args_str``
        through the corresponding parser if one exists. If no parser is
        registered for ``name``, ``args_str`` must be ``None``.

        :param name: The registered class name.
        :param args_str: The dotted argument suffix following ``name``
            (e.g. ``"7"`` in ``grid.7``), or ``None`` if the argument had no
            suffix.
        :return: A dictionary of keyword arguments for the class constructor.
            Empty if no parser exists or ``args_str`` is ``None``.
        """
        self.get_type(name)
        kwargs: Dict[str, Any] = dict()
        parser: Optional[Parser] = self.get_parser(name)
        if (parser is not None) and (args_str is not None):
            try:
                kwargs = parser.parse(args_str)
            except Exception as e:
                logging.exception(f"Error occurred: {e}")
                raise ValueError(f"Error parsing {args_str} for {self._class_type_str} {name!r}.\nParser help:\n{parser.help()}")
        else:
            assert args_str is None, f"No parser for {self._class_type_str} {name}, however, args given are {args_str}"
        return kwargs
```
