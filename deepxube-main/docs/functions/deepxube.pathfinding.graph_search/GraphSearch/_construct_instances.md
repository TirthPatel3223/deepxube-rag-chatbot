---
id: "func:deepxube.pathfinding.graph_search.GraphSearch._construct_instances"
kind: "method"
name: "_construct_instances"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearch._construct_instances"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 125
line_end: 141
class: "GraphSearch"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "inst_cls"
    annotation: "type[IGraph]"
    default: null
  - name: "nodes_root"
    annotation: "List[Node]"
    default: null
  - name: "inst_infos"
    annotation: "Optional[List[Any]]"
    default: null
  - name: "batch_size"
    annotation: "Optional[int]"
    default: null
  - name: "weight"
    annotation: "Optional[float]"
    default: null
  - name: "eps"
    annotation: "Optional[float]"
    default: null
returns: "List[IGraph]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.graph_search.inst_cls"
    expr: "inst_cls"
    call_sites: [135]
  - target: null
    expr: "zip"
    call_sites: [135]
  - target: null
    expr: "instance.set_batch_size"
    call_sites: [137]
  - target: null
    expr: "instance.set_weight"
    call_sites: [138]
  - target: null
    expr: "instance.set_eps"
    call_sites: [139]
raises: []
reads_attrs:
  - "self.batch_size_default"
  - "self.eps_default"
  - "self.weight_default"
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.GraphSearch._construct_instances`

**File:** [deepxube/pathfinding/graph_search.py:125](../../../../deepxube/pathfinding/graph_search.py#L125)
**Class:** `GraphSearch`
**Visibility:** private
**Kind:** method

## Signature

```python
def _construct_instances(self, inst_cls: type[IGraph], nodes_root: List[Node], inst_infos: Optional[List[Any]], batch_size: Optional[int], weight: Optional[float], eps: Optional[float]) -> List[IGraph]
```

## Docstring

Instantiate ``inst_cls`` for each root node and apply batch/weight/eps (instance overrides take precedence). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `inst_cls` | `type[IGraph]` | — |
| `nodes_root` | `List[Node]` | — |
| `inst_infos` | `Optional[List[Any]]` | — |
| `batch_size` | `Optional[int]` | — |
| `weight` | `Optional[float]` | — |
| `eps` | `Optional[float]` | — |

## Returns

`List[IGraph]`

## Calls

- `inst_cls` → `func:deepxube.pathfinding.graph_search.inst_cls` (lines: 135)

### Unresolved
- `zip` (lines: 135)
- `instance.set_batch_size` (lines: 137)
- `instance.set_weight` (lines: 138)
- `instance.set_eps` (lines: 139)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.batch_size_default`
- `self.eps_default`
- `self.weight_default`

## Source

```python
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
```
