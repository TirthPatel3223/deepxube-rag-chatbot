---
id: "func:tests.test_domains.test_actsrev"
kind: "function"
name: "test_actsrev"
qualified_name: "tests.test_domains.test_actsrev"
module: "tests.test_domains"
file: "tests/test_domains.py"
line_start: 80
line_end: 87
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators:
  - "@pytest.mark.parametrize('num_states', [1, 5, 10])"
parameters:
  - name: "domain_actsrev"
    annotation: "ActsRev"
    default: null
  - name: "num_states"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "domain_actsrev.sample_problem_instances"
    call_sites: [82]
  - target: null
    expr: "list"
    call_sites: [82]
  - target: null
    expr: "range"
    call_sites: [82]
  - target: null
    expr: "domain_actsrev.sample_state_action"
    call_sites: [83]
  - target: null
    expr: "domain_actsrev.next_state"
    call_sites: [84, 86]
  - target: null
    expr: "domain_actsrev.rev_action"
    call_sites: [85]
  - target: null
    expr: "all"
    call_sites: [87]
  - target: null
    expr: "zip"
    call_sites: [87]
raises: []
reads_attrs: []
writes_attrs: []
---

# `tests.test_domains.test_actsrev`

**File:** [tests/test_domains.py:80](../../../../tests/test_domains.py#L80)
**Visibility:** public
**Kind:** function
**Decorators:** `@pytest.mark.parametrize('num_states', [1, 5, 10])`

## Signature

```python
def test_actsrev(domain_actsrev: ActsRev, num_states: int) -> None
```

## Docstring

Assert that applying an action and then its reverse returns to the original state. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain_actsrev` | `ActsRev` | — |
| `num_states` | `int` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `domain_actsrev.sample_problem_instances` (lines: 82)
- `list` (lines: 82)
- `range` (lines: 82)
- `domain_actsrev.sample_state_action` (lines: 83)
- `domain_actsrev.next_state` (lines: 84, 86)
- `domain_actsrev.rev_action` (lines: 85)
- `all` (lines: 87)
- `zip` (lines: 87)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def test_actsrev(domain_actsrev: ActsRev, num_states: int) -> None:
    """ Assert that applying an action and then its reverse returns to the original state. """
    states, _ = domain_actsrev.sample_problem_instances(list(range(0, num_states)))
    actions: List[Action] = domain_actsrev.sample_state_action(states)
    states_next: List[State] = domain_actsrev.next_state(states, actions)[0]
    actions_rev: List[Action] = domain_actsrev.rev_action(states_next, actions)
    states_rev: List[State] = domain_actsrev.next_state(states_next, actions_rev)[0]
    assert all(state == state_rev for state, state_rev in zip(states, states_rev))
```
