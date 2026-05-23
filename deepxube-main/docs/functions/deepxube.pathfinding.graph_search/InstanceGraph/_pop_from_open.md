---
id: "func:deepxube.pathfinding.graph_search.InstanceGraph._pop_from_open"
kind: "method"
name: "_pop_from_open"
qualified_name: "deepxube.pathfinding.graph_search.InstanceGraph._pop_from_open"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 79
line_end: 98
class: "InstanceGraph"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "List[SchOver]"
docstring_source: "present"
callees:
  - target: null
    expr: "min"
    call_sites: [81]
  - target: null
    expr: "len"
    call_sites: [81, 86, 94]
  - target: null
    expr: "range"
    call_sites: [84]
  - target: "func:random.random"
    expr: "random.random"
    call_sites: [85]
  - target: "func:random.randrange"
    expr: "random.randrange"
    call_sites: [86]
  - target: null
    expr: "elems_popped.append"
    call_sites: [87, 90]
  - target: null
    expr: "self.open_set.pop"
    call_sites: [87]
  - target: "func:heapq.heapify"
    expr: "heapify"
    call_sites: [88]
  - target: "func:heapq.heappop"
    expr: "heappop"
    call_sites: [90]
  - target: null
    expr: "max"
    call_sites: [96]
raises: []
reads_attrs:
  - "self.batch_size"
  - "self.eps"
  - "self.lb"
  - "self.open_set"
writes_attrs:
  - "self.lb"
---

# `deepxube.pathfinding.graph_search.InstanceGraph._pop_from_open`

**File:** [deepxube/pathfinding/graph_search.py:79](../../../../deepxube/pathfinding/graph_search.py#L79)
**Class:** `InstanceGraph`
**Visibility:** private
**Kind:** method

## Signature

```python
def _pop_from_open(self) -> List[SchOver]
```

## Docstring

Pop up to ``batch_size`` items; with probability ``eps`` each pick is drawn uniformly at random. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`List[SchOver]`

## Calls

- `random.random` → `func:random.random` (lines: 85)
- `random.randrange` → `func:random.randrange` (lines: 86)
- `heapify` → `func:heapq.heapify` (lines: 88)
- `heappop` → `func:heapq.heappop` (lines: 90)

### Unresolved
- `min` (lines: 81)
- `len` (lines: 81, 86, 94)
- `range` (lines: 84)
- `elems_popped.append` (lines: 87, 90)
- `self.open_set.pop` (lines: 87)
- `max` (lines: 96)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.lb`

**Reads:**
- `self.batch_size`
- `self.eps`
- `self.lb`
- `self.open_set`

## Source

```python
    def _pop_from_open(self) -> List[SchOver]:
        """ Pop up to ``batch_size`` items; with probability ``eps`` each pick is drawn uniformly at random. """
        num_to_pop: int = min(self.batch_size, len(self.open_set))

        elems_popped: List[Tuple[float, int, SchOver]] = []
        for _ in range(num_to_pop):
            if random.random() < self.eps:
                pop_idx: int = random.randrange(0, len(self.open_set))
                elems_popped.append(self.open_set.pop(pop_idx))
                heapify(self.open_set)
            else:
                elems_popped.append(heappop(self.open_set))

        sch_over_popped: List[SchOver] = [elem_popped[2] for elem_popped in elems_popped]

        if len(elems_popped) > 0:
            cost_first: float = elems_popped[0][0]
            self.lb = max(cost_first, self.lb)

        return sch_over_popped
```
