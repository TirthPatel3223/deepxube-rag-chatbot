---
id: "func:deepxube.trainers.utils.train_loop.get_pathfind_w_instances"
kind: "function"
name: "get_pathfind_w_instances"
qualified_name: "deepxube.trainers.utils.train_loop.get_pathfind_w_instances"
module: "deepxube.trainers.utils.train_loop"
file: "deepxube/trainers/utils/train_loop.py"
line_start: 215
line_end: 223
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
  - name: "test_args"
    annotation: "TestArgs"
    default: null
  - name: "pathfind_arg"
    annotation: "str"
    default: null
returns: "PathFind"
docstring_source: "present"
callees:
  - target: "func:deepxube.trainers.utils.train_loop.get_pathfind"
    expr: "get_pathfind"
    call_sites: [218]
  - target: null
    expr: "pathfind.make_instances"
    call_sites: [220]
  - target: null
    expr: "pathfind.add_instances"
    call_sites: [221]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.trainers.utils.train_loop.get_pathfind_w_instances`

**File:** [deepxube/trainers/utils/train_loop.py:215](../../../../deepxube/trainers/utils/train_loop.py#L215)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_pathfind_w_instances(domain: Domain, heur_nnet_par: Optional[HeurNNetPar], train_heur: Optional[TrainHeur], policy_nnet_par: Optional[PolicyNNetPar], train_policy: Optional[TrainPolicy], test_args: TestArgs, pathfind_arg: str) -> PathFind
```

## Docstring

:return: A ``PathFind`` with test instances from ``test_args`` already created and added. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `heur_nnet_par` | `Optional[HeurNNetPar]` | — |
| `train_heur` | `Optional[TrainHeur]` | — |
| `policy_nnet_par` | `Optional[PolicyNNetPar]` | — |
| `train_policy` | `Optional[TrainPolicy]` | — |
| `test_args` | `TestArgs` | — |
| `pathfind_arg` | `str` | — |

## Returns

`PathFind`

## Calls

- `get_pathfind` → `func:deepxube.trainers.utils.train_loop.get_pathfind` (lines: 218)

### Unresolved
- `pathfind.make_instances` (lines: 220)
- `pathfind.add_instances` (lines: 221)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def get_pathfind_w_instances(domain: Domain, heur_nnet_par: Optional[HeurNNetPar], train_heur: Optional[TrainHeur], policy_nnet_par: Optional[PolicyNNetPar],
                             train_policy: Optional[TrainPolicy], test_args: TestArgs, pathfind_arg: str) -> PathFind:
    """ :return: A ``PathFind`` with test instances from ``test_args`` already created and added. """
    pathfind: PathFind = get_pathfind(domain, heur_nnet_par, train_heur, policy_nnet_par, train_policy, test_args.test_nnet_batch_size, pathfind_arg)

    instances: List[Instance] = pathfind.make_instances(test_args.test_states, test_args.test_goals, None, True)
    pathfind.add_instances(instances)

    return pathfind
```
