---
id: "func:deepxube._train_cli.parser_train"
kind: "function"
name: "parser_train"
qualified_name: "deepxube._train_cli.parser_train"
module: "deepxube._train_cli"
file: "deepxube/_train_cli.py"
line_start: 19
line_end: 87
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
    call_sites: [21, 23, 24, 28, 29, 30, 32, 35, 36, 37, 86]
  - target: null
    expr: "parser.add_argument_group"
    call_sites: [40, 54, 78]
  - target: null
    expr: "train_group.add_argument"
    call_sites: [41, 42, 43, 44, 46, 51]
  - target: null
    expr: "update_group.add_argument"
    call_sites: [55, 56, 57, 58, 59, 60, 62, 64, 67, 68, 71, 74]
  - target: null
    expr: "test_group.add_argument"
    call_sites: [79, 80, 81, 82, 83]
  - target: null
    expr: "parser.set_defaults"
    call_sites: [87]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._train_cli.parser_train`

**File:** [deepxube/_train_cli.py:19](../../../../deepxube/_train_cli.py#L19)
**Visibility:** public
**Kind:** function

## Signature

```python
def parser_train(parser: ArgumentParser) -> None
```

## Docstring

Register all training subcommand arguments and set ``train_cli`` as the handler. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `parser` | `ArgumentParser` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `parser.add_argument` (lines: 21, 23, 24, 28, 29, 30, 32, 35, 36, 37, 86)
- `parser.add_argument_group` (lines: 40, 54, 78)
- `train_group.add_argument` (lines: 41, 42, 43, 44, 46, 51)
- `update_group.add_argument` (lines: 55, 56, 57, 58, 59, 60, 62, 64, 67, 68, 71, 74)
- `test_group.add_argument` (lines: 79, 80, 81, 82, 83)
- `parser.set_defaults` (lines: 87)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def parser_train(parser: ArgumentParser) -> None:
    """ Register all training subcommand arguments and set ``train_cli`` as the handler. """
    parser.add_argument('--domain', type=str, required=True, help="Domain name and arguments.")

    parser.add_argument('--heur', type=str, default=None, help="Heuristic neural network and arguments.")
    parser.add_argument('--heur_type', type=str, default=None, help="V, QFix, QIn. V maps state/goal tuples to cost-to-go. "
                                                                    "QFix maps state/goal tuples to q_values for a fixed action space. "
                                                                    "QIn maps state/goal/action tuples to q_value (can be used in arbitrary action spaces).")

    parser.add_argument('--policy', type=str, default=None, help="Policy neural network and arguments.")
    parser.add_argument('--policy_samp', type=int, default=10, help="Number to actions to sample from policy")
    parser.add_argument('--policy_rand', type=int, default=5, help="Number of random actions to sample")

    parser.add_argument('--pathfind', type=str, required=True, help="Pathfinding algorithm and arguments. Batch size of any pathfinding algorithm should be 1 "
                                                                    "since updater assumes 1 instance is generated per iteration.")

    parser.add_argument('--dir', type=str, required=True, help="Directory to save neural networks.")
    parser.add_argument('--skip_heur', action='store_true', default=False, help="Set to skip training of heuristic function.")
    parser.add_argument('--skip_policy', action='store_true', default=False, help="Set to skip training of policy.")

    # train args
    train_group = parser.add_argument_group('train')
    train_group.add_argument('--batch_size', type=int, default=1000, help="Batch size.")
    train_group.add_argument('--max_itrs', type=int, default=100000, help="Maximum training iterations.")
    train_group.add_argument('--display', type=int, default=0, help="Display frequency for nnet training.")
    train_group.add_argument('--bal', action='store_true', default=False, help="Set to balance of number of steps to take to generate problem instances based "
                                                                               "on percentage of states solved.")
    train_group.add_argument('--rb', type=int, default=0, help="Number of updates worth of data to keep in replay buffer. If 0 then no replay buffer is used "
                                                               "and training waits for update to finish to get data and randomly sample from that data. "
                                                               "No replay buffer results in faster updates due to not having to use a separate network to "
                                                               "compute the update, but is more susceptible to instability due to shifts in the distribution "
                                                               "of states seen during search.")
    train_group.add_argument('--up_lt', type=float, default=np.inf, help="Loss must be below this threshold for update.")

    # updater args
    update_group = parser.add_argument_group('update')
    update_group.add_argument('--procs', type=int, default=1, help="Number of processes to generate update data.")
    update_group.add_argument('--step_max', type=int, required=True, help="Maximum number of steps to take when generating problem instnaces.")
    update_group.add_argument('--up_itrs', type=int, default=100, help="Number of iterations to check for update.")
    update_group.add_argument('--up_gen_itrs', type=int, default=100, help="Number of iterations for which to generate training data per update check.")
    update_group.add_argument('--search_itrs', type=int, default=1000, help="Number of search iterations to take when generating data.")
    update_group.add_argument('--up_batch_size', type=int, default=100, help="Maximum number of problem instances to generate at a time. Lower if running out "
                                                                             "of memory.")
    update_group.add_argument('--up_nnet_batch_size', type=int, default=20000, help="Maximum number of inputs to give to any nnet at a time during update. "
                                                                                    "Lower if running out of memory.")
    update_group.add_argument('--her', action='store_true', default=False, help="If problem instance not solved during search, do hindsight experience replay "
                                                                                "(HER) by relabeling deepest node in search tree as a goal state and "
                                                                                "sampling a goal from it.")
    update_group.add_argument('--sync_main', action='store_true', default=False, help="Use main nnet to search during update.")
    update_group.add_argument('--up_v', action='store_true', default=False, help="Verbose update.")

    # update heur args
    update_group.add_argument('--backup', type=int, default=1, help="1 for Bellman backup, -1 for limited horizon bellman lookahead (LHBL)")

    # update policy args
    update_group.add_argument('--policy_rand_p', type=float, default=0.0, help="Probability of sampling random actions for training policy "
                                                                               "(to prevent mode collapse)")

    # test args
    test_group = parser.add_argument_group('test')
    test_group.add_argument('--t_file', type=str, default=None, help="File to use when testing.")
    test_group.add_argument('--t_search_itrs', type=int, default=100, help="Number of search iterations when testing.")
    test_group.add_argument('--t_up_freq', type=int, default=10, help="Test every t_up_freq updates.")
    test_group.add_argument('--t_pathfinds', type=str, default="bwas", help="Comma separated list of pathfinding algorithms to use when testing.")
    test_group.add_argument('--t_init', action='store_true', default=False, help="Set for testing before training begins.")

    # other
    parser.add_argument('--debug', action='store_true', default=False, help="Set for debug mode.")
    parser.set_defaults(func=train_cli)
```
