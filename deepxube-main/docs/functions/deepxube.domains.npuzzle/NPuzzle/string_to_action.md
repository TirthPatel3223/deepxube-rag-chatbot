---
id: "func:deepxube.domains.npuzzle.NPuzzle.string_to_action"
kind: "method"
name: "string_to_action"
qualified_name: "deepxube.domains.npuzzle.NPuzzle.string_to_action"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 224
line_end: 230
class: "NPuzzle"
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
returns: "Optional[NPAction]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.npuzzle.NPAction"
    expr: "NPAction"
    call_sites: [226]
  - target: null
    expr: "act_str_to_act.keys"
    call_sites: [227]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle.string_to_action`

**File:** [deepxube/domains/npuzzle.py:224](../../../../deepxube/domains/npuzzle.py#L224)
**Class:** `NPuzzle`
**Visibility:** public
**Kind:** method

## Signature

```python
def string_to_action(self, act_str: str) -> Optional[NPAction]
```

## Docstring

:return: ``NPAction`` for ``'w'``/``'s'``/``'a'``/``'d'``, or ``None`` if unrecognised. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `act_str` | `str` | — |

## Returns

`Optional[NPAction]`

## Calls

- `NPAction` → `func:deepxube.domains.npuzzle.NPAction` (lines: 226)

### Unresolved
- `act_str_to_act.keys` (lines: 227)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def string_to_action(self, act_str: str) -> Optional[NPAction]:
        """ :return: ``NPAction`` for ``'w'``/``'s'``/``'a'``/``'d'``, or ``None`` if unrecognised. """
        act_str_to_act: Dict[str, NPAction] = {"w": NPAction(0), "s": NPAction(1), "a": NPAction(2), "d": NPAction(3)}
        if act_str in act_str_to_act.keys():
            return act_str_to_act[act_str]
        else:
            return None
```
