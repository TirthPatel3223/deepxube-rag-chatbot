---
id: "func:deepxube.trainers.utils.train_loop.get_pathfind"
kind: "function"
name: "get_pathfind"
qualified_name: "deepxube.trainers.utils.train_loop.get_pathfind"
module: "deepxube.trainers.utils.train_loop"
file: "deepxube/trainers/utils/train_loop.py"
line_start: 64
line_end: 79
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "domain"
    annotation: "Domain"
    default: null
  - name: "heur_nnet_par"
    annotation: "Optional[HeurNNetPar]"
    default: null
  - name: "train_heur"
    annotation: "Optional[TrainHeur]"
    default: null
  - name: "policy_nnet_par"
    annotation: "Optional[PolicyNNetPar]"
    default: null
  - name: "train_policy"
    annotation: "Optional[TrainPolicy]"
    default: null
  - name: "test_nnet_batch_size"
    annotation: "int"
    default: null
  - name: "pathfind_arg"
    annotation: "str"
    default: null
returns: "PathFind"
docstring_source: "present"
callees:
  - target: null
    expr: "heur_nnet_par.get_nnet_fn"
    call_sites: [71]
  - target: null
    expr: "policy_nnet_par.get_nnet_fn"
    call_sites: [74]
  - target: "func:deepxube.factories.pathfinding_factory.get_pathfind_functions"
    expr: "get_pathfind_functions"
    call_sites: [76]
  - target: "func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs"
    expr: "get_pathfind_name_kwargs"
    call_sites: [76]
  - target: "func:deepxube.utils.command_line_utils.get_pathfind_from_arg"
    expr: "get_pathfind_from_arg"
    call_sites: [77]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.trainers.utils.train_loop.get_pathfind`

**File:** [deepxube/trainers/utils/train_loop.py:64](../../../../deepxube/trainers/utils/train_loop.py#L64)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_pathfind(domain: Domain, heur_nnet_par: Optional[HeurNNetPar], train_heur: Optional[TrainHeur], policy_nnet_par: Optional[PolicyNNetPar], train_policy: Optional[TrainPolicy], test_nnet_batch_size: int, pathfind_arg: str) -> PathFind
```

## Docstring

:return: A ``PathFind`` built from the current nnet weights for the given ``pathfind_arg`` CLI string. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `heur_nnet_par` | `Optional[HeurNNetPar]` | — |
| `train_heur` | `Optional[TrainHeur]` | — |
| `policy_nnet_par` | `Optional[PolicyNNetPar]` | — |
| `train_policy` | `Optional[TrainPolicy]` | — |
| `test_nnet_batch_size` | `int` | — |
| `pathfind_arg` | `str` | — |

## Returns

`PathFind`

## Calls

- `get_pathfind_functions` → `func:deepxube.factories.pathfinding_factory.get_pathfind_functions` (lines: 76)
- `get_pathfind_name_kwargs` → `func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs` (lines: 76)
- `get_pathfind_from_arg` → `func:deepxube.utils.command_line_utils.get_pathfind_from_arg` (lines: 77)

### Unresolved
- `heur_nnet_par.get_nnet_fn` (lines: 71)
- `policy_nnet_par.get_nnet_fn` (lines: 74)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_pathfind(domain: Domain, heur_nnet_par: Optional[HeurNNetPar], train_heur: Optional[TrainHeur], policy_nnet_par: Optional[PolicyNNetPar],
                 train_policy: Optional[TrainPolicy], test_nnet_batch_size: int, pathfind_arg: str) -> PathFind:
    """ :return: A ``PathFind`` built from the current nnet weights for the given ``pathfind_arg`` CLI string. """
    heur_fn: Optional[HeurFn] = None
    policy_fn: Optional[PolicyFn] = None
    if heur_nnet_par is not None:
        assert train_heur is not None
        heur_fn = heur_nnet_par.get_nnet_fn(train_heur.nnet, test_nnet_batch_size, train_heur.device, None)
    if policy_nnet_par is not None:
        assert train_policy is not None
        policy_fn = policy_nnet_par.get_nnet_fn(train_policy.nnet, test_nnet_batch_size, train_policy.device, None)

    pathfind_functions: Any = get_pathfind_functions(get_pathfind_name_kwargs(pathfind_arg)[0], heur_fn, policy_fn)
    pathfind: PathFind = get_pathfind_from_arg(domain, pathfind_functions, pathfind_arg)[0]

    return pathfind
```
