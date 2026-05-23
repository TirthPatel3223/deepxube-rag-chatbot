---
id: "class:deepxube.base.trainer.Train"
kind: "class"
name: "Train"
qualified_name: "deepxube.base.trainer.Train"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 200
line_end: 421
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters:
  - "NNet"
  - "Up"
bases:
  - name: "Generic[NNet, Up]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.trainer.Train.data_parallel"
  - "func:deepxube.base.trainer.Train.__init__"
  - "func:deepxube.base.trainer.Train.update_step"
  - "func:deepxube.base.trainer.Train._get_update_data"
  - "func:deepxube.base.trainer.Train._train"
  - "func:deepxube.base.trainer.Train._train_sync_main"
  - "func:deepxube.base.trainer.Train._train_itr"
  - "func:deepxube.base.trainer.Train._end_update"
  - "func:deepxube.base.trainer.Train._add_post_up_info"
  - "func:deepxube.base.trainer.Train._get_shapes_dtypes"
attributes:
  - name: "self.db"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.device"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.from_main_qs"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_file"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_targ_file"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.on_gpu"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.optimizer"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.status"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.status_file"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.to_main_q"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.train_args"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.train_start_time"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.train_summary"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.train_summary_file"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.updater"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.writer"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.trainer.Train`

**File:** [deepxube/base/trainer.py:200](../../../deepxube/base/trainer.py#L200)
**Abstract:** yes
**Generic parameters:** `NNet, Up`

## Docstring

Abstract trainer. Owns network, optimiser, data buffer, and update loop;
subclasses provide the per-iteration loss and the data-buffer shape spec. 

## Inheritance

**Direct bases:**
- `Generic[NNet, Up]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `data_parallel` *(trivial, skipped)*
- `__init__`
- `update_step`
- `_get_update_data`
- `_train`
- `_train_sync_main`
- `_train_itr` *(trivial, skipped)*
- `_end_update`
- `_add_post_up_info` *(trivial, skipped)*
- `_get_shapes_dtypes` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.db` | — | __init__ |
| `self.device` | — | __init__ |
| `self.from_main_qs` | — | __init__ |
| `self.nnet` | — | __init__ |
| `self.nnet_file` | — | __init__ |
| `self.nnet_targ_file` | — | __init__ |
| `self.on_gpu` | — | __init__ |
| `self.optimizer` | — | __init__ |
| `self.status` | — | __init__ |
| `self.status_file` | — | __init__ |
| `self.to_main_q` | — | __init__ |
| `self.train_args` | — | __init__ |
| `self.train_start_time` | — | __init__ |
| `self.train_summary` | — | __init__ |
| `self.train_summary_file` | — | __init__ |
| `self.updater` | — | __init__ |
| `self.writer` | — | __init__ |

## Source

```python
class Train(Generic[NNet, Up], ABC):
    """ Abstract trainer. Owns network, optimiser, data buffer, and update loop;
    subclasses provide the per-iteration loss and the data-buffer shape spec. """

    @staticmethod
    @abstractmethod
    def data_parallel() -> bool:
        """ :return: Whether to wrap the network in ``nn.DataParallel``. """
        pass

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

    def update_step(self) -> None:
        """ One outer iteration: clear data buffer, run the updater, train for ``up_itrs`` steps, save checkpoints, possibly bump the target net. """
        self.db.clear()
        itr_init: int = self.status.itr

        # print info
        start_info_l: List[str] = [f"itr: {self.status.itr}", f"update_num: {self.status.update_num}", f"targ_update: {self.status.targ_update_num}"]

        num_gen: int = self.train_args.batch_size * self.updater.up_args.get_up_gen_itrs()
        start_info_l.append(f"num_gen: {format(num_gen, ',')}")
        if self.train_args.balance_steps:
            start_info_l.append(f"step max (curr): {self.status.step_max_curr}")
        print(f"\nGetting Data - {', '.join(start_info_l)}")
        times: Times = Times()

        # start updater
        start_time = time.time()
        self.updater.start_update(self.status.step_probs.tolist(), num_gen, self.train_args.batch_size, self.device, self.on_gpu)
        times.record_time("up_start", time.time() - start_time)

        # do training
        self.train_start_time = time.time()
        loss: float
        if not self.updater.up_args.sync_main:
            self._get_update_data(num_gen, times)
            self._end_update(itr_init, times)
            loss = self._train(times)
        else:
            loss = self._train_sync_main(num_gen, times)
            self._end_update(itr_init, times)

        # save nnet
        start_time = time.time()
        torch.save(self.nnet.state_dict(), self.nnet_file)
        times.record_time("save_net", time.time() - start_time)

        # update nnet
        update_targ: bool = False
        if loss < self.train_args.loss_thresh:
            update_targ = True

        if update_targ:
            shutil.copy(self.nnet_file, self.nnet_targ_file)
            self.status.targ_update_num = self.status.targ_update_num + 1
        self.status.update_num += 1

        start_time = time.time()
        # noinspection PyTypeChecker
        pickle.dump(self.status, open(self.status_file, "wb"), protocol=-1)
        # noinspection PyTypeChecker
        pickle.dump(self.train_summary, open(self.train_summary_file, "wb"), protocol=-1)
        times.record_time("save_status", time.time() - start_time)
        print(f"Train - itrs: {self.updater.up_args.up_itrs}, loss: {loss:.2E}, targ_updated: {update_targ}")
        print(f"Times - {times.get_time_str()}")

    def _get_update_data(self, num_gen: int, times: Times) -> None:
        """ Drain the updater's output queue into the data buffer until we have ``num_gen`` rows. """
        start_time = time.time()
        while self.db.size() < num_gen:
            data_l: List[List[NDArray]] = self.updater.get_update_data()
            for data in data_l:
                self.db.add(data)
        times.record_time("up_data", time.time() - start_time)

    def _train(self, times: Times) -> float:
        """ Run ``up_itrs`` training iterations against the data buffer; return the last loss. """
        loss: float = np.inf
        first_itr_in_update: bool = True
        for _ in range(self.updater.up_args.up_itrs):
            # sample data
            start_time = time.time()
            batch: List[NDArray] = self.db.sample(self.train_args.batch_size)
            times.record_time("data_samp", time.time() - start_time)

            # train
            loss = self._train_itr(batch, first_itr_in_update, times)
            first_itr_in_update = False
            self.status.itr += 1

        return loss

    def _train_sync_main(self, num_gen: int, times: Times) -> float:
        """ ``sync_main`` variant: interleave training iterations with serving worker NNet inference requests on the main process. """
        loss: float = np.inf
        update_train_itr: int = 0
        first_itr_in_update: bool = True
        while update_train_itr < self.updater.up_args.up_itrs:
            batch: List[NDArray]
            # data from updater should not be more that train_args.batch_size
            start_time = time.time()
            if self.db.size() == num_gen:
                batch = self.db.sample(self.train_args.batch_size)
            else:
                self.nnet.eval()
                while self.db.size() < ((update_train_itr + 1) * self.train_args.batch_size):
                    # get heuristic values for ongoing search
                    q_res: Optional[Tuple[int, List[SharedNDArray]]] = get_nowait_noerr(self.to_main_q)
                    if q_res is not None:
                        proc_id, inputs_np_shm = q_res
                        nnet_in_out_shared_q(self.nnet, inputs_np_shm, self.updater.up_args.nnet_batch_size,
                                             self.device, self.from_main_qs[proc_id])

                    # get update data
                    data_l_i: List[List[NDArray]] = self.updater.get_update_data(nowait=True)
                    for data in data_l_i:
                        self.db.add(data)
                sel_idxs: NDArray = np.arange(update_train_itr * self.train_args.batch_size,
                                              (update_train_itr + 1) * self.train_args.batch_size)
                batch = sel_l(self.db.arrays, sel_idxs)

            times.record_time("up_data", time.time() - start_time)

            # train
            loss = self._train_itr(batch, first_itr_in_update, times)
            update_train_itr += 1
            first_itr_in_update = False
            self.status.itr += 1

        return loss

    @abstractmethod
    def _train_itr(self, batch: List[NDArray], first_itr_in_update: bool, times: Times) -> float:
        """ Subclass hook: run one optimiser step on ``batch`` and return the scalar loss. """
        pass

    def _end_update(self, itr_init: int, times: Times) -> None:
        """ Wrap up the updater round: collect performance, push to TensorBoard, optionally rebalance step probs. """
        start_time = time.time()
        step_to_search_perf: Dict[int, PathFindPerf] = self.updater.end_update()
        self.train_summary.update_pathfindstats(step_to_search_perf, itr_init)
        if self.train_args.balance_steps:
            self.status.update_step_probs(step_to_search_perf)

        per_solved_ave, path_costs_ave, search_itrs_ave = get_eq_weighted_perf(step_to_search_perf)

        self.writer.add_scalar("train/pathfind/solved", per_solved_ave, self.status.itr)
        self.writer.add_scalar("train/pathfind/path_cost", path_costs_ave, self.status.itr)
        self.writer.add_scalar("train/pathfind/search_itrs", search_itrs_ave, self.status.itr)

        post_up_info_l: List[str] = [f"%solved: {per_solved_ave:.2f}", f"path_costs: {path_costs_ave:.3f}",
                                     f"search_itrs: {search_itrs_ave:.3f}"] + self._add_post_up_info()

        print(f"Data - {', '.join(post_up_info_l)}")

        times.record_time("up_end", time.time() - start_time)

    @abstractmethod
    def _add_post_up_info(self) -> List[str]:
        """ Subclass hook: extra strings appended to the per-update info line. """
        pass

    @abstractmethod
    def _get_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        """ Subclass hook: shapes and dtypes for the parallel arrays in ``DataBuffer``. """
        pass
```
