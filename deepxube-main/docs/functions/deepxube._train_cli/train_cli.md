---
id: "func:deepxube._train_cli.train_cli"
kind: "function"
name: "train_cli"
qualified_name: "deepxube._train_cli.train_cli"
module: "deepxube._train_cli"
file: "deepxube/_train_cli.py"
line_start: 90
line_end: 128
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
  - target: "func:deepxube.utils.command_line_utils.get_domain_from_arg"
    expr: "get_domain_from_arg"
    call_sites: [93]
  - target: "func:deepxube.base.updater.UpArgs"
    expr: "UpArgs"
    call_sites: [96]
  - target: "func:deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg"
    expr: "get_heur_nnet_par_from_arg"
    call_sites: [106]
  - target: "func:deepxube.factories.updater_factory.get_updater"
    expr: "get_updater"
    call_sites: [107, 112]
  - target: null
    expr: "isinstance"
    call_sites: [108, 113]
  - target: "func:deepxube.utils.command_line_utils.get_policy_nnet_par_from_arg"
    expr: "get_policy_nnet_par_from_arg"
    call_sites: [111]
  - target: "func:deepxube.base.trainer.TrainArgs"
    expr: "TrainArgs"
    call_sites: [117]
  - target: "func:pickle.load"
    expr: "pickle.load"
    call_sites: [123]
  - target: null
    expr: "open"
    call_sites: [123]
  - target: "func:deepxube.trainers.utils.train_loop.TestArgs"
    expr: "TestArgs"
    call_sites: [126]
  - target: null
    expr: "args.t_pathfinds.split"
    call_sites: [126]
  - target: "func:deepxube.trainers.utils.train_loop.train"
    expr: "train"
    call_sites: [128]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._train_cli.train_cli`

**File:** [deepxube/_train_cli.py:90](../../../../deepxube/_train_cli.py#L90)
**Visibility:** public
**Kind:** function

## Signature

```python
def train_cli(args: argparse.Namespace) -> None
```

## Docstring

Parse domain, nnet, and updater arguments from ``args`` and start the training loop. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `args` | `argparse.Namespace` | — |

## Returns

`None`

## Calls

- `get_domain_from_arg` → `func:deepxube.utils.command_line_utils.get_domain_from_arg` (lines: 93)
- `UpArgs` → `func:deepxube.base.updater.UpArgs` (lines: 96)
- `get_heur_nnet_par_from_arg` → `func:deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg` (lines: 106)
- `get_updater` → `func:deepxube.factories.updater_factory.get_updater` (lines: 107, 112)
- `get_policy_nnet_par_from_arg` → `func:deepxube.utils.command_line_utils.get_policy_nnet_par_from_arg` (lines: 111)
- `TrainArgs` → `func:deepxube.base.trainer.TrainArgs` (lines: 117)
- `pickle.load` → `func:pickle.load` (lines: 123)
- `TestArgs` → `func:deepxube.trainers.utils.train_loop.TestArgs` (lines: 126)
- `train` → `func:deepxube.trainers.utils.train_loop.train` (lines: 128)

### Unresolved
- `isinstance` (lines: 108, 113)
- `open` (lines: 123)
- `args.t_pathfinds.split` (lines: 126)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def train_cli(args: argparse.Namespace) -> None:
    """ Parse domain, nnet, and updater arguments from ``args`` and start the training loop. """
    # parse domain and heur_nnet
    domain, domain_name = get_domain_from_arg(args.domain)

    # update args
    up_args: UpArgs = UpArgs(args.procs, args.up_itrs, args.step_max, args.search_itrs, ub_heur_solns=False, backup=args.backup,
                             policy_rand_prob=args.policy_rand_p, up_gen_itrs=args.up_gen_itrs, up_batch_size=args.up_batch_size,
                             nnet_batch_size=args.up_nnet_batch_size, sync_main=args.sync_main, v=args.up_v)

    # parse nnets
    heur_nnet_par: Optional[HeurNNetPar] = None
    update_heur: Optional[UpdateHeur] = None
    policy_nnet_par: Optional[PolicyNNetPar] = None
    update_policy: Optional[UpdatePolicy] = None
    if args.heur is not None:
        heur_nnet_par = get_heur_nnet_par_from_arg(domain, domain_name, args.heur, args.heur_type)[0]
        update_ret: Update = get_updater(domain, args.pathfind, up_args, args.her, "heur")
        assert isinstance(update_ret, UpdateHeur)
        update_heur = update_ret
    if args.policy is not None:
        policy_nnet_par = get_policy_nnet_par_from_arg(domain, domain_name, args.policy, args.policy_samp, args.policy_rand)[0]
        update_ret = get_updater(domain, args.pathfind, up_args, args.her, "policy")
        assert isinstance(update_ret, UpdatePolicy)
        update_policy = update_ret

    # train args
    train_args: TrainArgs = TrainArgs(args.batch_size, args.max_itrs, args.bal, rb=args.rb, loss_thresh=args.up_lt, skip_heur=args.skip_heur,
                                      skip_policy=args.skip_policy, display=args.display)

    # test args
    test_args: Optional[TestArgs] = None
    if args.t_file is not None:
        data = pickle.load(open(args.t_file, "rb"))
        states: List[State] = data['states']
        goals: List[Goal] = data['goals']
        test_args = TestArgs(states, goals, args.t_search_itrs, args.t_pathfinds.split(","), args.up_nnet_batch_size, args.t_up_freq, args.t_init)

    train(domain, heur_nnet_par, update_heur, policy_nnet_par, update_policy, args.dir, train_args, test_args=test_args, debug=args.debug)
```
