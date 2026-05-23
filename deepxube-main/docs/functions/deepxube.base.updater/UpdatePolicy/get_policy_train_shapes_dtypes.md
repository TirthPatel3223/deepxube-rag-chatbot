---
id: "func:deepxube.base.updater.UpdatePolicy.get_policy_train_shapes_dtypes"
kind: "method"
name: "get_policy_train_shapes_dtypes"
qualified_name: "deepxube.base.updater.UpdatePolicy.get_policy_train_shapes_dtypes"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 721
line_end: 731
class: "UpdatePolicy"
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
    call_sites: [723]
  - target: null
    expr: "self.domain.sample_state_action"
    call_sites: [724]
  - target: null
    expr: "self.get_policy_nnet_par().to_np_train"
    call_sites: [725]
  - target: "func:deepxube.base.updater.UpdatePolicy.get_policy_nnet_par"
    expr: "self.get_policy_nnet_par"
    call_sites: [725]
  - target: null
    expr: "shapes_dtypes.append"
    call_sites: [729]
raises: []
reads_attrs:
  - "self.domain"
writes_attrs: []
---

# `deepxube.base.updater.UpdatePolicy.get_policy_train_shapes_dtypes`

**File:** [deepxube/base/updater.py:721](../../../../deepxube/base/updater.py#L721)
**Class:** `UpdatePolicy`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_policy_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]
```

## Docstring

:return: Shape/dtype of each training-array slot for the policy. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`List[Tuple[Tuple[int, ...], np.dtype]]`

## Calls

- `self.get_policy_nnet_par` → `func:deepxube.base.updater.UpdatePolicy.get_policy_nnet_par` (lines: 725)

### Unresolved
- `self.domain.sample_problem_instances` (lines: 723)
- `self.domain.sample_state_action` (lines: 724)
- `self.get_policy_nnet_par().to_np_train` (lines: 725)
- `shapes_dtypes.append` (lines: 729)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`

## Source

```python
    def get_policy_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        """ :return: Shape/dtype of each training-array slot for the policy. """
        states, goals = self.domain.sample_problem_instances([0])
        actions: List[Action] = self.domain.sample_state_action(states)
        inputs_nnet: List[NDArray[Any]] = self.get_policy_nnet_par().to_np_train(states, goals, actions)

        shapes_dtypes: List[Tuple[Tuple[int, ...], np.dtype]] = []
        for inputs_nnet_i in inputs_nnet:
            shapes_dtypes.append((inputs_nnet_i[0].shape, inputs_nnet_i.dtype))

        return shapes_dtypes
```
