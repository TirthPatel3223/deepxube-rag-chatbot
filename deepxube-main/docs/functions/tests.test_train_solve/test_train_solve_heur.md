---
id: "func:tests.test_train_solve.test_train_solve_heur"
kind: "function"
name: "test_train_solve_heur"
qualified_name: "tests.test_train_solve.test_train_solve_heur"
module: "tests.test_train_solve"
file: "tests/test_train_solve.py"
line_start: 45
line_end: 110
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators:
  - "@pytest.mark.parametrize('pathfind_tr_str,pathfind_solve_str,heur_type,bal,ub_heur_solns,backup,sync_main,soln_thresh', cases)"
parameters:
  - name: "pathfind_tr_str"
    annotation: "str"
    default: null
  - name: "pathfind_solve_str"
    annotation: "str"
    default: null
  - name: "heur_type"
    annotation: "str"
    default: null
  - name: "bal"
    annotation: "bool"
    default: null
  - name: "ub_heur_solns"
    annotation: "bool"
    default: null
  - name: "backup"
    annotation: "int"
    default: null
  - name: "sync_main"
    annotation: "bool"
    default: null
  - name: "soln_thresh"
    annotation: "float"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.command_line_utils.get_domain_from_arg"
    expr: "get_domain_from_arg"
    call_sites: [51]
  - target: "func:deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg"
    expr: "get_heur_nnet_par_from_arg"
    call_sites: [52]
  - target: "func:deepxube.base.updater.UpArgs"
    expr: "UpArgs"
    call_sites: [55]
  - target: "func:deepxube.factories.updater_factory.get_updater"
    expr: "get_updater"
    call_sites: [58]
  - target: null
    expr: "isinstance"
    call_sites: [59]
  - target: "func:deepxube.base.trainer.TrainArgs"
    expr: "TrainArgs"
    call_sites: [63]
  - target: null
    expr: "os.path.exists"
    call_sites: [67]
  - target: "func:shutil.rmtree"
    expr: "shutil.rmtree"
    call_sites: [68]
  - target: "func:deepxube.trainers.utils.train_loop.train"
    expr: "train"
    call_sites: [70]
  - target: "func:deepxube.nnet.nnet_utils.get_device"
    expr: "nnet_utils.get_device"
    call_sites: [74]
  - target: "func:deepxube.nnet.nnet_utils.load_nnet"
    expr: "nnet_utils.load_nnet"
    call_sites: [76]
  - target: null
    expr: "heur_nnet_par.get_nnet"
    call_sites: [76]
  - target: null
    expr: "nnet.eval"
    call_sites: [77]
  - target: null
    expr: "nnet.to"
    call_sites: [78]
  - target: "func:torch.nn.DataParallel"
    expr: "nn.DataParallel"
    call_sites: [79]
  - target: null
    expr: "heur_nnet_par.get_nnet_fn"
    call_sites: [80]
  - target: "func:deepxube.base.pathfinding.FNsHeurV"
    expr: "FNsHeurV"
    call_sites: [85]
  - target: "func:deepxube.base.pathfinding.FNsHeurQ"
    expr: "FNsHeurQ"
    call_sites: [87]
  - target: "func:deepxube.utils.command_line_utils.get_pathfind_from_arg"
    expr: "get_pathfind_from_arg"
    call_sites: [89]
  - target: null
    expr: "domain.sample_problem_instances"
    call_sites: [90]
  - target: null
    expr: "list"
    call_sites: [90]
  - target: null
    expr: "range"
    call_sites: [90, 93]
  - target: null
    expr: "pathfind.make_instances"
    call_sites: [91]
  - target: null
    expr: "pathfind.add_instances"
    call_sites: [92]
  - target: null
    expr: "pathfind.step"
    call_sites: [94]
  - target: "func:deepxube.pathfinding.utils.performance.PathFindPerf"
    expr: "PathFindPerf"
    call_sites: [97]
  - target: null
    expr: "pathfind_perf.update_perf"
    call_sites: [100]
  - target: "func:deepxube.base.pathfinding.get_path"
    expr: "get_path"
    call_sites: [105]
  - target: "func:deepxube.pathfinding.utils.performance.is_valid_soln"
    expr: "is_valid_soln"
    call_sites: [106]
  - target: null
    expr: "print"
    call_sites: [108]
  - target: null
    expr: "pathfind_perf.to_string"
    call_sites: [108]
  - target: null
    expr: "pathfind_perf.per_solved"
    call_sites: [109]
raises: []
reads_attrs: []
writes_attrs: []
---

# `tests.test_train_solve.test_train_solve_heur`

**File:** [tests/test_train_solve.py:45](../../../../tests/test_train_solve.py#L45)
**Visibility:** public
**Kind:** function
**Decorators:** `@pytest.mark.parametrize('pathfind_tr_str,pathfind_solve_str,heur_type,bal,ub_heur_solns,backup,sync_main,soln_thresh', cases)`

## Signature

```python
def test_train_solve_heur(pathfind_tr_str: str, pathfind_solve_str: str, heur_type: str, bal: bool, ub_heur_solns: bool, backup: int, sync_main: bool, soln_thresh: float) -> None
```

## Docstring

Train a heuristic on Grid 7×7 and assert solve rate on 100 instances meets ``soln_thresh``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `pathfind_tr_str` | `str` | — |
| `pathfind_solve_str` | `str` | — |
| `heur_type` | `str` | — |
| `bal` | `bool` | — |
| `ub_heur_solns` | `bool` | — |
| `backup` | `int` | — |
| `sync_main` | `bool` | — |
| `soln_thresh` | `float` | — |

## Returns

`None`

## Calls

- `get_domain_from_arg` → `func:deepxube.utils.command_line_utils.get_domain_from_arg` (lines: 51)
- `get_heur_nnet_par_from_arg` → `func:deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg` (lines: 52)
- `UpArgs` → `func:deepxube.base.updater.UpArgs` (lines: 55)
- `get_updater` → `func:deepxube.factories.updater_factory.get_updater` (lines: 58)
- `TrainArgs` → `func:deepxube.base.trainer.TrainArgs` (lines: 63)
- `shutil.rmtree` → `func:shutil.rmtree` (lines: 68)
- `train` → `func:deepxube.trainers.utils.train_loop.train` (lines: 70)
- `nnet_utils.get_device` → `func:deepxube.nnet.nnet_utils.get_device` (lines: 74)
- `nnet_utils.load_nnet` → `func:deepxube.nnet.nnet_utils.load_nnet` (lines: 76)
- `nn.DataParallel` → `func:torch.nn.DataParallel` (lines: 79)
- `FNsHeurV` → `func:deepxube.base.pathfinding.FNsHeurV` (lines: 85)
- `FNsHeurQ` → `func:deepxube.base.pathfinding.FNsHeurQ` (lines: 87)
- `get_pathfind_from_arg` → `func:deepxube.utils.command_line_utils.get_pathfind_from_arg` (lines: 89)
- `PathFindPerf` → `func:deepxube.pathfinding.utils.performance.PathFindPerf` (lines: 97)
- `get_path` → `func:deepxube.base.pathfinding.get_path` (lines: 105)
- `is_valid_soln` → `func:deepxube.pathfinding.utils.performance.is_valid_soln` (lines: 106)

### Unresolved
- `isinstance` (lines: 59)
- `os.path.exists` (lines: 67)
- `heur_nnet_par.get_nnet` (lines: 76)
- `nnet.eval` (lines: 77)
- `nnet.to` (lines: 78)
- `heur_nnet_par.get_nnet_fn` (lines: 80)
- `domain.sample_problem_instances` (lines: 90)
- `list` (lines: 90)
- `range` (lines: 90, 93)
- `pathfind.make_instances` (lines: 91)
- `pathfind.add_instances` (lines: 92)
- `pathfind.step` (lines: 94)
- `pathfind_perf.update_perf` (lines: 100)
- `print` (lines: 108)
- `pathfind_perf.to_string` (lines: 108)
- `pathfind_perf.per_solved` (lines: 109)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def test_train_solve_heur(pathfind_tr_str: str, pathfind_solve_str: str, heur_type: str, bal: bool, ub_heur_solns: bool, backup: int, sync_main: bool,
                          soln_thresh: float) -> None:
    """ Train a heuristic on Grid 7×7 and assert solve rate on 100 instances meets ``soln_thresh``. """
    domain_str: str = "grid.7"
    heur_str: str = "resnet_fc.100H_1B_bn"
    search_itrs: int = 20
    domain, domain_name = get_domain_from_arg(domain_str)
    heur_nnet_par: HeurNNetPar = get_heur_nnet_par_from_arg(domain, domain_name, heur_str, heur_type)[0]

    # update args
    up_args: UpArgs = UpArgs(1, 100, 100, search_itrs, ub_heur_solns=ub_heur_solns, backup=backup, sync_main=sync_main)

    # updater
    updater_ret: Update = get_updater(domain, pathfind_tr_str, up_args, False, "heur")
    assert isinstance(updater_ret, UpdateHeur)
    updater: UpdateHeur = updater_ret

    # train args
    train_args: TrainArgs = TrainArgs(50, 2000, bal, display=0)

    # train
    save_dir: str = "tests/dummy/"
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)

    train(domain, heur_nnet_par, updater, None, None, save_dir, train_args)

    # solve
    heur_file: str = f"{save_dir}/heur.pt"
    device, devices, on_gpu = nnet_utils.get_device()

    nnet: nn.Module = nnet_utils.load_nnet(heur_file, heur_nnet_par.get_nnet())
    nnet.eval()
    nnet.to(device)
    nnet = nn.DataParallel(nnet)
    heur_fn = heur_nnet_par.get_nnet_fn(nnet, None, device, None)

    # do pathfinding
    functions: Any
    if heur_type == "V":
        functions = FNsHeurV(heur_fn)
    else:
        functions = FNsHeurQ(heur_fn)

    pathfind: PathFind = get_pathfind_from_arg(domain, functions, pathfind_solve_str)[0]
    states, goals = domain.sample_problem_instances(list(range(0, 100)))
    instances: List[Instance] = pathfind.make_instances(states, goals, None, True)
    pathfind.add_instances(instances)
    for _ in range(search_itrs):
        pathfind.step()

    # get pathfind perf
    pathfind_perf: PathFindPerf = PathFindPerf()
    instance: Instance
    for instance in pathfind.instances:
        pathfind_perf.update_perf(instance)

        # check soln
        goal_node: Optional[Node] = instance.goal_node
        if goal_node is not None:
            path_states, path_actions, path_cost = get_path(goal_node)
            assert is_valid_soln(instance.root_node.state, instance.root_node.goal, path_actions, domain)

    print(pathfind_perf.to_string())
    per_solved: float = pathfind_perf.per_solved()
    assert per_solved >= soln_thresh, f"Should solve at least 90%, but solved {per_solved}"
```
