---
id: "func:deepxube.utils.command_line_utils.get_domain_from_arg"
kind: "function"
name: "get_domain_from_arg"
qualified_name: "deepxube.utils.command_line_utils.get_domain_from_arg"
module: "deepxube.utils.command_line_utils"
file: "deepxube/utils/command_line_utils.py"
line_start: 38
line_end: 46
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "domain"
    annotation: "str"
    default: null
returns: "Tuple[Domain, str]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.command_line_utils.get_name_args"
    expr: "get_name_args"
    call_sites: [44]
  - target: "func:deepxube.factories.domain_factory.domain_factory.get_kwargs"
    expr: "domain_factory.get_kwargs"
    call_sites: [45]
  - target: "func:deepxube.factories.domain_factory.domain_factory.build_class"
    expr: "domain_factory.build_class"
    call_sites: [46]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.utils.command_line_utils.get_domain_from_arg`

**File:** [deepxube/utils/command_line_utils.py:38](../../../../deepxube/utils/command_line_utils.py#L38)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_domain_from_arg(domain: str) -> Tuple[Domain, str]
```

## Docstring

Resolve a ``--domain`` CLI argument into a ``Domain`` instance.

:param domain: CLI string, e.g. ``"grid.7"``.
:return: Tuple of (instantiated ``Domain``, registration name).

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `str` | — |

## Returns

`Tuple[Domain, str]`

## Calls

- `get_name_args` → `func:deepxube.utils.command_line_utils.get_name_args` (lines: 44)
- `domain_factory.get_kwargs` → `func:deepxube.factories.domain_factory.domain_factory.get_kwargs` (lines: 45)
- `domain_factory.build_class` → `func:deepxube.factories.domain_factory.domain_factory.build_class` (lines: 46)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_domain_from_arg(domain: str) -> Tuple[Domain, str]:
    """ Resolve a ``--domain`` CLI argument into a ``Domain`` instance.

    :param domain: CLI string, e.g. ``"grid.7"``.
    :return: Tuple of (instantiated ``Domain``, registration name).
    """
    domain_name, domain_args = get_name_args(domain)
    domain_kwargs: Dict[str, Any] = domain_factory.get_kwargs(domain_name, domain_args)
    return domain_factory.build_class(domain_name, domain_kwargs), domain_name
```
