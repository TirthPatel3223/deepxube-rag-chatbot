---
id: "func:tests.test_domains.domain_name"
kind: "function"
name: "domain_name"
qualified_name: "tests.test_domains.domain_name"
module: "tests.test_domains"
file: "tests/test_domains.py"
line_start: 19
line_end: 20
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators:
  - "@pytest.fixture(params=DOMAIN_NAMES, ids=lambda dom_name: dom_name)"
parameters:
  - name: "request"
    annotation: null
    default: null
returns: "str"
docstring_source: "missing"
callees:
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [20]
raises: []
reads_attrs: []
writes_attrs: []
---

# `tests.test_domains.domain_name`

**File:** [tests/test_domains.py:19](../../../../tests/test_domains.py#L19)
**Visibility:** public
**Kind:** function
**Decorators:** `@pytest.fixture(params=DOMAIN_NAMES, ids=lambda dom_name: dom_name)`

## Signature

```python
def domain_name(request) -> str
```

## Docstring

*(No docstring present — listed in `missing_docstrings.md`.)*

## Parameters

| Name | Type | Default |
|------|------|---------|
| `request` | — | — |

## Returns

`str`

## Calls

- `cast` → `func:typing.cast` (lines: 20)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def domain_name(request) -> str:  # type: ignore
    return cast(str, request.param)
```
