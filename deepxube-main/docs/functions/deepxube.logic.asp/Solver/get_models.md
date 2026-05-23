---
id: "func:deepxube.logic.asp.Solver.get_models"
kind: "method"
name: "get_models"
qualified_name: "deepxube.logic.asp.Solver.get_models"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 148
line_end: 178
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
  - name: "on_model"
    annotation: "Callable[[Any], Model]"
    default: null
  - name: "num_models"
    annotation: "int"
    default: null
  - name: "minimal"
    annotation: "bool"
    default: null
returns: "List[Model]"
docstring_source: "present"
callees:
  - target: "func:deepxube.logic.asp.Solver._make_assumptions"
    expr: "self._make_assumptions"
    call_sites: [157, 175]
  - target: null
    expr: "range"
    call_sites: [161]
  - target: null
    expr: "self.ctl_rand.solve"
    call_sites: [163]
  - target: null
    expr: "models_i.append"
    call_sites: [163]
  - target: "func:deepxube.logic.asp.on_model"
    expr: "on_model"
    call_sites: [163]
  - target: null
    expr: "len"
    call_sites: [164]
  - target: "func:random.choice"
    expr: "random.choice"
    call_sites: [166]
  - target: "func:deepxube.logic.asp.Solver.sample_minimal_model"
    expr: "self.sample_minimal_model"
    call_sites: [169]
  - target: null
    expr: "models.append"
    call_sites: [172]
  - target: "func:deepxube.logic.asp.Spec"
    expr: "Spec"
    call_sites: [175]
  - target: null
    expr: "assumptions.extend"
    call_sites: [176]
raises: []
reads_attrs:
  - "self.ctl_rand"
writes_attrs: []
---

# `deepxube.logic.asp.Solver.get_models`

**File:** [deepxube/logic/asp.py:148](../../../../deepxube/logic/asp.py#L148)
**Class:** `Solver`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_models(self, spec: Spec, on_model: Callable[[Any], Model], num_models: int, minimal: bool) -> List[Model]
```

## Docstring

:param spec: Specification
:param on_model: Callable that processes models
:param num_models: number of models to sample
:param minimal: if true, only samples minimal models
:return:

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `spec` | `Spec` | — |
| `on_model` | `Callable[[Any], Model]` | — |
| `num_models` | `int` | — |
| `minimal` | `bool` | — |

## Returns

`List[Model]`

## Calls

- `self._make_assumptions` → `func:deepxube.logic.asp.Solver._make_assumptions` (lines: 157, 175)
- `on_model` → `func:deepxube.logic.asp.on_model` (lines: 163)
- `random.choice` → `func:random.choice` (lines: 166)
- `self.sample_minimal_model` → `func:deepxube.logic.asp.Solver.sample_minimal_model` (lines: 169)
- `Spec` → `func:deepxube.logic.asp.Spec` (lines: 175)

### Unresolved
- `range` (lines: 161)
- `self.ctl_rand.solve` (lines: 163)
- `models_i.append` (lines: 163)
- `len` (lines: 164)
- `models.append` (lines: 172)
- `assumptions.extend` (lines: 176)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.ctl_rand`

## Source

```python
    def get_models(self, spec: Spec, on_model: Callable[[Any], Model], num_models: int, minimal: bool) -> List[Model]:
        """

        :param spec: Specification
        :param on_model: Callable that processes models
        :param num_models: number of models to sample
        :param minimal: if true, only samples minimal models
        :return:
        """
        assumptions: List[Tuple[Symbol, bool]] = self._make_assumptions(spec)

        # get models
        models: List[Model] = []
        for model_itr in range(num_models):
            models_i: List[Model] = []
            self.ctl_rand.solve(assumptions=assumptions, on_model=lambda x: models_i.append(on_model(x)))
            if len(models_i) == 0:
                break
            model_i: Model = random.choice(models_i)

            if minimal:
                model_i = self.sample_minimal_model(spec, model_i, on_model)
                # assert model_i == self.sample_minimal_model_old(spec, model_i)

            models.append(model_i)

            if model_itr < (num_models - 1):
                assumptions_i: List[Tuple[Symbol, bool]] = self._make_assumptions(Spec(models_banned=[model_i]))
                assumptions.extend(assumptions_i)

        return models
```
