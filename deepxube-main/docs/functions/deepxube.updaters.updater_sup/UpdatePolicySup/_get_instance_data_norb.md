---
id: "func:deepxube.updaters.updater_sup.UpdatePolicySup._get_instance_data_norb"
kind: "method"
name: "_get_instance_data_norb"
qualified_name: "deepxube.updaters.updater_sup.UpdatePolicySup._get_instance_data_norb"
module: "deepxube.updaters.updater_sup"
file: "deepxube/updaters/updater_sup.py"
line_start: 40
line_end: 58
class: "UpdatePolicySup"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "instances"
    annotation: "List[InstanceEdge]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "edges_popped.extend"
    call_sites: [51]
  - target: null
    expr: "instance.get_edges_popped"
    call_sites: [51]
  - target: null
    expr: "self.get_policy_nnet_par().to_np_train"
    call_sites: [57]
  - target: "func:deepxube.updaters.updater_sup.UpdatePolicySup.get_policy_nnet_par"
    expr: "self.get_policy_nnet_par"
    call_sites: [57]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_sup.UpdatePolicySup._get_instance_data_norb`

**File:** [deepxube/updaters/updater_sup.py:40](../../../../deepxube/updaters/updater_sup.py#L40)
**Class:** `UpdatePolicySup`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_norb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]
```

## Docstring

Convert popped edges from finished instances into training numpy
arrays (state, goal, action) for the policy network.

:param instances: Finished supervised instances.
:param times: Timer accumulator (unused here but part of the
    signature).
:return: List of numpy arrays ready for policy training.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceEdge]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `self.get_policy_nnet_par` → `func:deepxube.updaters.updater_sup.UpdatePolicySup.get_policy_nnet_par` (lines: 57)

### Unresolved
- `edges_popped.extend` (lines: 51)
- `instance.get_edges_popped` (lines: 51)
- `self.get_policy_nnet_par().to_np_train` (lines: 57)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_instance_data_norb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]:
        """ Convert popped edges from finished instances into training numpy
        arrays (state, goal, action) for the policy network.

        :param instances: Finished supervised instances.
        :param times: Timer accumulator (unused here but part of the
            signature).
        :return: List of numpy arrays ready for policy training.
        """
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())

        states: List[State] = [edge.node.state for edge in edges_popped]
        goals: List[Goal] = [edge.node.goal for edge in edges_popped]
        actions: List[Action] = [edge.action for edge in edges_popped]

        inputs_np: List[NDArray] = self.get_policy_nnet_par().to_np_train(states, goals, actions)
        return inputs_np
```
