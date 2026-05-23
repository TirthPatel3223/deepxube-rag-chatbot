---
id: "func:deepxube.domains.cube3.Cube3.rev_action"
kind: "method"
name: "rev_action"
qualified_name: "deepxube.domains.cube3.Cube3.rev_action"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 596
line_end: 608
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
  - name: "states"
    annotation: "List[Cube3State]"
    default: null
  - name: "actions"
    annotation: "List[Cube3Action]"
    default: null
returns: "List[Cube3Action]"
docstring_source: "present"
callees:
  - target: null
    expr: "actions_rev.append"
    call_sites: [606]
  - target: "func:deepxube.domains.cube3.Cube3Action"
    expr: "Cube3Action"
    call_sites: [606]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3.rev_action`

**File:** [deepxube/domains/cube3.py:596](../../../../deepxube/domains/cube3.py#L596)
**Class:** `Cube3`
**Visibility:** public
**Kind:** method

## Signature

```python
def rev_action(self, states: List[Cube3State], actions: List[Cube3Action]) -> List[Cube3Action]
```

## Docstring

:return: Reverse of each action (even index ↔ odd index neighbour). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[Cube3State]` | — |
| `actions` | `List[Cube3Action]` | — |

## Returns

`List[Cube3Action]`

## Calls

- `Cube3Action` → `func:deepxube.domains.cube3.Cube3Action` (lines: 606)

### Unresolved
- `actions_rev.append` (lines: 606)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def rev_action(self, states: List[Cube3State], actions: List[Cube3Action]) -> List[Cube3Action]:
        """ :return: Reverse of each action (even index ↔ odd index neighbour). """
        actions_rev: List[Cube3Action] = []
        for action in actions:
            action_val: int = action.action
            action_val_rev: int
            if action_val % 2 == 0:
                action_val_rev = action_val + 1
            else:
                action_val_rev = action_val - 1
            actions_rev.append(Cube3Action(action_val_rev))

        return actions_rev
```
