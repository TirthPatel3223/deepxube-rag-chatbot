---
id: "func:deepxube.trainers.utils.train_loop.test"
kind: "function"
name: "test"
qualified_name: "deepxube.trainers.utils.train_loop.test"
module: "deepxube.trainers.utils.train_loop"
file: "deepxube/trainers/utils/train_loop.py"
line_start: 226
line_end: 254
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
  - name: "writer"
    annotation: "SummaryWriter"
    default: null
  - name: "curr_itr"
    annotation: "int"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "print"
    call_sites: [229, 254]
  - target: null
    expr: "len"
    call_sites: [229, 230]
  - target: null
    expr: "range"
    call_sites: [230, 237]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [231, 244]
  - target: "func:deepxube.trainers.utils.train_loop.get_pathfind_w_instances"
    expr: "get_pathfind_w_instances"
    call_sites: [234]
  - target: null
    expr: "pathfind.step"
    call_sites: [238]
  - target: "func:deepxube.pathfinding.utils.performance.PathFindPerf"
    expr: "PathFindPerf"
    call_sites: [241]
  - target: null
    expr: "pathfind_perf.update_perf"
    call_sites: [243]
  - target: null
    expr: "pathfind_perf.stats"
    call_sites: [247]
  - target: null
    expr: "writer.add_scalar"
    call_sites: [251, 252, 253]
  - target: null
    expr: "', '.join"
    call_sites: [254]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.trainers.utils.train_loop.test`

**File:** [deepxube/trainers/utils/train_loop.py:226](../../../../deepxube/trainers/utils/train_loop.py#L226)
**Visibility:** public
**Kind:** function

## Signature

```python
def test(domain: Domain, heur_nnet_par: Optional[HeurNNetPar], train_heur: Optional[TrainHeur], policy_nnet_par: Optional[PolicyNNetPar], train_policy: Optional[TrainPolicy], test_args: TestArgs, writer: SummaryWriter, curr_itr: int) -> None
```

## Docstring

Run each pathfinding algorithm in ``test_args`` for ``search_itrs`` steps and log solve rates to TensorBoard. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `heur_nnet_par` | `Optional[HeurNNetPar]` | — |
| `train_heur` | `Optional[TrainHeur]` | — |
| `policy_nnet_par` | `Optional[PolicyNNetPar]` | — |
| `train_policy` | `Optional[TrainPolicy]` | — |
| `test_args` | `TestArgs` | — |
| `writer` | `SummaryWriter` | — |
| `curr_itr` | `int` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 231, 244)
- `get_pathfind_w_instances` → `func:deepxube.trainers.utils.train_loop.get_pathfind_w_instances` (lines: 234)
- `PathFindPerf` → `func:deepxube.pathfinding.utils.performance.PathFindPerf` (lines: 241)

### Unresolved
- `print` (lines: 229, 254)
- `len` (lines: 229, 230)
- `range` (lines: 230, 237)
- `pathfind.step` (lines: 238)
- `pathfind_perf.update_perf` (lines: 243)
- `pathfind_perf.stats` (lines: 247)
- `writer.add_scalar` (lines: 251, 252, 253)
- `', '.join` (lines: 254)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def test(domain: Domain, heur_nnet_par: Optional[HeurNNetPar], train_heur: Optional[TrainHeur], policy_nnet_par: Optional[PolicyNNetPar],
         train_policy: Optional[TrainPolicy], test_args: TestArgs, writer: SummaryWriter, curr_itr: int) -> None:
    """ Run each pathfinding algorithm in ``test_args`` for ``search_itrs`` steps and log solve rates to TensorBoard. """
    print(f"Testing - itr: {curr_itr}, num_inst: {len(test_args.test_states)}, num_pathfinds: {len(test_args.pathfinds)}")
    for pathfind_idx in range(len(test_args.pathfinds)):
        start_time = time.time()
        # get pathfinding alg with test instances
        pathfind_arg: str = test_args.pathfinds[pathfind_idx]
        pathfind: PathFind = get_pathfind_w_instances(domain, heur_nnet_par, train_heur, policy_nnet_par, train_policy, test_args, pathfind_arg)

        # attempt to solve
        for _ in range(test_args.search_itrs):
            pathfind.step()

        # get performacne
        pathfind_perf: PathFindPerf = PathFindPerf()
        for instance in pathfind.instances:
            pathfind_perf.update_perf(instance)
        test_time = time.time() - start_time

        # log
        per_solved_ave, path_cost_ave, search_itrs_ave = pathfind_perf.stats()
        test_info_l: List[str] = [f"%solved: {per_solved_ave:.2f}", f"path_costs: {path_cost_ave:.3f}",
                                  f"search_itrs: {search_itrs_ave:.3f}",
                                  f"test_time: {test_time:.2f}"]
        writer.add_scalar(f"val/{pathfind_arg}/solved", per_solved_ave, curr_itr)
        writer.add_scalar(f"val/{pathfind_arg}/path_cost", path_cost_ave, curr_itr)
        writer.add_scalar(f"val/{pathfind_arg}/search_itrs", search_itrs_ave, curr_itr)
        print(f"Test {pathfind_arg} - {', '.join(test_info_l)}")
```
