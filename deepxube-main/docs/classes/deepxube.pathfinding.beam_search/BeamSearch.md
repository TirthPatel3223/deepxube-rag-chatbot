---
id: "class:deepxube.pathfinding.beam_search.BeamSearch"
kind: "class"
name: "BeamSearch"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearch"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 93
line_end: 122
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PathFind[D, FNs, IBeam]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.BeamSearch.__init__"
  - "func:deepxube.pathfinding.beam_search.BeamSearch._construct_instances"
  - "func:deepxube.pathfinding.beam_search.BeamSearch.__repr__"
attributes:
  - name: "self.beam_size_default"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.eps_default"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.temp_default"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearch`

**File:** [deepxube/pathfinding/beam_search.py:93](../../../deepxube/pathfinding/beam_search.py#L93)
**Abstract:** yes

## Docstring

Abstract beam-search base. Carries default beam size, temperature, and epsilon used when constructing instances. 

## Inheritance

**Direct bases:**
- `PathFind[D, FNs, IBeam]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `_construct_instances`
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.beam_size_default` | — | __init__ |
| `self.eps_default` | — | __init__ |
| `self.temp_default` | — | __init__ |

## Source

```python
class BeamSearch(PathFind[D, FNs, IBeam], ABC):
    """ Abstract beam-search base. Carries default beam size, temperature, and epsilon used when constructing instances. """

    def __init__(self, domain: D, functions: FNs, beam_size: int = 1, temp: float = 0.0, eps: float = 0.0):
        """ Store default beam-search parameters; per-instance overrides may be supplied to ``make_instances``. """
        super().__init__(domain, functions)
        self.beam_size_default: int = beam_size
        self.temp_default: float = temp
        self.eps_default: float = eps

    def _construct_instances(self, inst_cls: type[IBeam], nodes_root: List[Node], inst_infos: Optional[List[Any]], beam_size: Optional[int],
                             temp: Optional[float], eps: Optional[float]) -> List[IBeam]:
        """ Instantiate ``inst_cls`` for each root node and apply beam-size / temp / eps (instance overrides take precedence). """
        if inst_infos is None:
            inst_infos = [None for _ in nodes_root]

        beam_size_inst: int = beam_size if beam_size is not None else self.beam_size_default
        temp_inst: float = temp if temp is not None else self.temp_default
        eps_inst: float = eps if eps is not None else self.eps_default

        instances: List[IBeam] = [inst_cls(node_root, inst_info) for node_root, inst_info in zip(nodes_root, inst_infos, strict=True)]
        for instance in instances:
            instance.set_beam_size(beam_size_inst)
            instance.set_temp(temp_inst)
            instance.set_eps(eps_inst)

        return instances

    def __repr__(self) -> str:
        return f"{type(self).__name__}(beam_size={self.beam_size_default}, temp={self.temp_default}, eps={self.eps_default})"
```
