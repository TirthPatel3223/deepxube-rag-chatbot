---
id: "func:deepxube.updaters.updater_sup.UpdateHeurVSup._get_instance_data_norb"
kind: "method"
name: "_get_instance_data_norb"
qualified_name: "deepxube.updaters.updater_sup.UpdateHeurVSup._get_instance_data_norb"
module: "deepxube.updaters.updater_sup"
file: "deepxube/updaters/updater_sup.py"
line_start: 77
line_end: 94
class: "UpdateHeurVSup"
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
    annotation: "List[InstanceNode]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "nodes_popped.extend"
    call_sites: [87]
  - target: null
    expr: "instance.get_nodes_popped"
    call_sites: [87]
  - target: null
    expr: "self.get_heur_nnet_par().to_np"
    call_sites: [93]
  - target: "func:deepxube.updaters.updater_sup.UpdateHeurVSup.get_heur_nnet_par"
    expr: "self.get_heur_nnet_par"
    call_sites: [93]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [94]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_sup.UpdateHeurVSup._get_instance_data_norb`

**File:** [deepxube/updaters/updater_sup.py:77](../../../../deepxube/updaters/updater_sup.py#L77)
**Class:** `UpdateHeurVSup`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_instance_data_norb(self, instances: List[InstanceNode], times: Times) -> List[NDArray]
```

## Docstring

Convert popped nodes from finished instances into training numpy
arrays (state, goal, ctg) for the V-heuristic network.

:param instances: Finished supervised instances.
:param times: Timer accumulator (unused here).
:return: List of numpy arrays, last element is the cost-to-go target.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[InstanceNode]` | — |
| `times` | `Times` | — |

## Returns

`List[NDArray]`

## Calls

- `self.get_heur_nnet_par` → `func:deepxube.updaters.updater_sup.UpdateHeurVSup.get_heur_nnet_par` (lines: 93)
- `np.array` → `func:numpy.array` (lines: 94)

### Unresolved
- `nodes_popped.extend` (lines: 87)
- `instance.get_nodes_popped` (lines: 87)
- `self.get_heur_nnet_par().to_np` (lines: 93)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_instance_data_norb(self, instances: List[InstanceNode], times: Times) -> List[NDArray]:
        """ Convert popped nodes from finished instances into training numpy
        arrays (state, goal, ctg) for the V-heuristic network.

        :param instances: Finished supervised instances.
        :param times: Timer accumulator (unused here).
        :return: List of numpy arrays, last element is the cost-to-go target.
        """
        nodes_popped: List[Node] = []
        for instance in instances:
            nodes_popped.extend(instance.get_nodes_popped())

        states: List[State] = [node.state for node in nodes_popped]
        goals: List[Goal] = [node.goal for node in nodes_popped]

        ctgs_backup: List[float] = [node.heuristic for node in nodes_popped]
        inputs_np: List[NDArray] = self.get_heur_nnet_par().to_np(states, goals)
        return inputs_np + [np.array(ctgs_backup)]
```
