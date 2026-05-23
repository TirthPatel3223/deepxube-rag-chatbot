---
id: "func:deepxube.updaters.updater_sup.UpdateHeurQSup._get_instance_data_norb"
kind: "method"
name: "_get_instance_data_norb"
qualified_name: "deepxube.updaters.updater_sup.UpdateHeurQSup._get_instance_data_norb"
module: "deepxube.updaters.updater_sup"
file: "deepxube/updaters/updater_sup.py"
line_start: 113
line_end: 131
class: "UpdateHeurQSup"
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
    call_sites: [123]
  - target: null
    expr: "instance.get_edges_popped"
    call_sites: [123]
  - target: null
    expr: "self.get_heur_nnet_par().to_np"
    call_sites: [130]
  - target: "func:deepxube.updaters.updater_sup.UpdateHeurQSup.get_heur_nnet_par"
    expr: "self.get_heur_nnet_par"
    call_sites: [130]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [131]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_sup.UpdateHeurQSup._get_instance_data_norb`

**File:** [deepxube/updaters/updater_sup.py:113](../../../../deepxube/updaters/updater_sup.py#L113)
**Class:** `UpdateHeurQSup`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_norb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]
```

## Docstring

Convert popped edges from finished instances into training numpy
arrays (state, goal, action, q_val) for the Q-heuristic network.

:param instances: Finished supervised instances.
:param times: Timer accumulator (unused here).
:return: List of numpy arrays, last element is the Q-value target.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceEdge]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `self.get_heur_nnet_par` → `func:deepxube.updaters.updater_sup.UpdateHeurQSup.get_heur_nnet_par` (lines: 130)
- `np.array` → `func:numpy.array` (lines: 131)

### Unresolved
- `edges_popped.extend` (lines: 123)
- `instance.get_edges_popped` (lines: 123)
- `self.get_heur_nnet_par().to_np` (lines: 130)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_instance_data_norb(self, instances: List[InstanceEdge], times: Times) -> List[NDArray]:
        """ Convert popped edges from finished instances into training numpy
        arrays (state, goal, action, q_val) for the Q-heuristic network.

        :param instances: Finished supervised instances.
        :param times: Timer accumulator (unused here).
        :return: List of numpy arrays, last element is the Q-value target.
        """
        edges_popped: List[EdgeQ] = []
        for instance in instances:
            edges_popped.extend(instance.get_edges_popped())

        states: List[State] = [edge.node.state for edge in edges_popped]
        goals: List[Goal] = [edge.node.goal for edge in edges_popped]
        actions: List[Action] = [edge.action for edge in edges_popped]

        ctgs_backup: List[float] = [edge.q_val for edge in edges_popped]
        inputs_np: List[NDArray] = self.get_heur_nnet_par().to_np(states, goals, [[action] for action in actions])
        return inputs_np + [np.array(ctgs_backup)]
```
