---
id: "func:deepxube.domains.sokoban.Sokoban.string_to_action"
kind: "method"
name: "string_to_action"
qualified_name: "deepxube.domains.sokoban.Sokoban.string_to_action"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 261
line_end: 267
class: "Sokoban"
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
returns: "Optional[SkAction]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.sokoban.SkAction"
    expr: "SkAction"
    call_sites: [263]
  - target: null
    expr: "act_str_to_act.keys"
    call_sites: [264]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.sokoban.Sokoban.string_to_action`

**File:** [deepxube/domains/sokoban.py:261](../../../../deepxube/domains/sokoban.py#L261)
**Class:** `Sokoban`
**Visibility:** public
**Kind:** method

## Signature

```python
def string_to_action(self, act_str: str) -> Optional[SkAction]
```

## Docstring

:return: ``SkAction`` for ``'w'``/``'s'``/``'a'``/``'d'``, or ``None`` if unrecognised. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `act_str` | `str` | — |

## Returns

`Optional[SkAction]`

## Calls

- `SkAction` → `func:deepxube.domains.sokoban.SkAction` (lines: 263)

### Unresolved
- `act_str_to_act.keys` (lines: 264)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def string_to_action(self, act_str: str) -> Optional[SkAction]:
        """ :return: ``SkAction`` for ``'w'``/``'s'``/``'a'``/``'d'``, or ``None`` if unrecognised. """
        act_str_to_act: Dict[str, SkAction] = {"w": SkAction(0), "s": SkAction(1), "a": SkAction(2), "d": SkAction(3)}
        if act_str in act_str_to_act.keys():
            return act_str_to_act[act_str]
        else:
            return None
```
