---
id: "func:deepxube.domains.sokoban.load_states"
kind: "function"
name: "load_states"
qualified_name: "deepxube.domains.sokoban.load_states"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 77
line_end: 95
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "data_dir"
    annotation: "str"
    default: null
returns: "List[SkState]"
docstring_source: "present"
callees:
  - target: "func:pickle.load"
    expr: "pickle.load"
    call_sites: [79]
  - target: null
    expr: "open"
    call_sites: [79]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [85]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [86, 87, 91]
  - target: null
    expr: "range"
    call_sites: [90]
  - target: null
    expr: "states.append"
    call_sites: [93]
  - target: "func:deepxube.domains.sokoban.SkState"
    expr: "SkState"
    call_sites: [93]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.domains.sokoban.load_states`

**File:** [deepxube/domains/sokoban.py:77](../../../../deepxube/domains/sokoban.py#L77)
**Visibility:** public
**Kind:** function

## Signature

```python
def load_states(data_dir: str) -> List[SkState]
```

## Docstring

:return: List of ``SkState`` objects decoded from ``train.pkl`` in ``data_dir/sokoban/``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `data_dir` | `str` | — |

## Returns

`List[SkState]`

## Calls

- `pickle.load` → `func:pickle.load` (lines: 79)
- `np.where` → `func:numpy.where` (lines: 85)
- `np.array` → `func:numpy.array` (lines: 86, 87, 91)
- `SkState` → `func:deepxube.domains.sokoban.SkState` (lines: 93)

### Unresolved
- `open` (lines: 79)
- `range` (lines: 90)
- `states.append` (lines: 93)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def load_states(data_dir: str) -> List[SkState]:
    """ :return: List of ``SkState`` objects decoded from ``train.pkl`` in ``data_dir/sokoban/``. """
    states_np = pickle.load(open(f"{data_dir}/sokoban/train.pkl", "rb"))
    # t_file = tarfile.open(file_name, "r:gz")
    # states_np = pickle.load(t_file.extractfile(t_file.getmembers()[1]))

    states: List[SkState] = []

    agent_idxs: Tuple[NDArray, ...] = np.where(states_np == 1)
    box_masks: NDArray = np.array(states_np == 2)
    wall_masks: NDArray = np.array(states_np == 4)

    idx: int
    for idx in range(states_np.shape[0]):
        agent_idx = np.array([agent_idxs[1][idx], agent_idxs[2][idx]], dtype=int)

        states.append(SkState(agent_idx, box_masks[idx], wall_masks[idx]))

    return states
```
