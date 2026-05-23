---
id: "func:deepxube.trainers.utils.train_loop.train"
kind: "function"
name: "train"
qualified_name: "deepxube.trainers.utils.train_loop.train"
module: "deepxube.trainers.utils.train_loop"
file: "deepxube/trainers/utils/train_loop.py"
line_start: 82
line_end: 212
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
  - name: "update_heur"
    annotation: "Optional[UpdateHeur]"
    default: null
  - name: "policy_nnet_par"
    annotation: "Optional[PolicyNNetPar]"
    default: null
  - name: "update_policy"
    annotation: "Optional[UpdatePolicy]"
    default: null
  - name: "nnet_dir"
    annotation: "str"
    default: null
  - name: "train_args"
    annotation: "TrainArgs"
    default: null
  - name: "test_args"
    annotation: "Optional[TestArgs]"
    default: "None"
  - name: "debug"
    annotation: "bool"
    default: "False"
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "os.path.exists"
    call_sites: [87]
  - target: "func:os.makedirs"
    expr: "os.makedirs"
    call_sites: [88]
  - target: "func:deepxube.utils.data_utils.Logger"
    expr: "data_utils.Logger"
    call_sites: [93]
  - target: null
    expr: "print"
    call_sites: [96, 102, 136, 144, 152, 153, 155, 156, 158, 212]
  - target: "func:deepxube.nnet.nnet_utils.get_device"
    expr: "nnet_utils.get_device"
    call_sites: [101]
  - target: "func:torch.utils.tensorboard.SummaryWriter"
    expr: "SummaryWriter"
    call_sites: [105]
  - target: null
    expr: "isinstance"
    call_sites: [120, 125, 180, 182, 189, 192]
  - target: null
    expr: "updater.set_heur_nnet"
    call_sites: [121]
  - target: null
    expr: "updater.set_heur_file"
    call_sites: [122]
  - target: null
    expr: "updater.set_policy_nnet"
    call_sites: [126]
  - target: null
    expr: "updater.set_policy_file"
    call_sites: [127]
  - target: null
    expr: "heur_nnet_par.get_nnet"
    call_sites: [135]
  - target: null
    expr: "update_heur.start_procs"
    call_sites: [137]
  - target: "func:deepxube.trainers.train_heur.TrainHeur"
    expr: "TrainHeur"
    call_sites: [138]
  - target: null
    expr: "policy_nnet_par.get_nnet"
    call_sites: [143]
  - target: null
    expr: "update_policy.start_procs"
    call_sites: [145]
  - target: "func:deepxube.trainers.train_policy.TrainPolicy"
    expr: "TrainPolicy"
    call_sites: [146]
  - target: "func:deepxube.trainers.utils.train_loop.get_pathfind"
    expr: "get_pathfind"
    call_sites: [153]
  - target: "func:deepxube.trainers.utils.train_loop.get_curr_itr"
    expr: "get_curr_itr"
    call_sites: [163, 201]
  - target: "func:deepxube.trainers.utils.train_loop.get_curr_update_num"
    expr: "get_curr_update_num"
    call_sites: [168]
  - target: "func:deepxube.trainers.utils.train_loop.test"
    expr: "test"
    call_sites: [176, 205]
  - target: null
    expr: "updater.set_targ_update_num"
    call_sites: [190, 193]
  - target: null
    expr: "updater.heur_name"
    call_sites: [190]
  - target: null
    expr: "updater.policy_name"
    call_sites: [193]
  - target: null
    expr: "train_obj.update_step"
    call_sites: [197]
  - target: null
    expr: "torch.cuda.empty_cache"
    call_sites: [198]
  - target: null
    expr: "updater.stop_procs"
    call_sites: [210]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.trainers.utils.train_loop.train`

**File:** [deepxube/trainers/utils/train_loop.py:82](../../../../deepxube/trainers/utils/train_loop.py#L82)
**Visibility:** public
**Kind:** function

## Signature

```python
def train(domain: Domain, heur_nnet_par: Optional[HeurNNetPar], update_heur: Optional[UpdateHeur], policy_nnet_par: Optional[PolicyNNetPar], update_policy: Optional[UpdatePolicy], nnet_dir: str, train_args: TrainArgs, test_args: Optional[TestArgs] = None, debug: bool = False) -> None
```

## Docstring

Main training loop: initialises trainers, alternates heuristic/policy update steps, periodically evaluates, and
stops worker processes when done. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `heur_nnet_par` | `Optional[HeurNNetPar]` | — |
| `update_heur` | `Optional[UpdateHeur]` | — |
| `policy_nnet_par` | `Optional[PolicyNNetPar]` | — |
| `update_policy` | `Optional[UpdatePolicy]` | — |
| `nnet_dir` | `str` | — |
| `train_args` | `TrainArgs` | — |
| `test_args` | `Optional[TestArgs]` | `None` |
| `debug` | `bool` | `False` |

## Returns

`None`

## Calls

- `os.makedirs` → `func:os.makedirs` (lines: 88)
- `data_utils.Logger` → `func:deepxube.utils.data_utils.Logger` (lines: 93)
- `nnet_utils.get_device` → `func:deepxube.nnet.nnet_utils.get_device` (lines: 101)
- `SummaryWriter` → `func:torch.utils.tensorboard.SummaryWriter` (lines: 105)
- `TrainHeur` → `func:deepxube.trainers.train_heur.TrainHeur` (lines: 138)
- `TrainPolicy` → `func:deepxube.trainers.train_policy.TrainPolicy` (lines: 146)
- `get_pathfind` → `func:deepxube.trainers.utils.train_loop.get_pathfind` (lines: 153)
- `get_curr_itr` → `func:deepxube.trainers.utils.train_loop.get_curr_itr` (lines: 163, 201)
- `get_curr_update_num` → `func:deepxube.trainers.utils.train_loop.get_curr_update_num` (lines: 168)
- `test` → `func:deepxube.trainers.utils.train_loop.test` (lines: 176, 205)

### Unresolved
- `os.path.exists` (lines: 87)
- `print` (lines: 96, 102, 136, 144, 152, 153, 155, 156, 158, 212)
- `isinstance` (lines: 120, 125, 180, 182, 189, 192)
- `updater.set_heur_nnet` (lines: 121)
- `updater.set_heur_file` (lines: 122)
- `updater.set_policy_nnet` (lines: 126)
- `updater.set_policy_file` (lines: 127)
- `heur_nnet_par.get_nnet` (lines: 135)
- `update_heur.start_procs` (lines: 137)
- `policy_nnet_par.get_nnet` (lines: 143)
- `update_policy.start_procs` (lines: 145)
- `updater.set_targ_update_num` (lines: 190, 193)
- `updater.heur_name` (lines: 190)
- `updater.policy_name` (lines: 193)
- `train_obj.update_step` (lines: 197)
- `torch.cuda.empty_cache` (lines: 198)
- `updater.stop_procs` (lines: 210)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def train(domain: Domain, heur_nnet_par: Optional[HeurNNetPar], update_heur: Optional[UpdateHeur], policy_nnet_par: Optional[PolicyNNetPar],
          update_policy: Optional[UpdatePolicy], nnet_dir: str, train_args: TrainArgs, test_args: Optional[TestArgs] = None,
          debug: bool = False) -> None:
    """ Main training loop: initialises trainers, alternates heuristic/policy update steps, periodically evaluates, and
    stops worker processes when done. """
    if not os.path.exists(nnet_dir):
        os.makedirs(nnet_dir)

    # logging
    if not debug:
        output_save_loc = f"{nnet_dir}/output.txt"
        sys.stdout = data_utils.Logger(output_save_loc, "a")

    if 'SLURM_JOB_ID' in os.environ:
        print("SLURM JOB ID: %s" % os.environ['SLURM_JOB_ID'])

    # get device
    on_gpu: bool
    device: torch.device
    device, devices, on_gpu = nnet_utils.get_device()
    print("device: %s, devices: %s, on_gpu: %s" % (device, devices, on_gpu))

    # file info
    writer: SummaryWriter = SummaryWriter(nnet_dir)

    heur_file: str = f"{nnet_dir}/heur.pt"
    heur_targ_file: str = f"{nnet_dir}/heur_targ.pt"
    heur_status_file: str = f"{nnet_dir}/heur_status.pkl"
    heur_train_summ_file: str = f"{nnet_dir}/heur_train_summary.pkl"

    policy_file = f"{nnet_dir}/policy.pt"
    policy_targ_file = f"{nnet_dir}/policy_targ.pt"
    policy_status_file: str = f"{nnet_dir}/policy_status.pkl"
    policy_train_summ_file: str = f"{nnet_dir}/policy_train_summary.pkl"

    # set updater heur info
    if heur_nnet_par is not None:
        for updater in [update_heur, update_policy]:
            if (updater is not None) and isinstance(updater, UpdateHasHeur):
                updater.set_heur_nnet(heur_nnet_par)
                updater.set_heur_file(heur_targ_file)
    if policy_nnet_par is not None:
        for updater in [update_heur, update_policy]:
            if (updater is not None) and isinstance(updater, UpdateHasPolicy):
                updater.set_policy_nnet(policy_nnet_par)
                updater.set_policy_file(policy_targ_file)

    # start_procs and trainers
    train_heur: Optional[TrainHeur] = None
    train_policy: Optional[TrainPolicy] = None
    if heur_nnet_par is not None:
        assert update_heur is not None

        heur_nnet: HeurNNet = heur_nnet_par.get_nnet()
        print(heur_nnet_par)
        to_main_q, from_main_qs = update_heur.start_procs(train_args.rb * train_args.batch_size * update_heur.up_args.up_itrs)
        train_heur = TrainHeur(heur_nnet, update_heur, to_main_q, from_main_qs, heur_file, heur_targ_file, heur_status_file, heur_train_summ_file, device,
                               on_gpu, writer, train_args)
    if policy_nnet_par is not None:
        assert update_policy is not None

        policy_nnet: PolicyNNet = policy_nnet_par.get_nnet()
        print(policy_nnet_par)
        to_main_q, from_main_qs = update_policy.start_procs(train_args.rb * train_args.batch_size * update_policy.up_args.up_itrs)
        train_policy = TrainPolicy(policy_nnet, update_policy, to_main_q, from_main_qs, policy_file, policy_targ_file, policy_status_file,
                                   policy_train_summ_file, device, on_gpu, writer, train_args)

    # print info
    for updater in [update_heur, update_policy]:
        if updater is not None:
            print(f"{updater}")
            print(get_pathfind(domain, heur_nnet_par, train_heur, policy_nnet_par, train_policy, 100, updater.pathfind_arg))

    print(f"{train_args}")
    print(domain)
    if test_args is not None:
        print(f"{test_args}")

    # training
    up_itr_performed: bool = False

    curr_itr: int = get_curr_itr(train_heur, train_policy)
    while curr_itr < train_args.max_itrs:
        # test
        do_test: bool = False
        if test_args is not None:
            update_num: int = get_curr_update_num(train_heur, train_policy)
            if update_num > 0:
                do_test = update_num % test_args.test_up_freq == 0
            elif update_num == 0:
                do_test = test_args.test_init

        if do_test:
            assert test_args is not None
            test(domain, heur_nnet_par, train_heur, policy_nnet_par, train_policy, test_args, writer, curr_itr)

        # train
        for train_obj in [train_heur, train_policy]:
            if isinstance(train_obj, TrainHeur) and train_args.skip_heur:
                continue
            if isinstance(train_obj, TrainPolicy) and train_args.skip_policy:
                continue

            for updater in [update_heur, update_policy]:
                if updater is None:
                    continue
                if train_heur is not None:
                    assert isinstance(updater, UpdateHasHeur)
                    updater.set_targ_update_num(updater.heur_name(), train_heur.status.targ_update_num)
                if train_policy is not None:
                    assert isinstance(updater, UpdateHasPolicy)
                    updater.set_targ_update_num(updater.policy_name(), train_policy.status.targ_update_num)

            if (train_obj is None) or (train_obj.status.itr > curr_itr):
                continue
            train_obj.update_step()
            torch.cuda.empty_cache()

        up_itr_performed = True
        curr_itr = get_curr_itr(train_heur, train_policy)

    # test
    if (test_args is not None) and up_itr_performed:
        test(domain, heur_nnet_par, train_heur, policy_nnet_par, train_policy, test_args, writer, curr_itr)

    # stop procs
    for updater in [update_heur, update_policy]:
        if updater is not None:
            updater.stop_procs()

    print("Done")
```
