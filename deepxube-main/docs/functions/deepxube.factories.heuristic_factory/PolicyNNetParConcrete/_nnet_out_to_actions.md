---
id: "func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete._nnet_out_to_actions"
kind: "method"
name: "_nnet_out_to_actions"
qualified_name: "deepxube.factories.heuristic_factory.PolicyNNetParConcrete._nnet_out_to_actions"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 357
line_end: 363
class: "PolicyNNetParConcrete"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "nnet_out"
    annotation: "List[NDArray[np.float64]]"
    default: null
returns: "List[Action]"
docstring_source: "present"
callees:
  - target: null
    expr: "self._get_nnet_input().nnet_out_to_actions"
    call_sites: [363]
  - target: "func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete._get_nnet_input"
    expr: "self._get_nnet_input"
    call_sites: [363]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.heuristic_factory.PolicyNNetParConcrete._nnet_out_to_actions`

**File:** [deepxube/factories/heuristic_factory.py:357](../../../../deepxube/factories/heuristic_factory.py#L357)
**Class:** `PolicyNNetParConcrete`
**Visibility:** private
**Kind:** method

## Signature

```python
def _nnet_out_to_actions(self, nnet_out: List[NDArray[np.float64]]) -> List[Action]
```

## Docstring

Decode raw network outputs into one ``Action`` per input state.

:param nnet_out: Per-state output arrays from the policy network.
:return: One sampled/argmaxed ``Action`` per state.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet_out` | `List[NDArray[np.float64]]` | — |

## Returns

`List[Action]`

## Calls

- `self._get_nnet_input` → `func:deepxube.factories.heuristic_factory.PolicyNNetParConcrete._get_nnet_input` (lines: 363)

### Unresolved
- `self._get_nnet_input().nnet_out_to_actions` (lines: 363)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _nnet_out_to_actions(self, nnet_out: List[NDArray[np.float64]]) -> List[Action]:
        """ Decode raw network outputs into one ``Action`` per input state.

        :param nnet_out: Per-state output arrays from the policy network.
        :return: One sampled/argmaxed ``Action`` per state.
        """
        return self._get_nnet_input().nnet_out_to_actions(nnet_out)
```
