---
id: "func:deepxube.logic.logic_objects.theta_sub_replace"
kind: "function"
name: "theta_sub_replace"
qualified_name: "deepxube.logic.logic_objects.theta_sub_replace"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 414
line_end: 429
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "clause1"
    annotation: "Clause"
    default: null
  - name: "clause2"
    annotation: "Clause"
    default: null
  - name: "ignore_head"
    annotation: "bool"
    default: "False"
returns: "Clause"
docstring_source: "present"
callees:
  - target: null
    expr: "clause1.theta_sub"
    call_sites: [417]
  - target: "func:deepxube.logic.logic_objects.Clause"
    expr: "Clause"
    call_sites: [419, 428]
  - target: "func:deepxube.logic.logic_objects.make_subs"
    expr: "make_subs"
    call_sites: [421]
  - target: null
    expr: "set"
    call_sites: [425]
  - target: null
    expr: "lit.to_code"
    call_sites: [425, 426]
  - target: null
    expr: "tuple"
    call_sites: [428]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.logic_objects.theta_sub_replace`

**File:** [deepxube/logic/logic_objects.py:414](../../../../deepxube/logic/logic_objects.py#L414)
**Visibility:** public
**Kind:** function

## Signature

```python
def theta_sub_replace(clause1: Clause, clause2: Clause, ignore_head: bool = False) -> Clause
```

## Docstring

Theta-subsume ``clause1`` into ``clause2`` and rewrite ``clause2`` to use ``clause1``'s variable names where
they match; :return: the rewritten clause (unchanged if no subsumption). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `clause1` | `Clause` | — |
| `clause2` | `Clause` | — |
| `ignore_head` | `bool` | `False` |

## Returns

`Clause`

## Calls

- `Clause` → `func:deepxube.logic.logic_objects.Clause` (lines: 419, 428)
- `make_subs` → `func:deepxube.logic.logic_objects.make_subs` (lines: 421)

### Unresolved
- `clause1.theta_sub` (lines: 417)
- `set` (lines: 425)
- `lit.to_code` (lines: 425, 426)
- `tuple` (lines: 428)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def theta_sub_replace(clause1: Clause, clause2: Clause, ignore_head: bool = False) -> Clause:
    """ Theta-subsume ``clause1`` into ``clause2`` and rewrite ``clause2`` to use ``clause1``'s variable names where
    they match; :return: the rewritten clause (unchanged if no subsumption). """
    subs: Optional[Dict[str, str]] = clause1.theta_sub(clause2, ignore_head=ignore_head)
    if subs is None:
        return Clause(clause2.head, clause2.body)

    clause1 = make_subs(clause1, subs)
    body_new: List[Literal] = [clause1.head]

    # TODO changes in to_code() may break this, what about direction?
    clause1_body_code_set: Set[str] = set(lit.to_code() for lit in clause1.body)
    body_new = body_new + [lit for lit in clause2.body if lit.to_code() not in clause1_body_code_set]

    clause2_new: Clause = Clause(clause2.head, tuple(body_new))
    return clause2_new
```
