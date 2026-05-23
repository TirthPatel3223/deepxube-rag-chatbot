---
id: "class:deepxube.base.pathfinding.PathFindSetHeurV"
kind: "class"
name: "PathFindSetHeurV"
qualified_name: "deepxube.base.pathfinding.PathFindSetHeurV"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 746
line_end: 763
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFind[D, FNsHV, I]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.pathfinding.PathFindSetHeurV._set_node_vals"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.PathFindSetHeurV`

**File:** [deepxube/base/pathfinding.py:746](../../../deepxube/base/pathfinding.py#L746)
**Abstract:** yes

## Docstring

Mixin: ``_set_node_vals`` populates ``heuristic`` from the V function. 

## Inheritance

**Direct bases:**
- `PathFind[D, FNsHV, I]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `_set_node_vals`

## Source

```python
class PathFindSetHeurV(PathFind[D, FNsHV, I], ABC):
    """ Mixin: ``_set_node_vals`` populates ``heuristic`` from the V function. """

    def _set_node_vals(self, nodes: List[Node]) -> None:
        """ Evaluate V-heuristic on (state, goal) pairs and store on each node. """
        start_time = time.time()
        states: List[State] = [node.state for node in nodes]
        goals: List[Goal] = [node.goal for node in nodes]

        heuristics: List[float] = self.functions.heur_fn_v(states, goals)

        assert len(heuristics) == len(states) == len(goals), \
            f"{len(heuristics)}, {len(states)}, {len(goals)}"

        for node, heuristic in zip(nodes, heuristics, strict=True):
            node.heuristic = heuristic

        self.times.record_time("heur", time.time() - start_time)
```
