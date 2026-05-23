---
id: "func:deepxube.domains.cube3.Cube3.string_to_action"
kind: "method"
name: "string_to_action"
qualified_name: "deepxube.domains.cube3.Cube3.string_to_action"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 583
line_end: 588
class: "Cube3"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "act_str"
    annotation: "str"
    default: null
returns: "Optional[Cube3Action]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.cube3.Cube3Action"
    expr: "Cube3Action"
    call_sites: [586]
  - target: null
    expr: "self.atomic_actions.index"
    call_sites: [586]
raises: []
reads_attrs:
  - "self.atomic_actions"
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3.string_to_action`

**File:** [deepxube/domains/cube3.py:583](../../../../deepxube/domains/cube3.py#L583)
**Class:** `Cube3`
**Visibility:** public
**Kind:** method

## Signature

```python
def string_to_action(self, act_str: str) -> Optional[Cube3Action]
```

## Docstring

:return: ``Cube3Action`` for strings like ``'U1'`` or ``'F-1'``, or ``None`` if unrecognised. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `act_str` | `str` | — |

## Returns

`Optional[Cube3Action]`

## Calls

- `Cube3Action` → `func:deepxube.domains.cube3.Cube3Action` (lines: 586)

### Unresolved
- `self.atomic_actions.index` (lines: 586)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.atomic_actions`

## Source

```python
    def string_to_action(self, act_str: str) -> Optional[Cube3Action]:
        """ :return: ``Cube3Action`` for strings like ``'U1'`` or ``'F-1'``, or ``None`` if unrecognised. """
        if act_str in self.atomic_actions:
            return Cube3Action(self.atomic_actions.index(act_str))
        else:
            return None
```
