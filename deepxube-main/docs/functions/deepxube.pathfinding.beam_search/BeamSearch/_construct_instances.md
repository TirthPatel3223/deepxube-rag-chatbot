---
id: "func:deepxube.pathfinding.beam_search.BeamSearch._construct_instances"
kind: "method"
name: "_construct_instances"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearch._construct_instances"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 103
line_end: 119
class: "BeamSearch"
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
    annotation: "type[IBeam]"
    default: null
  - name: "nodes_root"
    annotation: "List[Node]"
    default: null
  - name: "inst_infos"
    annotation: "Optional[List[Any]]"
    default: null
  - name: "beam_size"
    annotation: "Optional[int]"
    default: null
  - name: "temp"
    annotation: "Optional[float]"
    default: null
  - name: "eps"
    annotation: "Optional[float]"
    default: null
returns: "List[IBeam]"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.beam_search.inst_cls"
    expr: "inst_cls"
    call_sites: [113]
  - target: null
    expr: "zip"
    call_sites: [113]
  - target: null
    expr: "instance.set_beam_size"
    call_sites: [115]
  - target: null
    expr: "instance.set_temp"
    call_sites: [116]
  - target: null
    expr: "instance.set_eps"
    call_sites: [117]
raises: []
reads_attrs:
  - "self.beam_size_default"
  - "self.eps_default"
  - "self.temp_default"
writes_attrs: []
---

# `deepxube.pathfinding.beam_search.BeamSearch._construct_instances`

**File:** [deepxube/pathfinding/beam_search.py:103](../../../../deepxube/pathfinding/beam_search.py#L103)
**Class:** `BeamSearch`
**Visibility:** private
**Kind:** method

## Signature

```python
def _construct_instances(self, inst_cls: type[IBeam], nodes_root: List[Node], inst_infos: Optional[List[Any]], beam_size: Optional[int], temp: Optional[float], eps: Optional[float]) -> List[IBeam]
```

## Docstring

Instantiate ``inst_cls`` for each root node and apply beam-size / temp / eps (instance overrides take precedence). 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `inst_cls` | `type[IBeam]` | — |
| `nodes_root` | `List[Node]` | — |
| `inst_infos` | `Optional[List[Any]]` | — |
| `beam_size` | `Optional[int]` | — |
| `temp` | `Optional[float]` | — |
| `eps` | `Optional[float]` | — |

## Returns

`List[IBeam]`

## Calls

- `inst_cls` → `func:deepxube.pathfinding.beam_search.inst_cls` (lines: 113)

### Unresolved
- `zip` (lines: 113)
- `instance.set_beam_size` (lines: 115)
- `instance.set_temp` (lines: 116)
- `instance.set_eps` (lines: 117)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.beam_size_default`
- `self.eps_default`
- `self.temp_default`

## Source

```python
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
```
