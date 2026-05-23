---
id: "class:deepxube.pathfinding.graph_search.GraphSearch"
kind: "class"
name: "GraphSearch"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearch"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 115
line_end: 144
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFind[D, FNs, IGraph]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearch.__init__"
  - "func:deepxube.pathfinding.graph_search.GraphSearch._construct_instances"
  - "func:deepxube.pathfinding.graph_search.GraphSearch.__repr__"
attributes:
  - name: "self.batch_size_default"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.eps_default"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.weight_default"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearch`

**File:** [deepxube/pathfinding/graph_search.py:115](../../../deepxube/pathfinding/graph_search.py#L115)
**Abstract:** yes

## Docstring

Abstract best-first graph-search base; stores default batch_size, weight, and eps. 

## Inheritance

**Direct bases:**
- `PathFind[D, FNs, IGraph]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `_construct_instances`
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.batch_size_default` | — | __init__ |
| `self.eps_default` | — | __init__ |
| `self.weight_default` | — | __init__ |

## Source

```python
class GraphSearch(PathFind[D, FNs, IGraph], ABC):
    """ Abstract best-first graph-search base; stores default batch_size, weight, and eps. """

    def __init__(self, domain: D, functions: FNs, batch_size: int = 1, weight: float = 1.0, eps: float = 0.0):
        """ Store default batch/weight/eps parameters used when constructing instances. """
        super().__init__(domain, functions)
        self.batch_size_default: int = batch_size
        self.weight_default: float = weight
        self.eps_default: float = eps

    def _construct_instances(self, inst_cls: type[IGraph], nodes_root: List[Node], inst_infos: Optional[List[Any]], batch_size: Optional[int],
                             weight: Optional[float], eps: Optional[float]) -> List[IGraph]:
        """ Instantiate ``inst_cls`` for each root node and apply batch/weight/eps (instance overrides take precedence). """
        if inst_infos is None:
            inst_infos = [None for _ in nodes_root]

        batch_size_inst: int = batch_size if batch_size is not None else self.batch_size_default
        weight_inst: float = weight if weight is not None else self.weight_default
        eps_inst: float = eps if eps is not None else self.eps_default

        instances: List[IGraph] = [inst_cls(node_root, inst_info) for node_root, inst_info in zip(nodes_root, inst_infos, strict=True)]
        for instance in instances:
            instance.set_batch_size(batch_size_inst)
            instance.set_weight(weight_inst)
            instance.set_eps(eps_inst)

        return instances

    def __repr__(self) -> str:
        return f"{type(self).__name__}(batch_size={self.batch_size_default}, weight={self.weight_default}, eps={self.eps_default})"
```
