---
id: "func:deepxube.base.updater.UpdateHeurQ.get_heur_train_shapes_dtypes"
kind: "method"
name: "get_heur_train_shapes_dtypes"
qualified_name: "deepxube.base.updater.UpdateHeurQ.get_heur_train_shapes_dtypes"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 760
line_end: 771
class: "UpdateHeurQ"
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
    call_sites: [762]
  - target: null
    expr: "self.domain.sample_state_action"
    call_sites: [763]
  - target: null
    expr: "self.get_heur_nnet_par().to_np"
    call_sites: [764]
  - target: "func:deepxube.base.updater.UpdateHeurQ.get_heur_nnet_par"
    expr: "self.get_heur_nnet_par"
    call_sites: [764]
  - target: null
    expr: "shapes_dtypes.append"
    call_sites: [768, 769]
  - target: null
    expr: "tuple"
    call_sites: [769]
  - target: "func:numpy.dtype"
    expr: "np.dtype"
    call_sites: [769]
raises: []
reads_attrs:
  - "self.domain"
writes_attrs: []
---

# `deepxube.base.updater.UpdateHeurQ.get_heur_train_shapes_dtypes`

**File:** [deepxube/base/updater.py:760](../../../../deepxube/base/updater.py#L760)
**Class:** `UpdateHeurQ`
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

- `self.get_heur_nnet_par` → `func:deepxube.base.updater.UpdateHeurQ.get_heur_nnet_par` (lines: 764)
- `np.dtype` → `func:numpy.dtype` (lines: 769)

### Unresolved
- `self.domain.sample_problem_instances` (lines: 762)
- `self.domain.sample_state_action` (lines: 763)
- `self.get_heur_nnet_par().to_np` (lines: 764)
- `shapes_dtypes.append` (lines: 768, 769)
- `tuple` (lines: 769)

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
        actions: List[Action] = self.domain.sample_state_action(states)
        inputs_nnet: List[NDArray[Any]] = self.get_heur_nnet_par().to_np(states, goals, [[action] for action in actions])

        shapes_dtypes: List[Tuple[Tuple[int, ...], np.dtype]] = []
        for inputs_nnet_i in inputs_nnet:
            shapes_dtypes.append((inputs_nnet_i[0].shape, inputs_nnet_i.dtype))
        shapes_dtypes.append((tuple(), np.dtype(np.float64)))

        return shapes_dtypes
```
