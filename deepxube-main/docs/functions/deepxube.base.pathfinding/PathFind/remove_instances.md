---
id: "func:deepxube.base.pathfinding.PathFind.remove_instances"
kind: "method"
name: "remove_instances"
qualified_name: "deepxube.base.pathfinding.PathFind.remove_instances"
module: "deepxube.base.pathfinding"
file: "deepxube/base/pathfinding.py"
line_start: 329
line_end: 345
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
  - name: "test_rem"
    annotation: "Callable[[I], bool]"
    default: null
returns: "List[I]"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.pathfinding.test_rem"
    expr: "test_rem"
    call_sites: [338]
  - target: null
    expr: "instances_remove.append"
    call_sites: [339]
  - target: null
    expr: "instances_keep.append"
    call_sites: [341]
raises: []
reads_attrs:
  - "self.instances"
writes_attrs:
  - "self.instances"
---

# `deepxube.base.pathfinding.PathFind.remove_instances`

**File:** [deepxube/base/pathfinding.py:329](../../../../deepxube/base/pathfinding.py#L329)
**Class:** `PathFind`
**Visibility:** public
**Kind:** method

## Signature

```python
def remove_instances(self, test_rem: Callable[[I], bool]) -> List[I]
```

## Docstring

Remove instances

:param test_rem: A Callable that takes an instance as input and returns true if the instance should be removed
:return: List of removed instances

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `test_rem` | `Callable[[I], bool]` | — |

## Returns

`List[I]`

## Calls

- `test_rem` → `func:deepxube.base.pathfinding.test_rem` (lines: 338)

### Unresolved
- `instances_remove.append` (lines: 339)
- `instances_keep.append` (lines: 341)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.instances`

**Reads:**
- `self.instances`

## Source

```python
    def remove_instances(self, test_rem: Callable[[I], bool]) -> List[I]:
        """ Remove instances

        :param test_rem: A Callable that takes an instance as input and returns true if the instance should be removed
        :return: List of removed instances
        """
        instances_remove: List[I] = []
        instances_keep: List[I] = []
        for instance in self.instances:
            if test_rem(instance):
                instances_remove.append(instance)
            else:
                instances_keep.append(instance)

        self.instances = instances_keep

        return instances_remove
```
