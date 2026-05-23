---
id: "class:deepxube.base.pathfinding.PathFindSetPolicy"
kind: "class"
name: "PathFindSetPolicy"
qualified_name: "deepxube.base.pathfinding.PathFindSetPolicy"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 726
line_end: 743
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFind[D, FNsP, I]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.pathfinding.PathFindSetPolicy._set_node_vals"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.PathFindSetPolicy`

**File:** [deepxube/base/pathfinding.py:726](../../../deepxube/base/pathfinding.py#L726)
**Abstract:** yes

## Docstring

Mixin: ``_set_node_vals`` populates ``act_probs`` from the policy function. 

## Inheritance

**Direct bases:**
- `PathFind[D, FNsP, I]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_set_node_vals`

## Source

```python
class PathFindSetPolicy(PathFind[D, FNsP, I], ABC):
    """ Mixin: ``_set_node_vals`` populates ``act_probs`` from the policy function. """

    def _set_node_vals(self, nodes: List[Node]) -> None:
        """ Run the policy on (state, goal) pairs and stash the (actions, pdfs) on each node. """
        start_time = time.time()
        states: List[State] = [node.state for node in nodes]
        goals: List[Goal] = [node.goal for node in nodes]
        actions_l, probs_l = self.functions.policy_fn(self.domain, states, goals)

        assert len(actions_l) == len(probs_l) == len(states) == len(goals), \
            f"{len(actions_l)}, {len(probs_l)}, {len(states)}, {len(goals)}"

        for node, actions, probs in zip(nodes, actions_l, probs_l, strict=True):
            assert len(actions) == len(probs), f"{len(actions)}, {len(probs)}"
            node.act_probs = (actions, probs)

        self.times.record_time("policy", time.time() - start_time)
```
