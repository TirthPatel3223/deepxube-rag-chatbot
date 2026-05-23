---
id: "func:deepxube.domains.npuzzle.NPuzzle.random_walk"
kind: "method"
name: "random_walk"
qualified_name: "deepxube.domains.npuzzle.NPuzzle.random_walk"
module: "deepxube.domains.npuzzle"
file: "deepxube/domains/npuzzle.py"
line_start: 262
line_end: 290
class: "NPuzzle"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "states"
    annotation: "List[NPState]"
    default: null
  - name: "num_steps_l"
    annotation: "List[int]"
    default: null
returns: "Tuple[List[NPState], List[float]]"
docstring_source: "present"
callees:
  - target: "func:numpy.stack"
    expr: "np.stack"
    call_sites: [264]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [269, 277]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [272]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [273]
  - target: null
    expr: "len"
    call_sites: [273, 278]
  - target: null
    expr: "int"
    call_sites: [276, 278]
  - target: "func:numpy.max"
    expr: "np.max"
    call_sites: [276]
  - target: null
    expr: "max"
    call_sites: [278]
  - target: null
    expr: "np.random.choice"
    call_sites: [279]
  - target: "func:random.randrange"
    expr: "randrange"
    call_sites: [281]
  - target: "func:deepxube.domains.npuzzle.NPuzzle._move_np"
    expr: "self._move_np"
    call_sites: [282]
  - target: null
    expr: "enumerate"
    call_sites: [285]
  - target: "func:deepxube.domains.npuzzle.NPState"
    expr: "NPState"
    call_sites: [290]
raises: []
reads_attrs:
  - "self.num_actions"
writes_attrs: []
---

# `deepxube.domains.npuzzle.NPuzzle.random_walk`

**File:** [deepxube/domains/npuzzle.py:262](../../../../deepxube/domains/npuzzle.py#L262)
**Class:** `NPuzzle`
**Visibility:** public
**Kind:** method

## Signature

```python
def random_walk(self, states: List[NPState], num_steps_l: List[int]) -> Tuple[List[NPState], List[float]]
```

## Docstring

:return: States after each state in ``states`` takes ``num_steps_l[i]`` random slides, plus total costs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `states` | `List[NPState]` | — |
| `num_steps_l` | `List[int]` | — |

## Returns

`Tuple[List[NPState], List[float]]`

## Calls

- `np.stack` → `func:numpy.stack` (lines: 264)
- `np.where` → `func:numpy.where` (lines: 269, 277)
- `np.array` → `func:numpy.array` (lines: 272)
- `np.zeros` → `func:numpy.zeros` (lines: 273)
- `np.max` → `func:numpy.max` (lines: 276)
- `randrange` → `func:random.randrange` (lines: 281)
- `self._move_np` → `func:deepxube.domains.npuzzle.NPuzzle._move_np` (lines: 282)
- `NPState` → `func:deepxube.domains.npuzzle.NPState` (lines: 290)

### Unresolved
- `len` (lines: 273, 278)
- `int` (lines: 276, 278)
- `max` (lines: 278)
- `np.random.choice` (lines: 279)
- `enumerate` (lines: 285)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.num_actions`

## Source

```python
    def random_walk(self, states: List[NPState], num_steps_l: List[int]) -> Tuple[List[NPState], List[float]]:
        """ :return: States after each state in ``states`` takes ``num_steps_l[i]`` random slides, plus total costs. """
        states_np = np.stack([x.tiles for x in states], axis=0)
        path_costs: List[float] = [0.0 for _ in states]

        # Get z_idxs
        z_idxs: NDArray[np.int_]
        _, z_idxs = np.where(states_np == 0)

        # Scrambles
        num_steps_np: NDArray[np.int_] = np.array(num_steps_l)
        num_actions: NDArray[np.int_] = np.zeros(len(states), dtype=int)

        # go backward from goal state
        while int(np.max(num_actions < num_steps_np)) > 0:
            idxs: NDArray[np.int_] = np.where((num_actions < num_steps_np))[0]
            subset_size: int = int(max(len(idxs) / self.num_actions, 1))
            idxs = np.random.choice(idxs, subset_size)

            move: int = randrange(self.num_actions)
            states_np[idxs], z_idxs[idxs], tcs = self._move_np(states_np[idxs], z_idxs[idxs], move)

            idx: int
            for move_idx, idx in enumerate(idxs):
                path_costs[idx] += tcs[move_idx]

            num_actions[idxs] = num_actions[idxs] + 1

        return [NPState(x) for x in states_np], path_costs
```
