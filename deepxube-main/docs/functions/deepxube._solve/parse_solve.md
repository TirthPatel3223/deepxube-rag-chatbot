---
id: "func:deepxube._solve.parse_solve"
kind: "function"
name: "parse_solve"
qualified_name: "deepxube._solve.parse_solve"
module: "deepxube._solve"
file: "deepxube/_solve.py"
line_start: 25
line_end: 55
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "parser"
    annotation: "ArgumentParser"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "parser.add_argument"
    call_sites: [27, 29, 31, 32, 36, 38, 39, 40, 42, 43, 45, 47, 48, 49, 52, 53, 54]
  - target: null
    expr: "parser.set_defaults"
    call_sites: [55]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._solve.parse_solve`

**File:** [deepxube/_solve.py:25](../../../../deepxube/_solve.py#L25)
**Visibility:** public
**Kind:** function

## Signature

```python
def parse_solve(parser: ArgumentParser) -> None
```

## Docstring

Register all solve subcommand arguments and set ``solve_cli`` as the handler. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `parser` | `ArgumentParser` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `parser.add_argument` (lines: 27, 29, 31, 32, 36, 38, 39, 40, 42, 43, 45, 47, 48, 49, 52, 53, 54)
- `parser.set_defaults` (lines: 55)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def parse_solve(parser: ArgumentParser) -> None:
    """ Register all solve subcommand arguments and set ``solve_cli`` as the handler. """
    parser.add_argument('--domain', type=str, required=True, help="Domain name and arguments.")

    parser.add_argument('--heur', type=str, default=None, help="Heuristic neural network and arguments. If None then a heuristic whose output is always zero "
                                                               "is used.")
    parser.add_argument('--heur_file', type=str, default=None, help="File that has heuristic nnet. Can be None if using all zeros heuristic.")
    parser.add_argument('--heur_type', type=str, default=None, help="V, QFix, QIn. V maps state/goal tuples to cost-to-go. "
                                                                    "QFix maps state/goal tuples to q_values for a fixed action space. "
                                                                    "QIn maps state/goal/action tuples to q_value (can be used in arbitrary action spaces).")

    parser.add_argument('--policy', type=str, default=None, help="Policy neural network and arguments. If None then a policy that randomly samples actions "
                                                                 "with equal probability is used.")
    parser.add_argument('--policy_file', type=str, default=None, help="File that has policy nnet. Can be None if using random policy.")
    parser.add_argument('--policy_samp', type=int, default=10, help="Number of actions to sample.")
    parser.add_argument('--policy_rand', type=int, default=0, help="Number of random actions to sample.")

    parser.add_argument('--pathfind', type=str, required=True, help="Pathfinding algorithm and arguments.")
    parser.add_argument('--file', type=str, required=True, help="File containing problem instances to solve")

    parser.add_argument('--time_limit', type=float, default=-1.0, help="A time limit for search. Default is -1, which means infinite.")

    parser.add_argument('--results', type=str, required=True, help="Directory to save results. Saves results after every instance.")
    parser.add_argument('--start_idx', type=int, default=0, help="Index of instance at which to start. Useful for debugging.")
    parser.add_argument('--nnet_batch_size', type=int, default=None, help="Maximum number of inputs to give to any nnet at a time during search. "
                                                                          "Lower if running out of memory. None means no limit.")

    parser.add_argument('--redo', action='store_true', default=False, help="Set to redo already completed instances")
    parser.add_argument('--verbose', action='store_true', default=False, help="Set for verbose")
    parser.add_argument('--debug', action='store_true', default=False, help="Set when debugging with breakpoints")
    parser.set_defaults(func=solve_cli)
```
