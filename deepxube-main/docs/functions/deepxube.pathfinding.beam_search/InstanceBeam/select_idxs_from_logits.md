---
id: "func:deepxube.pathfinding.beam_search.InstanceBeam.select_idxs_from_logits"
kind: "method"
name: "select_idxs_from_logits"
qualified_name: "deepxube.pathfinding.beam_search.InstanceBeam.select_idxs_from_logits"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 58
line_end: 82
class: "InstanceBeam"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "logits"
    annotation: "List[float]"
    default: null
returns: "List[int]"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [60, 62, 75, 76]
  - target: null
    expr: "list"
    call_sites: [63, 81]
  - target: null
    expr: "range"
    call_sites: [63]
  - target: null
    expr: "np.argpartition(logits, -self.beam_size)[-self.beam_size:].tolist"
    call_sites: [67]
  - target: "func:numpy.argpartition"
    expr: "np.argpartition"
    call_sites: [67]
  - target: "func:deepxube.utils.misc_utils.boltzmann"
    expr: "boltzmann"
    call_sites: [70]
  - target: null
    expr: "np.random.choice(num_logits, size=self.beam_size, replace=False, p=probs).tolist"
    call_sites: [71]
  - target: null
    expr: "np.random.choice"
    call_sites: [71, 78]
  - target: null
    expr: "np.where(np.random.random(len(next_idxs)) < self.eps)[0].tolist"
    call_sites: [75]
  - target: "func:numpy.where"
    expr: "np.where"
    call_sites: [75]
  - target: null
    expr: "np.random.random"
    call_sites: [75]
  - target: null
    expr: "np.random.choice(num_logits, replace=False, size=num_replace).tolist"
    call_sites: [78]
  - target: null
    expr: "zip"
    call_sites: [79]
  - target: null
    expr: "set"
    call_sites: [81]
raises: []
reads_attrs:
  - "self.beam_size"
  - "self.eps"
  - "self.temp"
writes_attrs: []
---

# `deepxube.pathfinding.beam_search.InstanceBeam.select_idxs_from_logits`

**File:** [deepxube/pathfinding/beam_search.py:58](../../../../deepxube/pathfinding/beam_search.py#L58)
**Class:** `InstanceBeam`
**Visibility:** public
**Kind:** method

## Signature

```python
def select_idxs_from_logits(self, logits: List[float]) -> List[int]
```

## Docstring

Pick ``beam_size`` indices greedily, by Boltzmann sampling, or with epsilon random replacement. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `logits` | `List[float]` | — |

## Returns

`List[int]`

## Calls

- `np.argpartition` → `func:numpy.argpartition` (lines: 67)
- `boltzmann` → `func:deepxube.utils.misc_utils.boltzmann` (lines: 70)
- `np.where` → `func:numpy.where` (lines: 75)

### Unresolved
- `len` (lines: 60, 62, 75, 76)
- `list` (lines: 63, 81)
- `range` (lines: 63)
- `np.argpartition(logits, -self.beam_size)[-self.beam_size:].tolist` (lines: 67)
- `np.random.choice(num_logits, size=self.beam_size, replace=False, p=probs).tolist` (lines: 71)
- `np.random.choice` (lines: 71, 78)
- `np.where(np.random.random(len(next_idxs)) < self.eps)[0].tolist` (lines: 75)
- `np.random.random` (lines: 75)
- `np.random.choice(num_logits, replace=False, size=num_replace).tolist` (lines: 78)
- `zip` (lines: 79)
- `set` (lines: 81)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.beam_size`
- `self.eps`
- `self.temp`

## Source

```python
    def select_idxs_from_logits(self, logits: List[float]) -> List[int]:
        """ Pick ``beam_size`` indices greedily, by Boltzmann sampling, or with epsilon random replacement. """
        num_logits: int = len(logits)
        next_idxs: List[int]
        if len(logits) <= self.beam_size:
            next_idxs = list(range(num_logits))
        else:
            # get next idxs
            if self.temp == 0:
                next_idxs = (np.argpartition(logits, -self.beam_size)[-self.beam_size:]).tolist()
            else:
                # select next according to boltzmann
                probs: List[float] = boltzmann(logits, self.temp)
                next_idxs = np.random.choice(num_logits, size=self.beam_size, replace=False, p=probs).tolist()

            # randomly select index
            if self.eps > 0:
                replace_rand_idxs: List[int] = np.where(np.random.random(len(next_idxs)) < self.eps)[0].tolist()
                num_replace: int = len(replace_rand_idxs)
                if num_replace > 0:
                    next_idxs_rand: List[int] = np.random.choice(num_logits, replace=False, size=num_replace).tolist()
                    for replace_idx, next_idx_rand in zip(replace_rand_idxs, next_idxs_rand):
                        next_idxs[replace_idx] = next_idx_rand
                    next_idxs = list(set(next_idxs))
        return next_idxs
```
