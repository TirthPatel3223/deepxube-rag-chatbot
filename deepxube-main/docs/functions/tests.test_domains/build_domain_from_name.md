---
id: "func:tests.test_domains.build_domain_from_name"
kind: "function"
name: "build_domain_from_name"
qualified_name: "tests.test_domains.build_domain_from_name"
module: "tests.test_domains"
file: "tests/test_domains.py"
line_start: 13
line_end: 15
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "domain_id"
    annotation: "str"
    default: null
returns: "Domain"
docstring_source: "present"
callees:
  - target: "func:deepxube.factories.domain_factory.domain_factory.build_class"
    expr: "domain_factory.build_class"
    call_sites: [15]
raises: []
reads_attrs: []
writes_attrs: []
---

# `tests.test_domains.build_domain_from_name`

**File:** [tests/test_domains.py:13](../../../../tests/test_domains.py#L13)
**Visibility:** public
**Kind:** function

## Signature

```python
def build_domain_from_name(domain_id: str) -> Domain
```

## Docstring

:return: Default-constructed domain instance for ``domain_id``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain_id` | `str` | — |

## Returns

`Domain`

## Calls

- `domain_factory.build_class` → `func:deepxube.factories.domain_factory.domain_factory.build_class` (lines: 15)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def build_domain_from_name(domain_id: str) -> Domain:
    """ :return: Default-constructed domain instance for ``domain_id``. """
    return domain_factory.build_class(domain_id, {})
```
