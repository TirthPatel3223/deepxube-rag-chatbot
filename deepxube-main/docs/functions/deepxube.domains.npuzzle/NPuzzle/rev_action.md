---
id: "func:deepxube.domains.npuzzle.NPuzzle.rev_action"
kind: "method"
name: "rev_action"
qualified_name: "deepxube.domains.npuzzle.NPuzzle.rev_action"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 163
line_end: 175
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
  - name: "states"
    annotation: "List[NPState]"
    default: null
  - name: "actions"
    annotation: "List[NPAction]"
    default: null
returns: "List[NPAction]"
docstring_source: "present"
callees:
  - target: null
    expr: "actions_rev.append"
    call_sites: [173]
  - target: "func:deepxube.domains.npuzzle.NPAction"
    expr: "NPAction"
    call_sites: [173]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle.rev_action`

**File:** [deepxube/domains/npuzzle.py:163](../../../../deepxube/domains/npuzzle.py#L163)
**Class:** `NPuzzle`
**Visibility:** public
**Kind:** method

## Signature

```python
def rev_action(self, states: List[NPState], actions: List[NPAction]) -> List[NPAction]
```

## Docstring

:return: Reverse of each action (U↔D, L↔R). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[NPState]` | — |
| `actions` | `List[NPAction]` | — |

## Returns

`List[NPAction]`

## Calls

- `NPAction` → `func:deepxube.domains.npuzzle.NPAction` (lines: 173)

### Unresolved
- `actions_rev.append` (lines: 173)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def rev_action(self, states: List[NPState], actions: List[NPAction]) -> List[NPAction]:
        """ :return: Reverse of each action (U↔D, L↔R). """
        actions_rev: List[NPAction] = []
        for action in actions:
            action_val: int = action.action
            action_val_rev: int
            if action_val % 2 == 0:
                action_val_rev = action_val + 1
            else:
                action_val_rev = action_val - 1
            actions_rev.append(NPAction(action_val_rev))

        return actions_rev
```
