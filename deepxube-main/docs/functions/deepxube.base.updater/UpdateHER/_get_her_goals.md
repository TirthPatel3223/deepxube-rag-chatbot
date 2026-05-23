---
id: "func:deepxube.base.updater.UpdateHER._get_her_goals"
kind: "method"
name: "_get_her_goals"
qualified_name: "deepxube.base.updater.UpdateHER._get_her_goals"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 533
line_end: 582
class: "UpdateHER"
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
    annotation: "List[Inst]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "Tuple[List[Inst], List[Goal]]"
docstring_source: "present"
callees:
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [541]
  - target: null
    expr: "np.random.uniform(0, 1, size=len(instances)).tolist"
    call_sites: [541]
  - target: null
    expr: "np.random.uniform"
    call_sites: [541]
  - target: null
    expr: "len"
    call_sites: [541, 553, 563, 569]
  - target: null
    expr: "zip"
    call_sites: [542]
  - target: null
    expr: "instance.finished"
    call_sites: [543]
  - target: null
    expr: "instance.has_soln"
    call_sites: [543]
  - target: null
    expr: "instances_goalkeep.append"
    call_sites: [544]
  - target: null
    expr: "instances_relabel.append"
    call_sites: [546]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [555, 575, 578, 580]
  - target: null
    expr: "states_start.append"
    call_sites: [559]
  - target: null
    expr: "instance.root_node.get_all_descendants"
    call_sites: [562]
  - target: "func:deepxube.base.pathfinding.get_path"
    expr: "get_path"
    call_sites: [569]
  - target: null
    expr: "states_deepest.append"
    call_sites: [573]
  - target: null
    expr: "times.record_time"
    call_sites: [575, 580]
  - target: null
    expr: "self.domain.sample_goal_from_state"
    call_sites: [579]
raises: []
reads_attrs:
  - "self.domain"
writes_attrs: []
---

# `deepxube.base.updater.UpdateHER._get_her_goals`

**File:** [deepxube/base/updater.py:533](../../../../deepxube/base/updater.py#L533)
**Class:** `UpdateHER`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_her_goals(self, instances: List[Inst], times: Times) -> Tuple[List[Inst], List[Goal]]
```

## Docstring

If instance is not finisheed and solved, get deepest states out all nodes that have children + root node for relabeled goal.
:return: Instances and their corresponding goals (order of instances changes)

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `instances` | `List[Inst]` | — |
| `times` | `Times` | — |

## Returns

`Tuple[List[Inst], List[Goal]]`

## Calls

- `cast` → `func:typing.cast` (lines: 541)
- `time.time` → `func:time.time` (lines: 555, 575, 578, 580)
- `get_path` → `func:deepxube.base.pathfinding.get_path` (lines: 569)

### Unresolved
- `np.random.uniform(0, 1, size=len(instances)).tolist` (lines: 541)
- `np.random.uniform` (lines: 541)
- `len` (lines: 541, 553, 563, 569)
- `zip` (lines: 542)
- `instance.finished` (lines: 543)
- `instance.has_soln` (lines: 543)
- `instances_goalkeep.append` (lines: 544)
- `instances_relabel.append` (lines: 546)
- `states_start.append` (lines: 559)
- `instance.root_node.get_all_descendants` (lines: 562)
- `states_deepest.append` (lines: 573)
- `times.record_time` (lines: 575, 580)
- `self.domain.sample_goal_from_state` (lines: 579)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.domain`

## Source

```python
    def _get_her_goals(self, instances: List[Inst], times: Times) -> Tuple[List[Inst], List[Goal]]:
        """ If instance is not finisheed and solved, get deepest states out all nodes that have children + root node for relabeled goal.
            :return: Instances and their corresponding goals (order of instances changes)
        """
        # get states/goals or mark for goal relabelling
        instances_goalkeep: List[Inst] = []
        instances_relabel: List[Inst] = []

        rand_keeps: List[float] = cast(List[float], np.random.uniform(0, 1, size=len(instances)).tolist())
        for instance, rand_keep in zip(instances, rand_keeps):
            if instance.finished() and instance.has_soln():
                instances_goalkeep.append(instance)
            else:
                instances_relabel.append(instance)

        # get goals goalkeep
        goals_goalkeep: List[Goal] = [instance.root_node.goal for instance in instances_goalkeep]

        # get relabeled goals
        goals_relabel: List[Goal] = []
        if len(instances_relabel) > 0:
            # get start states and deepest states
            start_time = time.time()
            states_start: List[State] = []
            states_deepest: List[State] = []
            for instance in instances_relabel:
                states_start.append(instance.root_node.state)

                # get all descendants that have children
                nodes_desc: List[Node] = instance.root_node.get_all_descendants()
                node_desc_w_children: List[Node] = [node_desc for node_desc in nodes_desc if len(node_desc.edge_dict) > 0]

                # get state of deepest node
                state_deepest: State = instance.root_node.state
                deepest_depth: int = 0
                for node in node_desc_w_children:
                    depth: int = len(get_path(node)[0])
                    if depth > deepest_depth:
                        deepest_depth = depth
                        state_deepest = node.state
                states_deepest.append(state_deepest)

            times.record_time("her_node_deepest", time.time() - start_time)

            # relabel
            start_time = time.time()
            goals_relabel = self.domain.sample_goal_from_state(states_start, states_deepest)
            times.record_time("her_relabel", time.time() - start_time)

        return instances_goalkeep + instances_relabel, goals_goalkeep + goals_relabel
```
