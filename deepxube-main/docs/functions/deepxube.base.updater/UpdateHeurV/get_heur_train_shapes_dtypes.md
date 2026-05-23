---
id: "func:deepxube.base.updater.UpdateHeurV.get_heur_train_shapes_dtypes"
kind: "method"
name: "get_heur_train_shapes_dtypes"
qualified_name: "deepxube.base.updater.UpdateHeurV.get_heur_train_shapes_dtypes"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 744
line_end: 754
class: "UpdateHeurV"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "List[Tuple[Tuple[int, ...], np.dtype]]"
docstring_source: "present"
callees:
  - target: null
    expr: "self.domain.sample_problem_instances"
    call_sites: [746]
  - target: null
    expr: "self.get_heur_nnet_par().to_np"
    call_sites: [747]
  - target: "func:deepxube.base.updater.UpdateHeurV.get_heur_nnet_par"
    expr: "self.get_heur_nnet_par"
    call_sites: [747]
  - target: null
    expr: "shapes_dtypes.append"
    call_sites: [751, 752]
  - target: null
    expr: "tuple"
    call_sites: [752]
  - target: "func:numpy.dtype"
    expr: "np.dtype"
    call_sites: [752]
raises: []
reads_attrs:
  - "self.domain"
writes_attrs: []
---

# `deepxube.base.updater.UpdateHeurV.get_heur_train_shapes_dtypes`

**File:** [deepxube/base/updater.py:744](../../../../deepxube/base/updater.py#L744)
**Class:** `UpdateHeurV`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_heur_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]
```

## Docstring

:return: Input shapes/dtypes plus a scalar float64 target slot. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`List[Tuple[Tuple[int, ...], np.dtype]]`

## Calls

- `self.get_heur_nnet_par` → `func:deepxube.base.updater.UpdateHeurV.get_heur_nnet_par` (lines: 747)
- `np.dtype` → `func:numpy.dtype` (lines: 752)

### Unresolved
- `self.domain.sample_problem_instances` (lines: 746)
- `self.get_heur_nnet_par().to_np` (lines: 747)
- `shapes_dtypes.append` (lines: 751, 752)
- `tuple` (lines: 752)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`

## Source

```python
    def get_heur_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        """ :return: Input shapes/dtypes plus a scalar float64 target slot. """
        states, goals = self.domain.sample_problem_instances([0])
        inputs_nnet: List[NDArray[Any]] = self.get_heur_nnet_par().to_np(states, goals)

        shapes_dtypes: List[Tuple[Tuple[int, ...], np.dtype]] = []
        for inputs_nnet_i in inputs_nnet:
            shapes_dtypes.append((inputs_nnet_i[0].shape, inputs_nnet_i.dtype))
        shapes_dtypes.append((tuple(), np.dtype(np.float64)))

        return shapes_dtypes
```
