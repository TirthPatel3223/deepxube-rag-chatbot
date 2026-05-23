---
id: "class:deepxube.trainers.utils.train_loop.TestArgs"
kind: "class"
name: "TestArgs"
qualified_name: "deepxube.trainers.utils.train_loop.TestArgs"
module: "deepxube.trainers.utils.train_loop"
file: "deepxube/trainers/utils/train_loop.py"
line_start: 30
line_end: 43
is_abstract: false
is_dataclass: true
decorators:
  - "@dataclass"
generic_parameters: []
bases: []
methods:
  - "func:deepxube.trainers.utils.train_loop.TestArgs.__repr__"
attributes:
  - name: "test_states"
    annotation: "List[State]"
    default: null
    from: "class_body"
  - name: "test_goals"
    annotation: "List[Goal]"
    default: null
    from: "class_body"
  - name: "search_itrs"
    annotation: "int"
    default: null
    from: "class_body"
  - name: "pathfinds"
    annotation: "List[str]"
    default: null
    from: "class_body"
  - name: "test_nnet_batch_size"
    annotation: "int"
    default: null
    from: "class_body"
  - name: "test_up_freq"
    annotation: "int"
    default: null
    from: "class_body"
  - name: "test_init"
    annotation: "bool"
    default: null
    from: "class_body"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.trainers.utils.train_loop.TestArgs`

**File:** [deepxube/trainers/utils/train_loop.py:30](../../../deepxube/trainers/utils/train_loop.py#L30)
**Abstract:** no
**Dataclass:** yes
**Decorators:** `@dataclass`

## Docstring

Configuration for periodic test evaluations: test states/goals, search budget, and algorithms to benchmark. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `test_states` | `List[State]` | class_body |
| `test_goals` | `List[Goal]` | class_body |
| `search_itrs` | `int` | class_body |
| `pathfinds` | `List[str]` | class_body |
| `test_nnet_batch_size` | `int` | class_body |
| `test_up_freq` | `int` | class_body |
| `test_init` | `bool` | class_body |

## Source

```python
class TestArgs:
    """ Configuration for periodic test evaluations: test states/goals, search budget, and algorithms to benchmark. """
    test_states: List[State]
    test_goals: List[Goal]
    search_itrs: int
    pathfinds: List[str]
    test_nnet_batch_size: int
    test_up_freq: int
    test_init: bool

    def __repr__(self) -> str:
        return (f"TestArgs(instances={len(self.test_states)}, search_itrs={self.search_itrs}, "
                f"pathfinds={self.pathfinds}, test_nnet_batch_size={self.test_nnet_batch_size}, "
                f"test_up_freq={self.test_up_freq}, test_init={self.test_init})")
```
