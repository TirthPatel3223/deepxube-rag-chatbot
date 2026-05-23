---
id: "func:tests.test_domains.domain_actsrev"
kind: "function"
name: "domain_actsrev"
qualified_name: "tests.test_domains.domain_actsrev"
module: "tests.test_domains"
file: "tests/test_domains.py"
line_start: 51
line_end: 53
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
    call_sites: [53]
raises: []
reads_attrs: []
writes_attrs: []
---

# `tests.test_domains.domain_actsrev`

**File:** [tests/test_domains.py:51](../../../../tests/test_domains.py#L51)
**Visibility:** public
**Kind:** function
**Decorators:** `@pytest.fixture(params=[dom_id for dom_id in DOMAIN_NAMES if issubclass(domain_factory.get_type(dom_id), GoalSampleable)], ids=lambda dom_id: dom_id)`

## Signature

```python
def domain_actsrev(request) -> Domain
```

## Docstring

:return: Domain instance restricted to domains that support ``GoalSampleable`` (used for ActsRev tests). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `request` | — | — |

## Returns

`Domain`

## Calls

- `build_domain_from_name` → `func:tests.test_domains.build_domain_from_name` (lines: 53)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def domain_actsrev(request) -> Domain:  # type: ignore
    """ :return: Domain instance restricted to domains that support ``GoalSampleable`` (used for ActsRev tests). """
    return build_domain_from_name(request.param)
```
