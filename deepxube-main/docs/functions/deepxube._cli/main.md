---
id: "func:deepxube._cli.main"
kind: "function"
name: "main"
qualified_name: "deepxube._cli.main"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 306
line_end: 364
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters: []
returns: "None"
docstring_source: "present"
callees:
  - target: "func:argparse.ArgumentParser"
    expr: "ArgumentParser"
    call_sites: [308]
  - target: null
    expr: "parser.add_subparsers"
    call_sites: [311]
  - target: null
    expr: "subparsers.add_parser"
    call_sites: [314, 321, 325, 334, 339, 344, 349, 354, 359]
  - target: "func:deepxube._cli._parser_domain_info"
    expr: "_parser_domain_info"
    call_sites: [318]
  - target: "func:deepxube._cli._parse_viz_info"
    expr: "_parse_viz_info"
    call_sites: [322]
  - target: "func:deepxube._cli._parser_heur_info"
    expr: "_parser_heur_info"
    call_sites: [331]
  - target: "func:deepxube._cli._parser_pathfind_info"
    expr: "_parser_pathfind_info"
    call_sites: [336]
  - target: "func:deepxube._cli._parse_time"
    expr: "_parse_time"
    call_sites: [341]
  - target: "func:deepxube._train_cli.parser_train"
    expr: "parser_train"
    call_sites: [346]
  - target: "func:deepxube._cli._parse_train_summary"
    expr: "_parse_train_summary"
    call_sites: [351]
  - target: "func:deepxube._cli._parse_problem_instance"
    expr: "_parse_problem_instance"
    call_sites: [356]
  - target: "func:deepxube._solve.parse_solve"
    expr: "parse_solve"
    call_sites: [360]
  - target: null
    expr: "parser.parse_args"
    call_sites: [362]
  - target: null
    expr: "args.func"
    call_sites: [364]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli.main`

**File:** [deepxube/_cli.py:306](../../../../deepxube/_cli.py#L306)
**Visibility:** public
**Kind:** function

## Signature

```python
def main() -> None
```

## Docstring

Parse command-line arguments and dispatch to the selected subcommand function. 

## Parameters

*(No parameters.)*

## Returns

`None`

## Calls

- `ArgumentParser` → `func:argparse.ArgumentParser` (lines: 308)
- `_parser_domain_info` → `func:deepxube._cli._parser_domain_info` (lines: 318)
- `_parse_viz_info` → `func:deepxube._cli._parse_viz_info` (lines: 322)
- `_parser_heur_info` → `func:deepxube._cli._parser_heur_info` (lines: 331)
- `_parser_pathfind_info` → `func:deepxube._cli._parser_pathfind_info` (lines: 336)
- `_parse_time` → `func:deepxube._cli._parse_time` (lines: 341)
- `parser_train` → `func:deepxube._train_cli.parser_train` (lines: 346)
- `_parse_train_summary` → `func:deepxube._cli._parse_train_summary` (lines: 351)
- `_parse_problem_instance` → `func:deepxube._cli._parse_problem_instance` (lines: 356)
- `parse_solve` → `func:deepxube._solve.parse_solve` (lines: 360)

### Unresolved
- `parser.add_subparsers` (lines: 311)
- `subparsers.add_parser` (lines: 314, 321, 325, 334, 339, 344, 349, 354, 359)
- `parser.parse_args` (lines: 362)
- `args.func` (lines: 364)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def main() -> None:
    """ Parse command-line arguments and dispatch to the selected subcommand function. """
    parser = ArgumentParser(prog="deepxube", description="Solve pathfinding problems with deep reinforcement learning "
                                                         "and heuristic search.",
                            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(help="")

    # domain info
    parser_domain_info: ArgumentParser = subparsers.add_parser('domain_info', help="Print information on domains that "
                                                                                   "deepxube has registered. "
                                                                                   "Put user-defined definitions of "
                                                                                   "domains in './domains/'")
    _parser_domain_info(parser_domain_info)

    # visualization
    parser_viz: ArgumentParser = subparsers.add_parser('viz', help="Visualize states/goals")
    _parse_viz_info(parser_viz)

    # heuristic info
    parser_heur_info: ArgumentParser = subparsers.add_parser('heuristic_info', help="Print information on neural network "
                                                                                    "representations of heuristic functions "
                                                                                    "that deepxube has registered. "
                                                                                    "Put user-defined definitions of "
                                                                                    "heuristic neural networks in "
                                                                                    "'./heuristics/'")
    _parser_heur_info(parser_heur_info)

    # pathfinding info
    parser_pathfind_info: ArgumentParser = subparsers.add_parser('pathfinding_info', help="Print information on pathfinding algorithms that deepxube has "
                                                                                          "registered.")
    _parser_pathfind_info(parser_pathfind_info)

    # time functionality
    parser_time: ArgumentParser = subparsers.add_parser('time', help="Time basic functionality.",
                                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    _parse_time(parser_time)

    # train
    parser_tr: ArgumentParser = subparsers.add_parser('train', help="Train a heuristic function.",
                                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser_train(parser_tr)

    # train summary
    parser_tr_summ: ArgumentParser = subparsers.add_parser('train_summary', help="Visualize training information not shown in tensorboard.",
                                                           formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    _parse_train_summary(parser_tr_summ)

    # problem instance generation
    parser_problem_instance: ArgumentParser = subparsers.add_parser('problem_inst', help="Generate problem instances (state/goal pairs) and save to a "
                                                                                         "pickle file.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    _parse_problem_instance(parser_problem_instance)

    # solve
    parser_solve: ArgumentParser = subparsers.add_parser('solve', help="Solve problem instnaces.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parse_solve(parser_solve)

    args = parser.parse_args()

    args.func(args)
```
