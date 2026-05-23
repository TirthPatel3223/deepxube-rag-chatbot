---
id: "func:deepxube.base.trainer.Train.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.base.trainer.Train.__init__"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 210
line_end: 265
class: "Train"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "nnet"
    annotation: "NNet"
    default: null
  - name: "updater"
    annotation: "Up"
    default: null
  - name: "to_main_q"
    annotation: "Queue"
    default: null
  - name: "from_main_qs"
    annotation: "List[Queue]"
    default: null
  - name: "nnet_file"
    annotation: "str"
    default: null
  - name: "nnet_targ_file"
    annotation: "str"
    default: null
  - name: "status_file"
    annotation: "str"
    default: null
  - name: "train_summary_file"
    annotation: "str"
    default: null
  - name: "device"
    annotation: "torch.device"
    default: null
  - name: "on_gpu"
    annotation: "bool"
    default: null
  - name: "writer"
    annotation: "SummaryWriter"
    default: null
  - name: "train_args"
    annotation: "TrainArgs"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "os.path.isfile"
    call_sites: [228, 238, 246, 250]
  - target: "func:pickle.load"
    expr: "pickle.load"
    call_sites: [229, 239]
  - target: null
    expr: "open"
    call_sites: [229, 234, 239, 243]
  - target: null
    expr: "print"
    call_sites: [230]
  - target: "func:deepxube.base.trainer.Status"
    expr: "Status"
    call_sites: [232]
  - target: "func:pickle.dump"
    expr: "pickle.dump"
    call_sites: [234, 243]
  - target: "func:deepxube.base.trainer.TrainSummary"
    expr: "TrainSummary"
    call_sites: [241]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [247, 256]
  - target: "func:deepxube.nnet.nnet_utils.load_nnet"
    expr: "nnet_utils.load_nnet"
    call_sites: [247]
  - target: "func:torch.save"
    expr: "torch.save"
    call_sites: [249, 251]
  - target: null
    expr: "self.nnet.state_dict"
    call_sites: [249, 251]
  - target: null
    expr: "self.nnet.get_optimizer"
    call_sites: [252]
  - target: null
    expr: "self.nnet.to"
    call_sites: [254]
  - target: "func:deepxube.base.trainer.Train.data_parallel"
    expr: "self.data_parallel"
    call_sites: [255]
  - target: "func:torch.nn.DataParallel"
    expr: "nn.DataParallel"
    call_sites: [256]
  - target: "func:deepxube.base.trainer.Train._get_shapes_dtypes"
    expr: "self._get_shapes_dtypes"
    call_sites: [259]
  - target: "func:deepxube.base.trainer.DataBuffer"
    expr: "DataBuffer"
    call_sites: [262]
  - target: null
    expr: "self.updater.up_args.get_up_gen_itrs"
    call_sites: [262]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [265]
raises: []
reads_attrs:
  - "self.db"
  - "self.device"
  - "self.from_main_qs"
  - "self.nnet"
  - "self.nnet_file"
  - "self.nnet_targ_file"
  - "self.on_gpu"
  - "self.optimizer"
  - "self.status"
  - "self.status_file"
  - "self.to_main_q"
  - "self.train_args"
  - "self.train_start_time"
  - "self.train_summary"
  - "self.train_summary_file"
  - "self.updater"
  - "self.writer"
writes_attrs:
  - "self.db"
  - "self.device"
  - "self.from_main_qs"
  - "self.nnet"
  - "self.nnet_file"
  - "self.nnet_targ_file"
  - "self.on_gpu"
  - "self.optimizer"
  - "self.status"
  - "self.status_file"
  - "self.to_main_q"
  - "self.train_args"
  - "self.train_start_time"
  - "self.train_summary"
  - "self.train_summary_file"
  - "self.updater"
  - "self.writer"
---

# `deepxube.base.trainer.Train.__init__`

**File:** [deepxube/base/trainer.py:210](../../../../deepxube/base/trainer.py#L210)
**Class:** `Train`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, nnet: NNet, updater: Up, to_main_q: Queue, from_main_qs: List[Queue], nnet_file: str, nnet_targ_file: str, status_file: str, train_summary_file: str, device: torch.device, on_gpu: bool, writer: SummaryWriter, train_args: TrainArgs) -> None
```

## Docstring

Wire up updater + queues, load (or save initial) status / summary /
nnet checkpoints, build optimiser and ``DataBuffer``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `nnet` | `NNet` | — |
| `updater` | `Up` | — |
| `to_main_q` | `Queue` | — |
| `from_main_qs` | `List[Queue]` | — |
| `nnet_file` | `str` | — |
| `nnet_targ_file` | `str` | — |
| `status_file` | `str` | — |
| `train_summary_file` | `str` | — |
| `device` | `torch.device` | — |
| `on_gpu` | `bool` | — |
| `writer` | `SummaryWriter` | — |
| `train_args` | `TrainArgs` | — |

## Returns

`None`

## Calls

- `pickle.load` → `func:pickle.load` (lines: 229, 239)
- `Status` → `func:deepxube.base.trainer.Status` (lines: 232)
- `pickle.dump` → `func:pickle.dump` (lines: 234, 243)
- `TrainSummary` → `func:deepxube.base.trainer.TrainSummary` (lines: 241)
- `cast` → `func:typing.cast` (lines: 247, 256)
- `nnet_utils.load_nnet` → `func:deepxube.nnet.nnet_utils.load_nnet` (lines: 247)
- `torch.save` → `func:torch.save` (lines: 249, 251)
- `self.data_parallel` → `func:deepxube.base.trainer.Train.data_parallel` (lines: 255)
- `nn.DataParallel` → `func:torch.nn.DataParallel` (lines: 256)
- `self._get_shapes_dtypes` → `func:deepxube.base.trainer.Train._get_shapes_dtypes` (lines: 259)
- `DataBuffer` → `func:deepxube.base.trainer.DataBuffer` (lines: 262)
- `time.time` → `func:time.time` (lines: 265)

### Unresolved
- `os.path.isfile` (lines: 228, 238, 246, 250)
- `open` (lines: 229, 234, 239, 243)
- `print` (lines: 230)
- `self.nnet.state_dict` (lines: 249, 251)
- `self.nnet.get_optimizer` (lines: 252)
- `self.nnet.to` (lines: 254)
- `self.updater.up_args.get_up_gen_itrs` (lines: 262)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.db`
- `self.device`
- `self.from_main_qs`
- `self.nnet`
- `self.nnet_file`
- `self.nnet_targ_file`
- `self.on_gpu`
- `self.optimizer`
- `self.status`
- `self.status_file`
- `self.to_main_q`
- `self.train_args`
- `self.train_start_time`
- `self.train_summary`
- `self.train_summary_file`
- `self.updater`
- `self.writer`

**Reads:**
- `self.db`
- `self.device`
- `self.from_main_qs`
- `self.nnet`
- `self.nnet_file`
- `self.nnet_targ_file`
- `self.on_gpu`
- `self.optimizer`
- `self.status`
- `self.status_file`
- `self.to_main_q`
- `self.train_args`
- `self.train_start_time`
- `self.train_summary`
- `self.train_summary_file`
- `self.updater`
- `self.writer`

## Source

```python
    def __init__(self, nnet: NNet, updater: Up, to_main_q: Queue, from_main_qs: List[Queue], nnet_file: str, nnet_targ_file: str, status_file: str,
                 train_summary_file: str, device: torch.device, on_gpu: bool, writer: SummaryWriter, train_args: TrainArgs) -> None:
        """ Wire up updater + queues, load (or save initial) status / summary /
        nnet checkpoints, build optimiser and ``DataBuffer``. """
        self.updater: Up = updater
        self.to_main_q: Queue = to_main_q
        self.from_main_qs: List[Queue] = from_main_qs
        self.nnet: NNet = nnet
        self.nnet_file = nnet_file
        self.nnet_targ_file: str = nnet_targ_file
        self.writer: SummaryWriter = writer
        self.train_args: TrainArgs = train_args
        self.device: torch.device = device
        self.on_gpu: bool = on_gpu

        # load status
        self.status_file: str = status_file
        self.status: Status
        if os.path.isfile(self.status_file):
            self.status = pickle.load(open(self.status_file, "rb"))
            print(f"Loaded with itr: {self.status.itr}, update_num: {self.status.update_num}, targ_update_num: {self.status.targ_update_num}")
        else:
            self.status = Status(self.updater.up_args.step_max, train_args.balance_steps)
            # noinspection PyTypeChecker
            pickle.dump(self.status, open(self.status_file, "wb"), protocol=-1)

        self.train_summary_file: str = train_summary_file
        self.train_summary: TrainSummary
        if os.path.isfile(self.train_summary_file):
            self.train_summary = pickle.load(open(self.train_summary_file, "rb"))
        else:
            self.train_summary = TrainSummary()
            # noinspection PyTypeChecker
            pickle.dump(self.status, open(self.status_file, "wb"), protocol=-1)

        # load nnet
        if os.path.isfile(self.nnet_file):
            self.nnet = cast(NNet, nnet_utils.load_nnet(self.nnet_file, self.nnet))
        else:
            torch.save(self.nnet.state_dict(), self.nnet_file)
        if not os.path.isfile(self.nnet_targ_file):
            torch.save(self.nnet.state_dict(), self.nnet_targ_file)
        self.optimizer: Optimizer = self.nnet.get_optimizer()

        self.nnet.to(self.device)
        if self.data_parallel():
            self.nnet = cast(NNet, nn.DataParallel(self.nnet))

        # init data buffer
        shapes_dtypes: List[Tuple[Tuple[int, ...], np.dtype]] = self._get_shapes_dtypes()
        db_shapes: List[Tuple[int, ...]] = [x[0] for x in shapes_dtypes]
        db_dtypes: List[np.dtype] = [x[1] for x in shapes_dtypes]
        self.db: DataBuffer = DataBuffer(self.train_args.batch_size * self.updater.up_args.get_up_gen_itrs(), db_shapes, db_dtypes)

        # optimizer and criterion
        self.train_start_time = time.time()
```
