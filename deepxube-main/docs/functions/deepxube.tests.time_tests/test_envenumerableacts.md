---
id: "func:deepxube.tests.time_tests.test_envenumerableacts"
kind: "function"
name: "test_envenumerableacts"
qualified_name: "deepxube.tests.time_tests.test_envenumerableacts"
module: "deepxube.tests.time_tests"
file: "deepxube/tests/time_tests.py"
line_start: 116
line_end: 129
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "env"
    annotation: "ActsEnum"
    default: null
  - name: "states"
    annotation: "List[State]"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:torch.set_num_threads"
    expr: "torch.set_num_threads"
    call_sites: [118]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [121, 126]
  - target: null
    expr: "env.expand"
    call_sites: [122]
  - target: null
    expr: "float"
    call_sites: [123, 124]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [123, 124]
  - target: null
    expr: "len"
    call_sites: [123, 127, 129]
  - target: "func:deepxube.utils.misc_utils.flatten"
    expr: "flatten"
    call_sites: [124]
  - target: null
    expr: "print"
    call_sites: [128]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.tests.time_tests.test_envenumerableacts`

**File:** [deepxube/tests/time_tests.py:116](../../../../deepxube/tests/time_tests.py#L116)
**Visibility:** public
**Kind:** function

## Signature

```python
def test_envenumerableacts(env: ActsEnum, states: List[State]) -> None
```

## Docstring

Time full state expansion for domains with enumerable actions. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `env` | `ActsEnum` | — |
| `states` | `List[State]` | — |

## Returns

`None`

## Calls

- `torch.set_num_threads` → `func:torch.set_num_threads` (lines: 118)
- `time.time` → `func:time.time` (lines: 121, 126)
- `np.mean` → `func:numpy.mean` (lines: 123, 124)
- `flatten` → `func:deepxube.utils.misc_utils.flatten` (lines: 124)

### Unresolved
- `env.expand` (lines: 122)
- `float` (lines: 123, 124)
- `len` (lines: 123, 127, 129)
- `print` (lines: 128)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def test_envenumerableacts(env: ActsEnum, states: List[State]) -> None:
    """ Time full state expansion for domains with enumerable actions. """
    torch.set_num_threads(1)

    # expand
    start_time = time.time()
    states_exp, _, tcs = env.expand(states)
    ave_next_states: float = float(np.mean([len(x) for x in states_exp]))
    ave_tc: float = float(np.mean(flatten(tcs)[0]))

    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print(f"Expanded %i states, mean #next/tc: ({ave_next_states:.2f}/{ave_tc:.2f}), "
          f"in %s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))
```
