---
id: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.sample"
kind: "method"
name: "sample"
qualified_name: "deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.sample"
module: "deepxube.updaters.utils.replay_buffer_utils"
file: "deepxube/updaters/utils/replay_buffer_utils.py"
line_start: 51
line_end: 61
class: "ReplayBuffer"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "num"
    annotation: "int"
    default: null
returns: "SampRet"
docstring_source: "present"
callees:
  - target: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.size"
    expr: "self.size"
    call_sites: [58]
  - target: null
    expr: "np.random.randint(0, len(self.deque), size=num).tolist"
    call_sites: [59]
  - target: null
    expr: "np.random.randint"
    call_sites: [59]
  - target: null
    expr: "len"
    call_sites: [59]
  - target: "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer._elems_to_ret"
    expr: "self._elems_to_ret"
    call_sites: [61]
raises: []
reads_attrs:
  - "self.deque"
writes_attrs: []
---

# `deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.sample`

**File:** [deepxube/updaters/utils/replay_buffer_utils.py:51](../../../../deepxube/updaters/utils/replay_buffer_utils.py#L51)
**Class:** `ReplayBuffer`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample(self, num: int) -> SampRet
```

## Docstring

Uniformly sample ``num`` elements (with replacement) and unpack
them into per-field lists via ``_elems_to_ret``.

:param num: Number of elements to sample.
:return: A tuple of per-field lists, defined by the subclass.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |

## Returns

`SampRet`

## Calls

- `self.size` → `func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.size` (lines: 58)
- `self._elems_to_ret` → `func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer._elems_to_ret` (lines: 61)

### Unresolved
- `np.random.randint(0, len(self.deque), size=num).tolist` (lines: 59)
- `np.random.randint` (lines: 59)
- `len` (lines: 59)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.deque`

## Source

```python
    def sample(self, num: int) -> SampRet:
        """ Uniformly sample ``num`` elements (with replacement) and unpack
        them into per-field lists via ``_elems_to_ret``.

        :param num: Number of elements to sample.
        :return: A tuple of per-field lists, defined by the subclass.
        """
        assert self.size() > 0, f"Replay buffer size should not be {self.size()}"
        idxs: List[int] = np.random.randint(0, len(self.deque), size=num).tolist()
        elems: List[Elem] = [self.deque[idx] for idx in idxs]
        return self._elems_to_ret(elems)
```
