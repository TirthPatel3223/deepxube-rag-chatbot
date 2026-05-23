---
id: "class:deepxube.base.pathfinding.PathFindSup"
kind: "class"
name: "PathFindSup"
qualified_name: "deepxube.base.pathfinding.PathFindSup"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 841
line_end: 872
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFind[D, Any, I]"
    resolved_id: null
methods:
  - "func:deepxube.base.pathfinding.PathFindSup.functions_type"
  - "func:deepxube.base.pathfinding.PathFindSup.make_instances"
  - "func:deepxube.base.pathfinding.PathFindSup.expand_states"
  - "func:deepxube.base.pathfinding.PathFindSup.get_state_actions"
  - "func:deepxube.base.pathfinding.PathFindSup.make_instances_rw"
  - "func:deepxube.base.pathfinding.PathFindSup._set_node_vals"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.pathfinding.PathFindSup`

**File:** [deepxube/base/pathfinding.py:841](../../../deepxube/base/pathfinding.py#L841)
**Abstract:** yes

## Docstring

Use the path cost of a random walk as the learning target.
See Chervov, Alexander, et al. "A Machine Learning Approach That Beats Large Rubik's Cubes." NeurIPS(2025).

## Inheritance

**Direct bases:**
- `PathFind[D, Any, I]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `functions_type` *(trivial, skipped)*
- `make_instances` *(trivial, skipped)*
- `expand_states` *(trivial, skipped)*
- `get_state_actions` *(trivial, skipped)*
- `make_instances_rw` *(trivial, skipped)*
- `_set_node_vals` *(trivial, skipped)*

## Source

```python
class PathFindSup(PathFind[D, Any, I]):
    """ Use the path cost of a random walk as the learning target.
    See Chervov, Alexander, et al. "A Machine Learning Approach That Beats Large Rubik's Cubes." NeurIPS(2025).

    """
    @staticmethod
    def functions_type() -> Type[Any]:
        """ :return: ``Any`` — supervised pathfinders carry no function bundle. """
        return Any

    def make_instances(self, states: List[State], goals: List[Goal], inst_infos: Optional[List[Any]] = None, compute_root_vals: bool = True) -> List[I]:
        """ Not used by supervised pathfinders; build via ``make_instances_rw`` instead. """
        raise NotImplementedError

    def expand_states(self, states: List[State], goals: List[Goal]) -> Tuple[List[List[State]], List[List[Action]], List[List[float]]]:
        """ Not applicable: supervised pathfinders do not expand. """
        raise NotImplementedError

    def get_state_actions(self, states: List[State], goals: List[Goal]) -> List[List[Action]]:
        """ Not applicable: supervised pathfinders do not consult action sets. """
        raise NotImplementedError

    @abstractmethod
    def make_instances_rw(self, steps_gen: List[int], inst_infos: Optional[List[Any]]) -> List[I]:
        """ Make instances from a random walk

        """
        pass

    def _set_node_vals(self, nodes: List[Node]) -> None:
        """ Not applicable: supervised pathfinders do not score nodes. """
        raise NotImplementedError
```
