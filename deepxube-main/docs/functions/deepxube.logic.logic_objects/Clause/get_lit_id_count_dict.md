---
id: "func:deepxube.logic.logic_objects.Clause.get_lit_id_count_dict"
kind: "method"
name: "get_lit_id_count_dict"
qualified_name: "deepxube.logic.logic_objects.Clause.get_lit_id_count_dict"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 157
line_end: 168
class: "Clause"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "Dict[Tuple[str, int, bool], int]"
docstring_source: "present"
callees:
  - target: null
    expr: "dict"
    call_sites: [159]
  - target: null
    expr: "list"
    call_sites: [160]
  - target: null
    expr: "lit.get_pred_arity_pos_id"
    call_sites: [162]
raises: []
reads_attrs:
  - "self.body"
  - "self.head"
writes_attrs: []
---

# `deepxube.logic.logic_objects.Clause.get_lit_id_count_dict`

**File:** [deepxube/logic/logic_objects.py:157](../../../../deepxube/logic/logic_objects.py#L157)
**Class:** `Clause`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_lit_id_count_dict(self) -> Dict[Tuple[str, int, bool], int]
```

## Docstring

:return: Dict mapping ``(predicate, arity, positive)`` to occurrence count across head + body. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`Dict[Tuple[str, int, bool], int]`

## Calls

*(No resolved calls.)*

### Unresolved
- `dict` (lines: 159)
- `list` (lines: 160)
- `lit.get_pred_arity_pos_id` (lines: 162)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.body`
- `self.head`

## Source

```python
    def get_lit_id_count_dict(self) -> Dict[Tuple[str, int, bool], int]:
        """ :return: Dict mapping ``(predicate, arity, positive)`` to occurrence count across head + body. """
        lit_pred_dict: Dict[Tuple[str, int, bool], int] = dict()
        for lit in [self.head] + list(self.body):
            if lit is not None:
                lit_tup: Tuple[str, int, bool] = lit.get_pred_arity_pos_id()
                if lit_tup not in lit_pred_dict:
                    lit_pred_dict[lit_tup] = 0

                lit_pred_dict[lit_tup] += 1

        return lit_pred_dict
```
