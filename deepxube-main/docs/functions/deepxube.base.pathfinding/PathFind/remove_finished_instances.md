---
id: "func:deepxube.base.pathfinding.PathFind.remove_finished_instances"
kind: "method"
name: "remove_finished_instances"
qualified_name: "deepxube.base.pathfinding.PathFind.remove_finished_instances"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 318
line_end: 327
class: "PathFind"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "itr_max"
    annotation: "int"
    default: null
returns: "List[I]"
docstring_source: "present"
callees:
  - target: null
    expr: "inst_in.finished"
    call_sites: [321]
  - target: "func:deepxube.base.pathfinding.PathFind.remove_instances"
    expr: "self.remove_instances"
    call_sites: [327]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.base.pathfinding.PathFind.remove_finished_instances`

**File:** [deepxube/base/pathfinding.py:318](../../../../deepxube/base/pathfinding.py#L318)
**Class:** `PathFind`
**Visibility:** public
**Kind:** method

## Signature

```python
def remove_finished_instances(self, itr_max: int) -> List[I]
```

## Docstring

Remove instances that are finished or have run for ``itr_max`` iterations; return the removed list. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `itr_max` | `int` | — |

## Returns

`List[I]`

## Calls

- `self.remove_instances` → `func:deepxube.base.pathfinding.PathFind.remove_instances` (lines: 327)

### Unresolved
- `inst_in.finished` (lines: 321)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def remove_finished_instances(self, itr_max: int) -> List[I]:
        """ Remove instances that are finished or have run for ``itr_max`` iterations; return the removed list. """
        def remove_instance_fn(inst_in: I) -> bool:
            if inst_in.finished():
                return True
            if inst_in.itr >= itr_max:
                return True
            return False

        return self.remove_instances(remove_instance_fn)
```
