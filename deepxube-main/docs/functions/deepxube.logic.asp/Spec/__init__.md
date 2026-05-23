---
id: "func:deepxube.logic.asp.Spec.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.logic.asp.Spec.__init__"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 41
line_end: 80
class: "Spec"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "goal_true"
    annotation: "Optional[List[Clause]]"
    default: "None"
  - name: "goal_false"
    annotation: "Optional[List[Clause]]"
    default: "None"
  - name: "atoms_true"
    annotation: "Optional[List[Atom]]"
    default: "None"
  - name: "atoms_false"
    annotation: "Optional[List[Atom]]"
    default: "None"
  - name: "models_banned"
    annotation: "Optional[List[Model]]"
    default: "None"
  - name: "num_atoms_gt"
    annotation: "Optional[int]"
    default: "None"
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "goal_true.copy"
    call_sites: [59]
  - target: null
    expr: "goal_false.copy"
    call_sites: [61]
  - target: null
    expr: "atoms_true.copy"
    call_sites: [63]
  - target: null
    expr: "atoms_false.copy"
    call_sites: [65]
  - target: null
    expr: "models_banned.copy"
    call_sites: [67]
  - target: "func:deepxube.logic.logic_objects.Literal"
    expr: "Literal"
    call_sites: [71, 79]
  - target: null
    expr: "str"
    call_sites: [71]
  - target: null
    expr: "len"
    call_sites: [72]
  - target: "func:deepxube.logic.logic_objects.Clause"
    expr: "Clause"
    call_sites: [75, 79]
  - target: null
    expr: "goal_true_new.append"
    call_sites: [76]
  - target: null
    expr: "tuple"
    call_sites: [79]
raises: []
reads_attrs:
  - "self.atoms_false"
  - "self.atoms_true"
  - "self.goal_false"
  - "self.goal_true"
  - "self.models_banned"
writes_attrs:
  - "self.atoms_false"
  - "self.atoms_true"
  - "self.goal_false"
  - "self.goal_true"
  - "self.models_banned"
---

# `deepxube.logic.asp.Spec.__init__`

**File:** [deepxube/logic/asp.py:41](../../../../deepxube/logic/asp.py#L41)
**Class:** `Spec`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, goal_true: Optional[List[Clause]] = None, goal_false: Optional[List[Clause]] = None, atoms_true: Optional[List[Atom]] = None, atoms_false: Optional[List[Atom]] = None, models_banned: Optional[List[Model]] = None, num_atoms_gt: Optional[int] = None)
```

## Docstring

:param goal_true: Must be true. Clauses must have goal in the head.
:param goal_false: Must be false. Clauses must have goal in the head.
:param atoms_true: will only return stable models that are a superset (including equality) of given atoms
:param atoms_false: will not return stable models that contain given atoms
:param models_banned: will not return a stable model that is a superset (including equality) of given models
:param num_atoms_gt: Number of atoms in model found must be greater than given number

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `goal_true` | `Optional[List[Clause]]` | `None` |
| `goal_false` | `Optional[List[Clause]]` | `None` |
| `atoms_true` | `Optional[List[Atom]]` | `None` |
| `atoms_false` | `Optional[List[Atom]]` | `None` |
| `models_banned` | `Optional[List[Model]]` | `None` |
| `num_atoms_gt` | `Optional[int]` | `None` |

## Returns

*(Not annotated.)*

## Calls

- `Literal` → `func:deepxube.logic.logic_objects.Literal` (lines: 71, 79)
- `Clause` → `func:deepxube.logic.logic_objects.Clause` (lines: 75, 79)

### Unresolved
- `goal_true.copy` (lines: 59)
- `goal_false.copy` (lines: 61)
- `atoms_true.copy` (lines: 63)
- `atoms_false.copy` (lines: 65)
- `models_banned.copy` (lines: 67)
- `str` (lines: 71)
- `len` (lines: 72)
- `goal_true_new.append` (lines: 76)
- `tuple` (lines: 79)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.atoms_false`
- `self.atoms_true`
- `self.goal_false`
- `self.goal_true`
- `self.models_banned`

**Reads:**
- `self.atoms_false`
- `self.atoms_true`
- `self.goal_false`
- `self.goal_true`
- `self.models_banned`

## Source

```python
    def __init__(self, goal_true: Optional[List[Clause]] = None, goal_false: Optional[List[Clause]] = None,
                 atoms_true: Optional[List[Atom]] = None, atoms_false: Optional[List[Atom]] = None,
                 models_banned: Optional[List[Model]] = None, num_atoms_gt: Optional[int] = None):
        """
        :param goal_true: Must be true. Clauses must have goal in the head.
        :param goal_false: Must be false. Clauses must have goal in the head.
        :param atoms_true: will only return stable models that are a superset (including equality) of given atoms
        :param atoms_false: will not return stable models that contain given atoms
        :param models_banned: will not return a stable model that is a superset (including equality) of given models
        :param num_atoms_gt: Number of atoms in model found must be greater than given number
        """

        self.goal_true: List[Clause] = []
        self.goal_false: List[Clause] = []
        self.atoms_true: List[Atom] = []
        self.atoms_false: List[Atom] = []
        self.models_banned: List[Model] = []
        if goal_true is not None:
            self.goal_true = goal_true.copy()
        if goal_false is not None:
            self.goal_false = goal_false.copy()
        if atoms_true is not None:
            self.atoms_true = atoms_true.copy()
        if atoms_false is not None:
            self.atoms_false = atoms_false.copy()
        if models_banned is not None:
            self.models_banned = models_banned.copy()

        if num_atoms_gt is not None:
            # add num_atoms_gt to goal
            lit_count_gt: Literal = Literal("count_model_grnd_atoms_gt", (str(num_atoms_gt),), ("in",))
            if len(self.goal_true) > 0:
                goal_true_new = []
                for clause in self.goal_true:
                    clause_new = Clause(clause.head, clause.body + (lit_count_gt,))
                    goal_true_new.append(clause_new)
                self.goal_true = goal_true_new
            else:
                clause_new = Clause(Literal("goal", tuple(), tuple()), (lit_count_gt,))
                self.goal_true = [clause_new]
```
