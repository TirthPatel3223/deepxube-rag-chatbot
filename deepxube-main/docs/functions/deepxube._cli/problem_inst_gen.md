---
id: "func:deepxube._cli.problem_inst_gen"
kind: "function"
name: "problem_inst_gen"
qualified_name: "deepxube._cli.problem_inst_gen"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 283
line_end: 303
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
    expr: "os.path.isfile"
    call_sites: [285]
  - target: null
    expr: "print"
    call_sites: [286, 291, 294, 296, 303]
  - target: "func:deepxube.utils.command_line_utils.get_domain_from_arg"
    expr: "get_domain_from_arg"
    call_sites: [289]
  - target: null
    expr: "list"
    call_sites: [290]
  - target: null
    expr: "np.random.randint"
    call_sites: [290]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [292, 294, 297, 303]
  - target: null
    expr: "domain.sample_problem_instances"
    call_sites: [293]
  - target: null
    expr: "dict"
    call_sites: [298]
  - target: "func:pickle.dump"
    expr: "pickle.dump"
    call_sites: [302]
  - target: null
    expr: "open"
    call_sites: [302]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli.problem_inst_gen`

**File:** [deepxube/_cli.py:283](../../../../deepxube/_cli.py#L283)
**Visibility:** public
**Kind:** function

## Signature

```python
def problem_inst_gen(args: argparse.Namespace) -> None
```

## Docstring

Generate random problem instances by walking from solved states and save them to a pickle file. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `args` | `argparse.Namespace` | — |

## Returns

`None`

## Calls

- `get_domain_from_arg` → `func:deepxube.utils.command_line_utils.get_domain_from_arg` (lines: 289)
- `time.time` → `func:time.time` (lines: 292, 294, 297, 303)
- `pickle.dump` → `func:pickle.dump` (lines: 302)

### Unresolved
- `os.path.isfile` (lines: 285)
- `print` (lines: 286, 291, 294, 296, 303)
- `list` (lines: 290)
- `np.random.randint` (lines: 290)
- `domain.sample_problem_instances` (lines: 293)
- `dict` (lines: 298)
- `open` (lines: 302)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def problem_inst_gen(args: argparse.Namespace) -> None:
    """ Generate random problem instances by walking from solved states and save them to a pickle file. """
    if os.path.isfile(args.file) and (not args.redo):
        print(f"File {args.file} already exists and redo not set. Not generating data.")
        return

    domain, _ = get_domain_from_arg(args.domain)
    num_steps_l: List[int] = list(np.random.randint(args.step_min, args.step_max + 1, size=args.num))
    print(f"Generating {args.num} states")
    start_time = time.time()
    states, goals = domain.sample_problem_instances(num_steps_l)
    print(f"Time: {time.time() - start_time}")

    print(f"Saving data to {args.file}")
    start_time = time.time()
    data: Dict = dict()
    data['states'] = states
    data['goals'] = goals
    # noinspection PyTypeChecker
    pickle.dump(data, open(args.file, "wb"), protocol=-1)
    print(f"Time: {time.time() - start_time}")
```
