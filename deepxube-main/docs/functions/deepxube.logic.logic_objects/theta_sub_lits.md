---
id: "func:deepxube.logic.logic_objects.theta_sub_lits"
kind: "function"
name: "theta_sub_lits"
qualified_name: "deepxube.logic.logic_objects.theta_sub_lits"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 304
line_end: 362
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "lits1"
    annotation: "List[Literal]"
    default: null
  - name: "lits2_dict"
    annotation: "Dict[str, List[Literal]]"
    default: null
  - name: "negate_l"
    annotation: "List[bool]"
    default: null
  - name: "subs_prev"
    annotation: "Dict[str, str]"
    default: null
  - name: "subs_forbid"
    annotation: "Dict[str, List[str]]"
    default: null
returns: "Optional[Dict[str, str]]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [308, 316, 332, 339]
  - target: null
    expr: "lits2_dict.get"
    call_sites: [315]
  - target: "func:deepxube.logic.logic_objects.theta_sub_lits"
    expr: "theta_sub_lits"
    call_sites: [318, 334, 344, 355, 360]
  - target: null
    expr: "enumerate"
    call_sites: [324]
  - target: null
    expr: "subs_prev.get"
    call_sites: [325]
  - target: null
    expr: "idxs_vars_req.append"
    call_sites: [327]
  - target: null
    expr: "idxs_not_subbed.append"
    call_sites: [329]
  - target: "func:deepxube.logic.logic_objects.prune_lit"
    expr: "prune_lit"
    call_sites: [331]
  - target: "func:deepxube.logic.logic_objects.theta_sub_args"
    expr: "theta_sub_args"
    call_sites: [349]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.logic_objects.theta_sub_lits`

**File:** [deepxube/logic/logic_objects.py:304](../../../../deepxube/logic/logic_objects.py#L304)
**Visibility:** public
**Kind:** function

## Signature

```python
def theta_sub_lits(lits1: List[Literal], lits2_dict: Dict[str, List[Literal]], negate_l: List[bool], subs_prev: Dict[str, str], subs_forbid: Dict[str, List[str]]) -> Optional[Dict[str, str]]
```

## Docstring

Recursive theta-subsumption check over a literal list; :return: extended substitution dict, or ``None``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `lits1` | `List[Literal]` | — |
| `lits2_dict` | `Dict[str, List[Literal]]` | — |
| `negate_l` | `List[bool]` | — |
| `subs_prev` | `Dict[str, str]` | — |
| `subs_forbid` | `Dict[str, List[str]]` | — |

## Returns

`Optional[Dict[str, str]]`

## Calls

- `theta_sub_lits` → `func:deepxube.logic.logic_objects.theta_sub_lits` (lines: 318, 334, 344, 355, 360)
- `prune_lit` → `func:deepxube.logic.logic_objects.prune_lit` (lines: 331)
- `theta_sub_args` → `func:deepxube.logic.logic_objects.theta_sub_args` (lines: 349)

### Unresolved
- `len` (lines: 308, 316, 332, 339)
- `lits2_dict.get` (lines: 315)
- `enumerate` (lines: 324)
- `subs_prev.get` (lines: 325)
- `idxs_vars_req.append` (lines: 327)
- `idxs_not_subbed.append` (lines: 329)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def theta_sub_lits(lits1: List[Literal], lits2_dict: Dict[str, List[Literal]], negate_l: List[bool],
                   subs_prev: Dict[str, str], subs_forbid: Dict[str, List[str]]) -> Optional[Dict[str, str]]:
    """ Recursive theta-subsumption check over a literal list; :return: extended substitution dict, or ``None``. """
    # TODO handle negative literals
    if len(lits1) == 0:
        return subs_prev

    # TODO, negation as failure not really theta subsumption
    lit1: Literal = lits1[0]
    negate: bool = negate_l[0]

    lits2: List[Literal] = lits2_dict.get(lit1.predicate, [])
    if len(lits2) == 0:
        if negate:
            return theta_sub_lits(lits1[1:], lits2_dict, negate_l[1:], subs_prev, subs_forbid)
        else:
            return None

    idxs_not_subbed: List[int] = []
    idxs_vars_req: List[Tuple[int, str]] = []
    for i, x in enumerate(lit1.arguments):
        var_sub: Optional[str] = subs_prev.get(x)
        if var_sub is not None:
            idxs_vars_req.append((i, var_sub))
        else:
            idxs_not_subbed.append(i)

    lits2 = [x for x in lits2 if not prune_lit(lit1, x, idxs_vars_req)]
    if len(lits2) == 0:
        if negate:
            return theta_sub_lits(lits1[1:], lits2_dict, negate_l[1:], subs_prev, subs_forbid)
        else:
            return None

    subs_rec: Optional[Dict[str, str]]
    if len(idxs_not_subbed) == 0:
        # succeeded somewhere and no substitutions needed
        if negate:
            return None
        else:
            subs_rec = theta_sub_lits(lits1[1:], lits2_dict, negate_l[1:], subs_prev, subs_forbid)
            if subs_rec is not None:
                return subs_rec
    else:
        for lit2 in lits2:
            subs: Optional[Dict[str, str]] = theta_sub_args(lit1.arguments, lit2.arguments, idxs_not_subbed,
                                                            subs_prev, subs_forbid)
            if subs is not None:
                if negate:
                    return None
                else:
                    subs_rec = theta_sub_lits(lits1[1:], lits2_dict, negate_l[1:], subs, subs_forbid)
                    if subs_rec is not None:
                        return subs_rec

    if negate:
        return theta_sub_lits(lits1[1:], lits2_dict, negate_l[1:], subs_prev, subs_forbid)
    else:
        return None
```
