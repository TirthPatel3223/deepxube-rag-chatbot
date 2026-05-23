---
id: "func:tests.test_domains.domain_goalsamp_fromstate"
kind: "function"
name: "domain_goalsamp_fromstate"
qualified_name: "tests.test_domains.domain_goalsamp_fromstate"
module: "tests.test_domains"
file: "tests/test_domains.py"
line_start: 42
line_end: 44
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators:
  - "@pytest.fixture(params=[dom_id for dom_id in DOMAIN_NAMES if issubclass(domain_factory.get_type(dom_id), GoalSampleableFromState)], ids=lambda dom_id: dom_id)"
parameters:
  - name: "request"
    annotation: null
    default: null
returns: "Domain"
docstring_source: "present"
callees:
  - target: "func:tests.test_domains.build_domain_from_name"
    expr: "build_domain_from_name"
    call_sites: [44]
raises: []
reads_attrs: []
writes_attrs: []
---

# `tests.test_domains.domain_goalsamp_fromstate`

**File:** [tests/test_domains.py:42](../../../../tests/test_domains.py#L42)
**Visibility:** public
**Kind:** function
**Decorators:** `@pytest.fixture(params=[dom_id for dom_id in DOMAIN_NAMES if issubclass(domain_factory.get_type(dom_id), GoalSampleableFromState)], ids=lambda dom_id: dom_id)`

## Signature

```python
def domain_goalsamp_fromstate(request) -> Domain
```

## Docstring

:return: Domain instance restricted to domains that support ``GoalSampleableFromState``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `request` | — | — |

## Returns

`Domain`

## Calls

- `build_domain_from_name` → `func:tests.test_domains.build_domain_from_name` (lines: 44)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def domain_goalsamp_fromstate(request) -> Domain:  # type: ignore
    """ :return: Domain instance restricted to domains that support ``GoalSampleableFromState``. """
    return build_domain_from_name(request.param)
```
