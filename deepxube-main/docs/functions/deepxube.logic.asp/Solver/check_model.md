---
id: "func:deepxube.logic.asp.Solver.check_model"
kind: "method"
name: "check_model"
qualified_name: "deepxube.logic.asp.Solver.check_model"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 180
line_end: 200
class: "Solver"
visibility: "public"
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
  - name: "model"
    annotation: "Model"
    default: null
  - name: "timeout"
    annotation: "Optional[float]"
    default: "None"
returns: "bool"
docstring_source: "present"
callees:
  - target: "func:deepxube.logic.asp.Spec"
    expr: "Spec"
    call_sites: [189]
  - target: null
    expr: "list"
    call_sites: [189]
  - target: "func:deepxube.logic.asp.Solver._make_assumptions"
    expr: "self._make_assumptions"
    call_sites: [191, 192]
  - target: null
    expr: "self.ctl_rand.solve"
    call_sites: [195]
  - target: null
    expr: "models_ret.append"
    call_sites: [196]
  - target: null
    expr: "solve_handle.wait"
    call_sites: [197]
  - target: null
    expr: "solve_handle.cancel"
    call_sites: [198]
  - target: null
    expr: "len"
    call_sites: [200]
raises: []
reads_attrs:
  - "self.ctl_rand"
  - "self.ground_atoms"
writes_attrs: []
---

# `deepxube.logic.asp.Solver.check_model`

**File:** [deepxube/logic/asp.py:180](../../../../deepxube/logic/asp.py#L180)
**Class:** `Solver`
**Visibility:** public
**Kind:** method

## Signature

```python
def check_model(self, spec: Spec, model: Model, timeout: Optional[float] = None) -> bool
```

## Docstring

:param spec: Specification
:param model: Model to check
:param timeout: Timeout only for solving, not for grounding
:return:

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `spec` | `Spec` | — |
| `model` | `Model` | — |
| `timeout` | `Optional[float]` | `None` |

## Returns

`bool`

## Calls

- `Spec` → `func:deepxube.logic.asp.Spec` (lines: 189)
- `self._make_assumptions` → `func:deepxube.logic.asp.Solver._make_assumptions` (lines: 191, 192)

### Unresolved
- `list` (lines: 189)
- `self.ctl_rand.solve` (lines: 195)
- `models_ret.append` (lines: 196)
- `solve_handle.wait` (lines: 197)
- `solve_handle.cancel` (lines: 198)
- `len` (lines: 200)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.ctl_rand`
- `self.ground_atoms`

## Source

```python
    def check_model(self, spec: Spec, model: Model, timeout: Optional[float] = None) -> bool:
        """

        :param spec: Specification
        :param model: Model to check
        :param timeout: Timeout only for solving, not for grounding
        :return:
        """
        atoms_false: List[Atom] = [atom for atom in self.ground_atoms if atom not in model]
        spec_check: Spec = Spec(atoms_true=list(model), atoms_false=atoms_false)

        assumptions: List[Tuple[Symbol, bool]] = self._make_assumptions(spec)
        assumptions += self._make_assumptions(spec_check)
        models_ret: List[None] = []

        solve_handle: SolveHandle = self.ctl_rand.solve(assumptions=assumptions,
                                                        on_model=lambda x: models_ret.append(None), async_=True)
        solve_handle.wait(timeout=timeout)
        solve_handle.cancel()

        return len(models_ret) > 0
```
