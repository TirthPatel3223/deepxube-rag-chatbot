---
id: "func:deepxube.base.pathfinding.PathFind.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.base.pathfinding.PathFind.__init__"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 276
line_end: 285
class: "PathFind"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "domain"
    annotation: "D"
    default: null
  - name: "functions"
    annotation: "FNs"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "isinstance"
    call_sites: [278, 280]
  - target: "func:deepxube.base.pathfinding.PathFind.domain_type"
    expr: "self.domain_type"
    call_sites: [278]
  - target: "func:deepxube.base.pathfinding.PathFind.functions_type"
    expr: "self.functions_type"
    call_sites: [279, 280]
  - target: "func:deepxube.utils.timing_utils.Times"
    expr: "Times"
    call_sites: [284]
raises: []
reads_attrs:
  - "self.domain"
  - "self.functions"
  - "self.instances"
  - "self.itr"
  - "self.times"
writes_attrs:
  - "self.domain"
  - "self.functions"
  - "self.instances"
  - "self.itr"
  - "self.times"
---

# `deepxube.base.pathfinding.PathFind.__init__`

**File:** [deepxube/base/pathfinding.py:276](../../../../deepxube/base/pathfinding.py#L276)
**Class:** `PathFind`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, domain: D, functions: FNs)
```

## Docstring

Bind to a domain and a function bundle; init empty instance list. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `domain` | `D` | — |
| `functions` | `FNs` | — |

## Returns

*(Not annotated.)*

## Calls

- `self.domain_type` → `func:deepxube.base.pathfinding.PathFind.domain_type` (lines: 278)
- `self.functions_type` → `func:deepxube.base.pathfinding.PathFind.functions_type` (lines: 279, 280)
- `Times` → `func:deepxube.utils.timing_utils.Times` (lines: 284)

### Unresolved
- `isinstance` (lines: 278, 280)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.domain`
- `self.functions`
- `self.instances`
- `self.itr`
- `self.times`

**Reads:**
- `self.domain`
- `self.functions`
- `self.instances`
- `self.itr`
- `self.times`

## Source

```python
    def __init__(self, domain: D, functions: FNs):
        """ Bind to a domain and a function bundle; init empty instance list. """
        assert isinstance(domain, self.domain_type()), f"Domain {domain} must be an instance of {self.domain_type()}."
        if self.functions_type() is not Any:
            assert isinstance(functions, self.functions_type()), f"Functions {functions} must be an instance of {self.functions_type()}."
        self.domain: D = domain
        self.functions: FNs = functions
        self.instances: List[I] = []
        self.times: Times = Times()
        self.itr: int = 0
```
