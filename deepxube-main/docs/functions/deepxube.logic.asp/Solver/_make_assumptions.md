---
id: "func:deepxube.logic.asp.Solver._make_assumptions"
kind: "method"
name: "_make_assumptions"
qualified_name: "deepxube.logic.asp.Solver._make_assumptions"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 256
line_end: 286
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
  - name: "spec"
    annotation: "Spec"
    default: null
returns: "List[Tuple[Symbol, bool]]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [260, 262, 268]
  - target: null
    expr: "atoms_true.append"
    call_sites: [261]
  - target: "func:deepxube.logic.asp.Solver._add_goal"
    expr: "self._add_goal"
    call_sites: [261, 263, 271]
  - target: null
    expr: "atoms_false.append"
    call_sites: [263, 271]
  - target: "func:deepxube.logic.logic_objects.Literal"
    expr: "Literal"
    call_sites: [268, 270]
  - target: null
    expr: "tuple"
    call_sites: [268, 270]
  - target: "func:deepxube.logic.logic_objects.Clause"
    expr: "Clause"
    call_sites: [270]
  - target: null
    expr: "assumed_true.append"
    call_sites: [276]
  - target: "func:deepxube.logic.logic_utils.atom_to_str"
    expr: "atom_to_str"
    call_sites: [276, 278]
  - target: null
    expr: "assumed_false.append"
    call_sites: [278]
  - target: null
    expr: "assumptions.append"
    call_sites: [282, 284]
  - target: "func:clingo.parse_term"
    expr: "parse_term"
    call_sites: [282, 284]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.asp.Solver._make_assumptions`

**File:** [deepxube/logic/asp.py:256](../../../../deepxube/logic/asp.py#L256)
**Class:** `Solver`
**Visibility:** private
**Kind:** method

## Signature

```python
def _make_assumptions(self, spec: Spec) -> List[Tuple[Symbol, bool]]
```

## Docstring

:return: Clingo ``(Symbol, bool)`` assumption pairs derived from all constraints in ``spec``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `spec` | `Spec` | — |

## Returns

`List[Tuple[Symbol, bool]]`

## Calls

- `self._add_goal` → `func:deepxube.logic.asp.Solver._add_goal` (lines: 261, 263, 271)
- `Literal` → `func:deepxube.logic.logic_objects.Literal` (lines: 268, 270)
- `Clause` → `func:deepxube.logic.logic_objects.Clause` (lines: 270)
- `atom_to_str` → `func:deepxube.logic.logic_utils.atom_to_str` (lines: 276, 278)
- `parse_term` → `func:clingo.parse_term` (lines: 282, 284)

### Unresolved
- `len` (lines: 260, 262, 268)
- `atoms_true.append` (lines: 261)
- `atoms_false.append` (lines: 263, 271)
- `tuple` (lines: 268, 270)
- `assumed_true.append` (lines: 276)
- `assumed_false.append` (lines: 278)
- `assumptions.append` (lines: 282, 284)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _make_assumptions(self, spec: Spec) -> List[Tuple[Symbol, bool]]:
        """ :return: Clingo ``(Symbol, bool)`` assumption pairs derived from all constraints in ``spec``. """
        atoms_true: List[Atom] = []
        atoms_false: List[Atom] = []
        if len(spec.goal_true) > 0:
            atoms_true.append((self._add_goal(spec.goal_true),))
        if len(spec.goal_false) > 0:
            atoms_false.append((self._add_goal(spec.goal_false),))

        atoms_true += spec.atoms_true
        atoms_false += spec.atoms_false
        for model_banned in spec.models_banned:
            blits: List[Literal] = [Literal(atom[0], atom[1:], tuple(["in"] * len(atom[1:]))) for atom in
                                    model_banned]
            clause_banned: Clause = Clause(Literal("goal", tuple(), tuple()), tuple(blits))
            atoms_false.append((self._add_goal([clause_banned]),))

        assumed_true: List[str] = []
        assumed_false: List[str] = []
        for atom in atoms_true:
            assumed_true.append(atom_to_str(atom))
        for atom in atoms_false:
            assumed_false.append(atom_to_str(atom))

        assumptions: List[Tuple[Symbol, bool]] = []
        for lit in assumed_true:
            assumptions.append((parse_term(lit), True))
        for lit in assumed_false:
            assumptions.append((parse_term(lit), False))

        return assumptions
```
