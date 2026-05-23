---
id: "func:deepxube.logic.asp.Solver._add_goal"
kind: "method"
name: "_add_goal"
qualified_name: "deepxube.logic.asp.Solver._add_goal"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 227
line_end: 254
class: "Solver"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "goal"
    annotation: "List[Clause]"
    default: null
returns: "str"
docstring_source: "present"
callees:
  - target: null
    expr: "all"
    call_sites: [233, 234]
  - target: null
    expr: "len"
    call_sites: [234, 239]
  - target: null
    expr: "frozenset"
    call_sites: [236]
  - target: null
    expr: "self.goals_added.get"
    call_sites: [237]
  - target: "func:deepxube.logic.logic_utils.copy_clause_with_new_head"
    expr: "copy_clause_with_new_head"
    call_sites: [244]
  - target: null
    expr: "self.ctl_rand.add"
    call_sites: [245]
  - target: null
    expr: "goal_clause_new_head.to_code"
    call_sites: [245, 246]
  - target: null
    expr: "self.ctl_min.add"
    call_sites: [246]
  - target: null
    expr: "self.ctl_rand.ground"
    call_sites: [247]
  - target: null
    expr: "self.ctl_min.ground"
    call_sites: [248]
raises: []
reads_attrs:
  - "self.ctl_min"
  - "self.ctl_rand"
  - "self.goals_added"
writes_attrs: []
---

# `deepxube.logic.asp.Solver._add_goal`

**File:** [deepxube/logic/asp.py:227](../../../../deepxube/logic/asp.py#L227)
**Class:** `Solver`
**Visibility:** private
**Kind:** method

## Signature

```python
def _add_goal(self, goal: List[Clause]) -> str
```

## Docstring

Adds all goal clauses with same head

:param goal:
:return:

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `goal` | `List[Clause]` | — |

## Returns

`str`

## Calls

- `copy_clause_with_new_head` → `func:deepxube.logic.logic_utils.copy_clause_with_new_head` (lines: 244)

### Unresolved
- `all` (lines: 233, 234)
- `len` (lines: 234, 239)
- `frozenset` (lines: 236)
- `self.goals_added.get` (lines: 237)
- `self.ctl_rand.add` (lines: 245)
- `goal_clause_new_head.to_code` (lines: 245, 246)
- `self.ctl_min.add` (lines: 246)
- `self.ctl_rand.ground` (lines: 247)
- `self.ctl_min.ground` (lines: 248)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.ctl_min`
- `self.ctl_rand`
- `self.goals_added`

## Source

```python
    def _add_goal(self, goal: List[Clause]) -> str:
        """ Adds all goal clauses with same head

        :param goal:
        :return:
        """
        assert all([x.head.predicate == "goal" for x in goal]), "head should be goal"
        assert all([len(x.head.arguments) == 0 for x in goal]), "head should not have any arguments"

        goal_clauses_set: frozenset[Clause] = frozenset(goal)
        goal_new_head_pred_get: Optional[str] = self.goals_added.get(goal_clauses_set)
        if goal_new_head_pred_get is None:
            goal_num: int = len(self.goals_added)
            goal_new_head_pred: str = f"goal{goal_num}"

            prg_blk: str = goal_new_head_pred
            for goal_clause in goal:
                goal_clause_new_head: Clause = copy_clause_with_new_head(goal_clause, goal_new_head_pred)
                self.ctl_rand.add(prg_blk, [], f"{goal_clause_new_head.to_code()}.\n")
                self.ctl_min.add(prg_blk, [], f"{goal_clause_new_head.to_code()}.\n")
            self.ctl_rand.ground([(prg_blk, [])])
            self.ctl_min.ground([(prg_blk, [])])

            self.goals_added[goal_clauses_set] = goal_new_head_pred

            return goal_new_head_pred
        else:
            return goal_new_head_pred_get
```
