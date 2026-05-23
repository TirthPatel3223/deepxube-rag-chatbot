---
id: "func:deepxube.logic.asp.Solver.sample_minimal_model"
kind: "method"
name: "sample_minimal_model"
qualified_name: "deepxube.logic.asp.Solver.sample_minimal_model"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 202
line_end: 210
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
  - name: "on_model"
    annotation: "Callable[[ModelCl], Model]"
    default: null
returns: "Model"
docstring_source: "present"
callees:
  - target: "func:deepxube.logic.asp.Spec"
    expr: "Spec"
    call_sites: [206]
  - target: "func:deepxube.logic.asp.Solver._make_assumptions"
    expr: "self._make_assumptions"
    call_sites: [207]
  - target: null
    expr: "spec.add"
    call_sites: [207]
  - target: null
    expr: "self.ctl_min.solve"
    call_sites: [208]
  - target: null
    expr: "models_min.append"
    call_sites: [208]
  - target: "func:deepxube.logic.asp.on_model"
    expr: "on_model"
    call_sites: [208]
  - target: "func:random.choice"
    expr: "random.choice"
    call_sites: [210]
raises: []
reads_attrs:
  - "self.ctl_min"
  - "self.ground_atoms"
writes_attrs: []
---

# `deepxube.logic.asp.Solver.sample_minimal_model`

**File:** [deepxube/logic/asp.py:202](../../../../deepxube/logic/asp.py#L202)
**Class:** `Solver`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_minimal_model(self, spec: Spec, model: Model, on_model: Callable[[ModelCl], Model]) -> Model
```

## Docstring

:return: A randomly chosen stable model that is minimal w.r.t. the atoms not in ``model``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `spec` | `Spec` | — |
| `model` | `Model` | — |
| `on_model` | `Callable[[ModelCl], Model]` | — |

## Returns

`Model`

## Calls

- `Spec` → `func:deepxube.logic.asp.Spec` (lines: 206)
- `self._make_assumptions` → `func:deepxube.logic.asp.Solver._make_assumptions` (lines: 207)
- `on_model` → `func:deepxube.logic.asp.on_model` (lines: 208)
- `random.choice` → `func:random.choice` (lines: 210)

### Unresolved
- `spec.add` (lines: 207)
- `self.ctl_min.solve` (lines: 208)
- `models_min.append` (lines: 208)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.ctl_min`
- `self.ground_atoms`

## Source

```python
    def sample_minimal_model(self, spec: Spec, model: Model, on_model: Callable[[ModelCl], Model]) -> Model:
        """ :return: A randomly chosen stable model that is minimal w.r.t. the atoms not in ``model``. """
        models_min: List[Model] = []
        atoms_false: List[Atom] = [atom for atom in self.ground_atoms if atom not in model]
        spec_min: Spec = Spec(atoms_false=atoms_false)
        assumptions: List[Tuple[Symbol, bool]] = self._make_assumptions(spec.add(spec_min))
        self.ctl_min.solve(assumptions=assumptions, on_model=lambda x: models_min.append(on_model(x)))

        return random.choice(models_min)
```
