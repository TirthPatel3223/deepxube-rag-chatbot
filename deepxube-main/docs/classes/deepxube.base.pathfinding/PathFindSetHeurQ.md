---
id: "class:deepxube.base.pathfinding.PathFindSetHeurQ"
kind: "class"
name: "PathFindSetHeurQ"
qualified_name: "deepxube.base.pathfinding.PathFindSetHeurQ"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 766
line_end: 789
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFind[D, FNsHQ, I]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.pathfinding.PathFindSetHeurQ._set_node_vals"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.PathFindSetHeurQ`

**File:** [deepxube/base/pathfinding.py:766](../../../deepxube/base/pathfinding.py#L766)
**Abstract:** yes

## Docstring

Mixin: ``_set_node_vals`` evaluates the Q function and stores ``q_values`` plus ``heuristic = min_a q``. 

## Inheritance

**Direct bases:**
- `PathFind[D, FNsHQ, I]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_set_node_vals`

## Source

```python
class PathFindSetHeurQ(PathFind[D, FNsHQ, I], ABC):
    """ Mixin: ``_set_node_vals`` evaluates the Q function and stores ``q_values`` plus ``heuristic = min_a q``. """

    def _set_node_vals(self, nodes: List[Node]) -> None:
        """ Evaluate Q on each node's (state, goal, applicable actions) and store min-Q as heuristic. """
        start_time = time.time()
        states: List[State] = [node.state for node in nodes]
        goals: List[Goal] = [node.goal for node in nodes]
        actions_l: List[List[Action]] = self.get_state_actions(states, goals)

        self.times.record_time("actions", time.time() - start_time)

        start_time = time.time()
        qvals_l: List[List[float]] = self.functions.heur_fn_q(states, goals, actions_l)
        heuristics: List[float] = [min(x) for x in qvals_l]

        assert len(heuristics) == len(actions_l) == len(qvals_l) == len(states) == len(goals), \
            f"{len(heuristics)}, {len(actions_l)}, {len(qvals_l)}, {len(states)}, {len(goals)}"

        for node, heuristic, actions, qvals in zip(nodes, heuristics, actions_l, qvals_l, strict=True):
            node.heuristic = heuristic
            node.q_values = (actions, qvals)

        self.times.record_time("heur", time.time() - start_time)
```
