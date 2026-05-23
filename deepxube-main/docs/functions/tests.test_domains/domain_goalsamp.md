---
id: "func:tests.test_domains.domain_goalsamp"
kind: "function"
name: "domain_goalsamp"
qualified_name: "tests.test_domains.domain_goalsamp"
module: "tests.test_domains"
file: "tests/test_domains.py"
line_start: 33
line_end: 35
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators:
  - "@pytest.fixture(params=[dom_id for dom_id in DOMAIN_NAMES if issubclass(domain_factory.get_type(dom_id), GoalSampleable)], ids=lambda dom_id: dom_id)"
parameters:
  - name: "request"
    annotation: null
    default: null
returns: "Domain"
docstring_source: "present"
callees:
  - target: "func:tests.test_domains.build_domain_from_name"
    expr: "build_domain_from_name"
    call_sites: [35]
raises: []
reads_attrs: []
writes_attrs: []
---

# `tests.test_domains.domain_goalsamp`

**File:** [tests/test_domains.py:33](../../../../tests/test_domains.py#L33)
**Visibility:** public
**Kind:** function
**Decorators:** `@pytest.fixture(params=[dom_id for dom_id in DOMAIN_NAMES if issubclass(domain_factory.get_type(dom_id), GoalSampleable)], ids=lambda dom_id: dom_id)`

## Signature

```python
def domain_goalsamp(request) -> Domain
```

## Docstring

:return: Domain instance restricted to domains that support ``GoalSampleable``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `request` | — | — |

## Returns

`Domain`

## Calls

- `build_domain_from_name` → `func:tests.test_domains.build_domain_from_name` (lines: 35)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def domain_goalsamp(request) -> Domain:  # type: ignore
    """ :return: Domain instance restricted to domains that support ``GoalSampleable``. """
    return build_domain_from_name(request.param)
```
