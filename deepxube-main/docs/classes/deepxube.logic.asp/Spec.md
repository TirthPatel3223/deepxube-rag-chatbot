---
id: "class:deepxube.logic.asp.Spec"
kind: "class"
name: "Spec"
qualified_name: "deepxube.logic.asp.Spec"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 38
line_end: 88
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.logic.asp.Spec.__init__"
  - "func:deepxube.logic.asp.Spec.add"
attributes:
  - name: "self.atoms_false"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.atoms_true"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.goal_false"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.goal_true"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.models_banned"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.logic.asp.Spec`

**File:** [deepxube/logic/asp.py:38](../../../deepxube/logic/asp.py#L38)
**Abstract:** no

## Docstring

Declarative specification that constrains which stable models ``Solver`` will sample or check. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `add`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.atoms_false` | — | __init__ |
| `self.atoms_true` | — | __init__ |
| `self.goal_false` | — | __init__ |
| `self.goal_true` | — | __init__ |
| `self.models_banned` | — | __init__ |

## Source

```python
class Spec:
    """ Declarative specification that constrains which stable models ``Solver`` will sample or check. """

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

    def add(self, spec_add: 'Spec') -> 'Spec':
        """ :return: A new ``Spec`` that is the union of this spec and ``spec_add``. """
        return Spec(goal_true=self.goal_true + spec_add.goal_true,
                    goal_false=self.goal_false + spec_add.goal_false,
                    atoms_true=self.atoms_true + spec_add.atoms_true,
                    atoms_false=self.atoms_false + spec_add.atoms_false,
                    models_banned=self.models_banned + spec_add.models_banned)
```
