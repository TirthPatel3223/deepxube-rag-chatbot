---
id: "func:deepxube.logic.logic_objects.Clause.theta_sub"
kind: "method"
name: "theta_sub"
qualified_name: "deepxube.logic.logic_objects.Clause.theta_sub"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 170
line_end: 205
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
  - name: "other"
    annotation: "'Clause'"
    default: null
  - name: "subs_prev"
    annotation: "Optional[Dict[str, str]]"
    default: "None"
  - name: "negate_l"
    annotation: "Optional[List[bool]]"
    default: "None"
  - name: "subs_forbid"
    annotation: "Optional[Dict[str, List[str]]]"
    default: "None"
  - name: "ignore_head"
    annotation: "bool"
    default: "False"
returns: "Optional[Dict[str, str]]"
docstring_source: "present"
callees:
  - target: null
    expr: "dict"
    call_sites: [179, 181, 189]
  - target: null
    expr: "list"
    call_sites: [183, 184]
  - target: null
    expr: "name_to_lit_other.keys"
    call_sites: [191, 202]
  - target: null
    expr: "name_to_lit_other[lit.predicate].append"
    call_sites: [193]
  - target: null
    expr: "len"
    call_sites: [197, 200]
  - target: null
    expr: "zip"
    call_sites: [201]
  - target: "func:deepxube.logic.logic_objects.theta_sub_lits"
    expr: "theta_sub_lits"
    call_sites: [205]
raises: []
reads_attrs:
  - "self.body"
  - "self.head"
writes_attrs: []
---

# `deepxube.logic.logic_objects.Clause.theta_sub`

**File:** [deepxube/logic/logic_objects.py:170](../../../../deepxube/logic/logic_objects.py#L170)
**Class:** `Clause`
**Visibility:** public
**Kind:** method

## Signature

```python
def theta_sub(self, other: 'Clause', subs_prev: Optional[Dict[str, str]] = None, negate_l: Optional[List[bool]] = None, subs_forbid: Optional[Dict[str, List[str]]] = None, ignore_head: bool = False) -> Optional[Dict[str, str]]
```

## Docstring

:return: A variable-substitution dict if ``self`` theta-subsumes ``other``; ``None`` otherwise. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `other` | `'Clause'` | — |
| `subs_prev` | `Optional[Dict[str, str]]` | `None` |
| `negate_l` | `Optional[List[bool]]` | `None` |
| `subs_forbid` | `Optional[Dict[str, List[str]]]` | `None` |
| `ignore_head` | `bool` | `False` |

## Returns

`Optional[Dict[str, str]]`

## Calls

- `theta_sub_lits` → `func:deepxube.logic.logic_objects.theta_sub_lits` (lines: 205)

### Unresolved
- `dict` (lines: 179, 181, 189)
- `list` (lines: 183, 184)
- `name_to_lit_other.keys` (lines: 191, 202)
- `name_to_lit_other[lit.predicate].append` (lines: 193)
- `len` (lines: 197, 200)
- `zip` (lines: 201)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.body`
- `self.head`

## Source

```python
    def theta_sub(self, other: 'Clause', subs_prev: Optional[Dict[str, str]] = None,
                  negate_l: Optional[List[bool]] = None, subs_forbid: Optional[Dict[str, List[str]]] = None,
                  ignore_head: bool = False) -> Optional[Dict[str, str]]:
        """ :return: A variable-substitution dict if ``self`` theta-subsumes ``other``; ``None`` otherwise. """
        # Initialize
        if ignore_head:
            assert negate_l is None, "Negate not yet integrated with ignore_head"

        if subs_prev is None:
            subs_prev = dict()
        if subs_forbid is None:
            subs_forbid = dict()

        lits_self: List[Literal] = list(self.body)
        lits_other: List[Literal] = list(other.body)
        if not ignore_head:
            lits_self = [self.head] + lits_self
            lits_other = [other.head] + lits_other

        name_to_lit_other: Dict[str, List[Literal]] = dict()
        for lit in lits_other:
            if lit.predicate not in name_to_lit_other.keys():
                name_to_lit_other[lit.predicate] = []
            name_to_lit_other[lit.predicate].append(lit)

        negate_prev = negate_l
        if negate_l is None:
            negate_l = [False] * len(lits_self)

        # check all predicate names in self appears in other
        assert len(lits_self) == len(negate_l), f"{self}, {other}, {len(lits_self)}, {len(negate_l)}, {negate_prev}"
        for lit_self, negate in zip(lits_self, negate_l):
            if (not negate) and (lit_self.predicate not in name_to_lit_other.keys()):
                return None

        return theta_sub_lits(lits_self, name_to_lit_other, negate_l, subs_prev, subs_forbid)
```
