---
id: "func:deepxube._solve.solve_cli"
kind: "function"
name: "solve_cli"
qualified_name: "deepxube._solve.solve_cli"
module: "deepxube._solve"
file: "deepxube/_solve.py"
line_start: 120
line_end: 216
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "args"
    annotation: "argparse.Namespace"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "os.path.exists"
    call_sites: [122]
  - target: "func:os.makedirs"
    expr: "os.makedirs"
    call_sites: [123]
  - target: "func:deepxube.utils.command_line_utils.get_domain_from_arg"
    expr: "get_domain_from_arg"
    call_sites: [126]
  - target: "func:deepxube._solve.get_heur_fn"
    expr: "get_heur_fn"
    call_sites: [129]
  - target: "func:deepxube._solve.get_policy_fn"
    expr: "get_policy_fn"
    call_sites: [130]
  - target: null
    expr: "print"
    call_sites: [131, 134, 204, 208, 209, 213]
  - target: "func:deepxube.factories.pathfinding_factory.get_pathfind_functions"
    expr: "get_pathfind_functions"
    call_sites: [132]
  - target: "func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs"
    expr: "get_pathfind_name_kwargs"
    call_sites: [132]
  - target: "func:deepxube.utils.command_line_utils.get_pathfind_from_arg"
    expr: "get_pathfind_from_arg"
    call_sites: [133, 167]
  - target: "func:pickle.load"
    expr: "pickle.load"
    call_sites: [137, 150]
  - target: null
    expr: "open"
    call_sites: [137, 150, 216]
  - target: null
    expr: "os.path.isfile"
    call_sites: [145]
  - target: "func:deepxube.utils.data_utils.Logger"
    expr: "data_utils.Logger"
    call_sites: [152, 157]
  - target: null
    expr: "len"
    call_sites: [160, 161]
  - target: null
    expr: "range"
    call_sites: [161]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [170, 177, 179]
  - target: null
    expr: "pathfind.make_instances"
    call_sites: [172]
  - target: null
    expr: "pathfind.add_instances"
    call_sites: [173]
  - target: null
    expr: "min"
    call_sites: [174]
  - target: null
    expr: "x.finished"
    call_sites: [174]
  - target: null
    expr: "pathfind.step"
    call_sites: [175]
  - target: "func:deepxube.base.pathfinding.get_path"
    expr: "get_path"
    call_sites: [190]
  - target: "func:deepxube.pathfinding.utils.performance.is_valid_soln"
    expr: "is_valid_soln"
    call_sites: [191]
  - target: null
    expr: "results['actions'].append"
    call_sites: [194]
  - target: null
    expr: "results['states_on_path'].append"
    call_sites: [195]
  - target: null
    expr: "results['path_costs'].append"
    call_sites: [196]
  - target: null
    expr: "results['iterations'].append"
    call_sites: [197]
  - target: null
    expr: "results['itrs/sec'].append"
    call_sites: [198]
  - target: null
    expr: "results['times'].append"
    call_sites: [199]
  - target: null
    expr: "results['num_nodes_generated'].append"
    call_sites: [200]
  - target: null
    expr: "results['solved'].append"
    call_sites: [201]
  - target: null
    expr: "format"
    call_sites: [205]
  - target: null
    expr: "pathfind.times.get_time_str"
    call_sites: [208]
  - target: "func:deepxube._solve._get_mean"
    expr: "_get_mean"
    call_sites: [210, 211, 212]
  - target: "func:numpy.mean"
    expr: "np.mean"
    call_sites: [212]
  - target: "func:pickle.dump"
    expr: "pickle.dump"
    call_sites: [216]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._solve.solve_cli`

**File:** [deepxube/_solve.py:120](../../../../deepxube/_solve.py#L120)
**Visibility:** public
**Kind:** function

## Signature

```python
def solve_cli(args: argparse.Namespace) -> None
```

## Docstring

Iterate over problem instances, run pathfinding, validate solutions, and persist results to disk. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `args` | `argparse.Namespace` | — |

## Returns

`None`

## Calls

- `os.makedirs` → `func:os.makedirs` (lines: 123)
- `get_domain_from_arg` → `func:deepxube.utils.command_line_utils.get_domain_from_arg` (lines: 126)
- `get_heur_fn` → `func:deepxube._solve.get_heur_fn` (lines: 129)
- `get_policy_fn` → `func:deepxube._solve.get_policy_fn` (lines: 130)
- `get_pathfind_functions` → `func:deepxube.factories.pathfinding_factory.get_pathfind_functions` (lines: 132)
- `get_pathfind_name_kwargs` → `func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs` (lines: 132)
- `get_pathfind_from_arg` → `func:deepxube.utils.command_line_utils.get_pathfind_from_arg` (lines: 133, 167)
- `pickle.load` → `func:pickle.load` (lines: 137, 150)
- `data_utils.Logger` → `func:deepxube.utils.data_utils.Logger` (lines: 152, 157)
- `time.time` → `func:time.time` (lines: 170, 177, 179)
- `get_path` → `func:deepxube.base.pathfinding.get_path` (lines: 190)
- `is_valid_soln` → `func:deepxube.pathfinding.utils.performance.is_valid_soln` (lines: 191)
- `_get_mean` → `func:deepxube._solve._get_mean` (lines: 210, 211, 212)
- `np.mean` → `func:numpy.mean` (lines: 212)
- `pickle.dump` → `func:pickle.dump` (lines: 216)

### Unresolved
- `os.path.exists` (lines: 122)
- `print` (lines: 131, 134, 204, 208, 209, 213)
- `open` (lines: 137, 150, 216)
- `os.path.isfile` (lines: 145)
- `len` (lines: 160, 161)
- `range` (lines: 161)
- `pathfind.make_instances` (lines: 172)
- `pathfind.add_instances` (lines: 173)
- `min` (lines: 174)
- `x.finished` (lines: 174)
- `pathfind.step` (lines: 175)
- `results['actions'].append` (lines: 194)
- `results['states_on_path'].append` (lines: 195)
- `results['path_costs'].append` (lines: 196)
- `results['iterations'].append` (lines: 197)
- `results['itrs/sec'].append` (lines: 198)
- `results['times'].append` (lines: 199)
- `results['num_nodes_generated'].append` (lines: 200)
- `results['solved'].append` (lines: 201)
- `format` (lines: 205)
- `pathfind.times.get_time_str` (lines: 208)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def solve_cli(args: argparse.Namespace) -> None:
    """ Iterate over problem instances, run pathfinding, validate solutions, and persist results to disk. """
    if not os.path.exists(args.results):
        os.makedirs(args.results)

    # domain
    domain, domain_name = get_domain_from_arg(args.domain)

    # heur and policy fn
    heur_fn: Optional[HeurFn] = get_heur_fn(domain, domain_name, args.heur, args.heur_file, args.heur_type, args.nnet_batch_size)
    policy_fn: Optional[PolicyFn] = get_policy_fn(domain, domain_name, args.policy, args.policy_file, args.policy_samp, args.policy_rand, args.nnet_batch_size)
    print(domain)
    pathfind_functions: Any = get_pathfind_functions(get_pathfind_name_kwargs(args.pathfind)[0], heur_fn, policy_fn)
    pathfind: PathFind = get_pathfind_from_arg(domain, pathfind_functions, args.pathfind)[0]
    print(pathfind)

    # get data
    data: Dict = pickle.load(open(args.file, "rb"))
    states: List[State] = data['states']
    goals: List[Goal] = data['goals']

    results_file: str = "%s/results.pkl" % args.results
    output_file: str = "%s/output.txt" % args.results

    has_results: bool = False
    if os.path.isfile(results_file):
        has_results = True

    results: Dict[str, Any]
    if has_results and (not args.redo):
        results = pickle.load(open(results_file, "rb"))
        if not args.debug:
            sys.stdout = data_utils.Logger(output_file, "a")
    else:
        results = {"states": states, "goals": goals, "actions": [], "states_on_path": [], "path_costs": [], "iterations": [], "times": [], "itrs/sec": [],
                   "num_nodes_generated": [], "solved": []}
        if not args.debug:
            sys.stdout = data_utils.Logger(output_file, "w")

    # TODO add arg start_idx
    start_idx = len(results["actions"])
    for state_idx in range(start_idx, len(states)):
        # get problem instance
        state: State = states[state_idx]
        goal: Goal = goals[state_idx]

        # get pathfinding alg
        pathfind = get_pathfind_from_arg(domain, pathfind_functions, args.pathfind)[0]

        # do pathfinding
        start_time = time.time()
        num_itrs: int = 0
        instance: Instance = pathfind.make_instances([state], [goal], None, True)[0]
        pathfind.add_instances([instance])
        while not min(x.finished() for x in pathfind.instances):
            pathfind.step(verbose=args.verbose)
            num_itrs += 1
            if (args.time_limit >= 0) and ((time.time() - start_time) > args.time_limit):
                break
        solve_time = time.time() - start_time

        # record results
        solved: bool = False
        path_states: Optional[List[State]] = None
        path_actions: Optional[List[Action]] = None
        path_cost: float = np.inf
        itrs_per_sec: float = num_itrs / solve_time
        num_nodes_gen_idx: int = pathfind.instances[0].num_nodes_generated
        goal_node: Optional[Node] = pathfind.instances[0].goal_node
        if goal_node is not None:
            path_states, path_actions, path_cost = get_path(goal_node)
            assert is_valid_soln(state, goal, path_actions, domain)
            solved = True

        results["actions"].append(path_actions)
        results["states_on_path"].append(path_states)
        results["path_costs"].append(path_cost)
        results["iterations"].append(num_itrs)
        results["itrs/sec"].append(itrs_per_sec)
        results["times"].append(solve_time)
        results["num_nodes_generated"].append(num_nodes_gen_idx)
        results["solved"].append(solved)

        # print to screen
        print(f"State: %i, SolnCost: %.2f, # Nodes Gen: %s, Itrs: %i, Itrs/sec: %.2f, Solved: {solved}, "
              f"Time: %.2f" % (state_idx, path_cost, format(num_nodes_gen_idx, ","), num_itrs,
                               itrs_per_sec, solve_time))

        print("Times - %s, num_itrs: %i" % (pathfind.times.get_time_str(), num_itrs))
        print("Means - SolnCost: %.2f, # Nodes Gen: %.2f, Itrs: %.2f, Itrs/sec: %.2f, Solved: %.2f%%, "
              "Time: %.2f" % (_get_mean(results, "path_costs"), _get_mean(results, "num_nodes_generated"),
                              _get_mean(results, "iterations"), _get_mean(results, "itrs/sec"),
                              100.0 * np.mean(results["solved"]), _get_mean(results, "times")))
        print("")

        # noinspection PyTypeChecker
        pickle.dump(results, open(results_file, "wb"), protocol=-1)
```
