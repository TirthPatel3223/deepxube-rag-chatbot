---
id: "func:deepxube.domains.sokoban.Sokoban.sample_start_states"
kind: "method"
name: "sample_start_states"
qualified_name: "deepxube.domains.sokoban.Sokoban.sample_start_states"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 237
line_end: 251
class: "Sokoban"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "num_states"
    annotation: "int"
    default: null
returns: "List[SkState]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.sokoban._get_train_states"
    expr: "_get_train_states"
    call_sites: [241]
  - target: null
    expr: "np.random.randint"
    call_sites: [242]
  - target: null
    expr: "len"
    call_sites: [242]
  - target: null
    expr: "list"
    call_sites: [248]
  - target: null
    expr: "range"
    call_sites: [248]
  - target: null
    expr: "np.random.choice(steps_range, num_states).tolist"
    call_sites: [249]
  - target: null
    expr: "np.random.choice"
    call_sites: [249]
  - target: "func:deepxube.domains.sokoban.Sokoban.random_walk"
    expr: "self.random_walk"
    call_sites: [251]
raises: []
reads_attrs:
  - "self.states_train"
writes_attrs:
  - "self.states_train"
---

# `deepxube.domains.sokoban.Sokoban.sample_start_states`

**File:** [deepxube/domains/sokoban.py:237](../../../../deepxube/domains/sokoban.py#L237)
**Class:** `Sokoban`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample_start_states(self, num_states: int) -> List[SkState]
```

## Docstring

:return: ``num_states`` training states each perturbed by a random walk of 0–100 steps. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num_states` | `int` | — |

## Returns

`List[SkState]`

## Calls

- `_get_train_states` → `func:deepxube.domains.sokoban._get_train_states` (lines: 241)
- `self.random_walk` → `func:deepxube.domains.sokoban.Sokoban.random_walk` (lines: 251)

### Unresolved
- `np.random.randint` (lines: 242)
- `len` (lines: 242)
- `list` (lines: 248)
- `range` (lines: 248)
- `np.random.choice(steps_range, num_states).tolist` (lines: 249)
- `np.random.choice` (lines: 249)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.states_train`

**Reads:**
- `self.states_train`

## Source

```python
    def sample_start_states(self, num_states: int) -> List[SkState]:
        """ :return: ``num_states`` training states each perturbed by a random walk of 0–100 steps. """
        # get states
        if self.states_train is None:
            self.states_train = _get_train_states()
        state_idxs = np.random.randint(0, len(self.states_train), size=num_states)
        states: List[SkState] = [self.states_train[idx] for idx in state_idxs]

        # random walk
        step_range: Tuple[int, int] = (0, 100)

        steps_range: List[int] = list(range(step_range[0], step_range[1] + 1))
        step_nums: List[int] = np.random.choice(steps_range, num_states).tolist()

        return self.random_walk(states, step_nums)[0]
```
