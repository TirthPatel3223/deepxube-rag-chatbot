---
id: "func:deepxube.logic.logic_utils.parse_clause"
kind: "function"
name: "parse_clause"
qualified_name: "deepxube.logic.logic_utils.parse_clause"
module: "deepxube.logic.logic_utils"
file: "deepxube/logic/logic_utils.py"
line_start: 64
line_end: 96
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "constr_str"
    annotation: "str"
    default: null
returns: "Tuple[Clause, Dict[str, List[str]]]"
docstring_source: "present"
callees:
  - target: null
    expr: "constr_str.split"
    call_sites: [67]
  - target: "func:deepxube.logic.logic_utils.parse_literal"
    expr: "parse_literal"
    call_sites: [68, 74]
  - target: null
    expr: "tuple"
    call_sites: [71, 95]
  - target: "func:re.findall"
    expr: "re.findall"
    call_sites: [71, 79]
  - target: null
    expr: "body_lits.append"
    call_sites: [75]
  - target: null
    expr: "dict"
    call_sites: [78]
  - target: null
    expr: "v1.strip"
    call_sites: [81]
  - target: null
    expr: "v2.strip"
    call_sites: [82]
  - target: null
    expr: "subs_forbid[v1].append"
    call_sites: [88]
  - target: null
    expr: "subs_forbid[v2].append"
    call_sites: [89]
  - target: "func:deepxube.logic.logic_utils.replace_anon_vars"
    expr: "replace_anon_vars"
    call_sites: [91, 93]
  - target: null
    expr: "enumerate"
    call_sites: [92]
  - target: "func:deepxube.logic.logic_objects.Clause"
    expr: "Clause"
    call_sites: [95]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.logic_utils.parse_clause`

**File:** [deepxube/logic/logic_utils.py:64](../../../../deepxube/logic/logic_utils.py#L64)
**Visibility:** public
**Kind:** function

## Signature

```python
def parse_clause(constr_str: str) -> Tuple[Clause, Dict[str, List[str]]]
```

## Docstring

Parse a rule string ``'head :- body'`` into a ``(Clause, subs_forbid)`` pair where ``subs_forbid`` captures
``!=`` inequality constraints extracted from the body. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `constr_str` | `str` | — |

## Returns

`Tuple[Clause, Dict[str, List[str]]]`

## Calls

- `parse_literal` → `func:deepxube.logic.logic_utils.parse_literal` (lines: 68, 74)
- `re.findall` → `func:re.findall` (lines: 71, 79)
- `replace_anon_vars` → `func:deepxube.logic.logic_utils.replace_anon_vars` (lines: 91, 93)
- `Clause` → `func:deepxube.logic.logic_objects.Clause` (lines: 95)

### Unresolved
- `constr_str.split` (lines: 67)
- `tuple` (lines: 71, 95)
- `body_lits.append` (lines: 75)
- `dict` (lines: 78)
- `v1.strip` (lines: 81)
- `v2.strip` (lines: 82)
- `subs_forbid[v1].append` (lines: 88)
- `subs_forbid[v2].append` (lines: 89)
- `enumerate` (lines: 92)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def parse_clause(constr_str: str) -> Tuple[Clause, Dict[str, List[str]]]:
    """ Parse a rule string ``'head :- body'`` into a ``(Clause, subs_forbid)`` pair where ``subs_forbid`` captures
    ``!=`` inequality constraints extracted from the body. """
    head_str, body_str = constr_str.split(":-")
    head_lit = parse_literal(head_str)

    # lits
    body_lit_strs: Tuple[str, ...] = tuple(re.findall(r"[^,]+\([^)]+\)|^\s*[^,]+|[^,)]+\s*$", body_str))
    body_lits: List[Literal] = []
    for body_lit_str in body_lit_strs:
        body_lit = parse_literal(body_lit_str)
        body_lits.append(body_lit)

    # subs forbid
    subs_forbid: Dict[str, List[str]] = dict()
    sub_forbid_strs = re.findall(r"\s*([^,]+)\s*!\s*=\s*([^,]+)\s*", body_str)
    for v1, v2 in sub_forbid_strs:
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 not in subs_forbid:
            subs_forbid[v1] = []
        if v2 not in subs_forbid:
            subs_forbid[v2] = []

        subs_forbid[v1].append(v2)
        subs_forbid[v2].append(v1)

    head_lit = replace_anon_vars(head_lit, [head_lit] + body_lits)
    for idx, body_lit in enumerate(body_lits):
        body_lits[idx] = replace_anon_vars(body_lit, [head_lit] + body_lits)

    clause: Clause = Clause(head_lit, tuple(body_lits))
    return clause, subs_forbid
```
