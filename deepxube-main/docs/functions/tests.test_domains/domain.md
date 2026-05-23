---
id: "func:tests.test_domains.domain"
kind: "function"
name: "domain"
qualified_name: "tests.test_domains.domain"
module: "tests.test_domains"
file: "tests/test_domains.py"
line_start: 24
line_end: 26
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators:
  - "@pytest.fixture"
parameters:
  - name: "domain_name"
    annotation: "str"
    default: null
returns: "Domain"
docstring_source: "present"
callees:
  - target: "func:tests.test_domains.build_domain_from_name"
    expr: "build_domain_from_name"
    call_sites: [26]
raises: []
reads_attrs: []
writes_attrs: []
---

# `tests.test_domains.domain`

**File:** [tests/test_domains.py:24](../../../../tests/test_domains.py#L24)
**Visibility:** public
**Kind:** function
**Decorators:** `@pytest.fixture`

## Signature

```python
def domain(domain_name: str) -> Domain
```

## Docstring

:return: Domain instance built from the parameterised ``domain_name`` fixture. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain_name` | `str` | — |

## Returns

`Domain`

## Calls

- `build_domain_from_name` → `func:tests.test_domains.build_domain_from_name` (lines: 26)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def domain(domain_name: str) -> Domain:
    """ :return: Domain instance built from the parameterised ``domain_name`` fixture. """
    return build_domain_from_name(domain_name)
```
