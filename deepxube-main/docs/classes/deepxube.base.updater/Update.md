---
id: "class:deepxube.base.updater.Update"
kind: "class"
name: "Update"
qualified_name: "deepxube.base.updater.Update"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 105
line_end: 517
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters:
  - "D"
  - "FNs"
  - "P"
  - "Inst"
bases:
  - name: "Generic[D, FNs, P, Inst]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.updater.Update.domain_type"
  - "func:deepxube.base.updater.Update.functions_type"
  - "func:deepxube.base.updater.Update.pathfind_type"
  - "func:deepxube.base.updater.Update._update_perf"
  - "func:deepxube.base.updater.Update.__init__"
  - "func:deepxube.base.updater.Update.set_nnet_par_info_l_dict"
  - "func:deepxube.base.updater.Update.start_nnet_runners"
  - "func:deepxube.base.updater.Update.set_nnet_par_info"
  - "func:deepxube.base.updater.Update.clear_nnet_fn_dict"
  - "func:deepxube.base.updater.Update.add_nnet_par"
  - "func:deepxube.base.updater.Update.set_nnet_file"
  - "func:deepxube.base.updater.Update.set_main_qs"
  - "func:deepxube.base.updater.Update.start_procs"
  - "func:deepxube.base.updater.Update.start_update"
  - "func:deepxube.base.updater.Update.get_update_data"
  - "func:deepxube.base.updater.Update.end_update"
  - "func:deepxube.base.updater.Update.stop_procs"
  - "func:deepxube.base.updater.Update.initialize_fns"
  - "func:deepxube.base.updater.Update.get_pathfind"
  - "func:deepxube.base.updater.Update.set_targ_update_num"
  - "func:deepxube.base.updater.Update.update_runner"
  - "func:deepxube.base.updater.Update._add_instances"
  - "func:deepxube.base.updater.Update._step"
  - "func:deepxube.base.updater.Update._step_sync_main"
  - "func:deepxube.base.updater.Update._get_pathfind_functions"
  - "func:deepxube.base.updater.Update._get_instance_data"
  - "func:deepxube.base.updater.Update._get_instance_data_norb"
  - "func:deepxube.base.updater.Update._get_instance_data_rb"
  - "func:deepxube.base.updater.Update._make_instances"
  - "func:deepxube.base.updater.Update._init_replay_buffer"
  - "func:deepxube.base.updater.Update.__repr__"
attributes:
  - name: "self.domain"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.from_main_q"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.from_main_qs"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.from_q"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_file_dict"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_fn_dict"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_par_dict"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_par_info_dict"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_par_info_l_dict"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_par_info_main"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_runner_proc_l_dict"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.num_generated"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.pathfind_arg"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.pathfind_kwargs"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.pathfind_name"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.procs"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.q_id"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.targ_update_nums"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.to_main_q"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.to_q"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.up_args"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.updater.Update`

**File:** [deepxube/base/updater.py:105](../../../deepxube/base/updater.py#L105)
**Abstract:** yes
**Generic parameters:** `D, FNs, P, Inst`

## Docstring

Abstract training-data updater. Owns the domain, pathfinder, worker
processes, and shared queues used to produce training batches. 

## Inheritance

**Direct bases:**
- `Generic[D, FNs, P, Inst]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `domain_type` *(trivial, skipped)*
- `functions_type` *(trivial, skipped)*
- `pathfind_type` *(trivial, skipped)*
- `_update_perf`
- `__init__`
- `set_nnet_par_info_l_dict`
- `start_nnet_runners`
- `set_nnet_par_info`
- `clear_nnet_fn_dict` *(trivial, skipped)*
- `add_nnet_par` *(trivial, skipped)*
- `set_nnet_file` *(trivial, skipped)*
- `set_main_qs`
- `start_procs`
- `start_update`
- `get_update_data`
- `end_update`
- `stop_procs`
- `initialize_fns`
- `get_pathfind`
- `set_targ_update_num` *(trivial, skipped)*
- `update_runner`
- `_add_instances`
- `_step` *(trivial, skipped)*
- `_step_sync_main` *(trivial, skipped)*
- `_get_pathfind_functions` *(trivial, skipped)*
- `_get_instance_data`
- `_get_instance_data_norb` *(trivial, skipped)*
- `_get_instance_data_rb` *(trivial, skipped)*
- `_make_instances` *(trivial, skipped)*
- `_init_replay_buffer` *(trivial, skipped)*
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.domain` | — | __init__ |
| `self.from_main_q` | — | __init__ |
| `self.from_main_qs` | — | __init__ |
| `self.from_q` | — | __init__ |
| `self.nnet_file_dict` | — | __init__ |
| `self.nnet_fn_dict` | — | __init__ |
| `self.nnet_par_dict` | — | __init__ |
| `self.nnet_par_info_dict` | — | __init__ |
| `self.nnet_par_info_l_dict` | — | __init__ |
| `self.nnet_par_info_main` | — | __init__ |
| `self.nnet_runner_proc_l_dict` | — | __init__ |
| `self.num_generated` | — | __init__ |
| `self.pathfind_arg` | — | __init__ |
| `self.pathfind_kwargs` | — | __init__ |
| `self.pathfind_name` | — | __init__ |
| `self.procs` | — | __init__ |
| `self.q_id` | — | __init__ |
| `self.targ_update_nums` | — | __init__ |
| `self.to_main_q` | — | __init__ |
| `self.to_q` | — | __init__ |
| `self.up_args` | — | __init__ |

## Source

```python
class Update(Generic[D, FNs, P, Inst], ABC):
    """ Abstract training-data updater. Owns the domain, pathfinder, worker
    processes, and shared queues used to produce training batches. """

    @staticmethod
    @abstractmethod
    def domain_type() -> Type[D]:
        """ :return: Minimum domain type this updater supports. """
        pass

    @staticmethod
    @abstractmethod
    def functions_type() -> Type[FNs]:
        """ :return: The ``FNs*`` bundle class the pathfinder expects. """
        pass

    @staticmethod
    @abstractmethod
    def pathfind_type() -> Type[P]:
        """ :return: The ``PathFind`` subclass this updater drives. """
        pass

    @staticmethod
    def _update_perf(insts: List[Inst], step_to_pathperf: Dict[int, PathFindPerf]) -> None:
        """ Per-step performance bookkeeping: fold each instance's stats into the map keyed by its step count. """
        for inst in insts:
            step_num_inst: int = int(inst.inst_info[0])
            if step_num_inst not in step_to_pathperf.keys():
                step_to_pathperf[step_num_inst] = PathFindPerf()
            step_to_pathperf[step_num_inst].update_perf(inst)

    def __init__(self, domain: D, pathfind_arg: str, up_args: UpArgs):
        """ Store the domain, parse the pathfinding argument, and register
        every NNet supplied by ``domain.get_nnet_pars``. """
        self.domain: D = domain
        self.pathfind_arg: str = pathfind_arg
        pathfind_name, pathfind_kwargs = get_pathfind_name_kwargs(pathfind_arg)
        self.pathfind_name: str = pathfind_name
        self.pathfind_kwargs: Dict[str, Any] = pathfind_kwargs
        self.up_args: UpArgs = up_args
        self.targ_update_nums: Dict[str, int] = dict()
        self.nnet_par_dict: Dict[str, NNetPar] = dict()
        self.nnet_file_dict: Dict[str, str] = dict()
        for nnet_name, nnet_file, nnet_par in domain.get_nnet_pars():
            self.add_nnet_par(nnet_name, nnet_par)
            self.set_nnet_file(nnet_name, nnet_file)
        self.nnet_par_info_dict: Dict[str, NNetParInfo] = dict()
        self.nnet_fn_dict: Dict[str, NNetCallable] = dict()

        # update info
        self.nnet_par_info_l_dict: Dict[str, List[NNetParInfo]] = dict()
        self.nnet_runner_proc_l_dict: Dict[str, List[BaseProcess]] = dict()
        self.procs: List[BaseProcess] = []
        self.to_q: Optional[Queue] = None
        self.from_q: Optional[Queue] = None
        self.num_generated: int = 0
        self.to_main_q: Optional[Queue] = None
        self.from_main_q: Optional[Queue] = None
        self.from_main_qs: List[Queue] = []
        self.q_id: int = 0
        self.nnet_par_info_main: Optional[NNetParInfo] = None

    def set_nnet_par_info_l_dict(self) -> None:
        """ Build the list of per-worker NNet queue triples for every registered NNet. """
        for nnet_name in self.nnet_par_dict.keys():
            self.nnet_par_info_l_dict[nnet_name] = get_nnet_par_infos(self.up_args.procs)

    def start_nnet_runners(self, device: torch.device, on_gpu: bool) -> None:
        """ Spawn one NNet runner process per worker for every registered NNet. """
        for nnet_name, nnet_par in self.nnet_par_dict.items():
            nnet_file: str = self.nnet_file_dict[nnet_name]
            nnet_par_infos: List[NNetParInfo] = self.nnet_par_info_l_dict[nnet_name]
            self.nnet_runner_proc_l_dict[nnet_name] = start_nnet_fn_runners(nnet_par.get_nnet, nnet_par_infos,
                                                                            nnet_file, device, on_gpu,
                                                                            batch_size=self.up_args.nnet_batch_size)

    def set_nnet_par_info(self, nnet_name: str, nnet_par_info: NNetParInfo) -> None:
        """ Assign a single worker's NNet queue triple for ``nnet_name``. """
        assert nnet_name in self.nnet_par_dict.keys(), f"{nnet_name} not in dict"
        assert nnet_name in self.nnet_file_dict.keys(), f"{nnet_name} not in dict"
        assert nnet_name not in self.nnet_par_info_dict.keys(), f"{nnet_name} already in dict"
        self.nnet_par_info_dict[nnet_name] = nnet_par_info

    def clear_nnet_fn_dict(self) -> None:
        """ Forget all cached NNet callables (they are rebuilt on the next update). """
        self.nnet_fn_dict = dict()

    def add_nnet_par(self, nnet_name: str, nnet_par: NNetPar) -> None:
        """ Register a new NNet parameter object under ``nnet_name``. """
        assert nnet_name not in self.nnet_par_dict.keys(), f"{nnet_name} already in dict"
        self.nnet_par_dict[nnet_name] = nnet_par

    def set_nnet_file(self, nnet_name: str, nnet_file: str) -> None:
        """ Record the checkpoint path for a previously-registered NNet. """
        assert nnet_name in self.nnet_par_dict.keys(), f"{nnet_name} should already be in dict, but it is not"
        self.nnet_file_dict[nnet_name] = nnet_file

    def set_main_qs(self, to_main_q: Queue, from_main_q: Queue, q_id: int) -> None:
        """ Wire this updater to the main-process inference queues (used when ``sync_main``). """
        self.to_main_q = to_main_q
        self.from_main_q = from_main_q
        self.q_id = q_id
        self.nnet_par_info_main = NNetParInfo(self.to_main_q, self.from_main_q, self.q_id)

    def start_procs(self, rb_size: int) -> Tuple[Queue, List[Queue]]:
        """ Spawn worker processes, assign queue triples, and return the main-side queues. """
        # start updater procs
        # TODO implement safer copy?
        updaters: List[Update] = [copy.deepcopy(self) for _ in range(self.up_args.procs)]

        # parallel heuristic functions
        ctx = get_context("spawn")
        to_main_q: Queue = ctx.Queue()
        self.from_main_qs = []
        self.set_nnet_par_info_l_dict()
        for proc_idx, updater in enumerate(updaters):
            from_main_q: Queue = ctx.Queue(1)
            self.from_main_qs.append(from_main_q)
            updater.set_main_qs(to_main_q, from_main_q, proc_idx)
            for nnet_name in self.nnet_par_info_l_dict.keys():
                updater.set_nnet_par_info(nnet_name, self.nnet_par_info_l_dict[nnet_name][proc_idx])

        # get rb sizes
        rb_sizes_q: List[int] = [0] * len(updaters)
        if rb_size > 0:
            rb_sizes_q = split_evenly(rb_size, len(updaters))
            assert min(rb_sizes_q) > 0, "Number of processes must not exceed that of the size of the replay buffer"

        # start procs
        self.to_q = ctx.Queue()
        self.from_q = ctx.Queue()
        self.procs = []
        for updater, rb_size in zip(updaters, rb_sizes_q):
            proc: BaseProcess = ctx.Process(target=updater.update_runner, args=(self.to_q, self.from_q, rb_size))
            proc.daemon = True
            proc.start()
            self.procs.append(proc)

        return to_main_q, self.from_main_qs

    def start_update(self, step_probs: List[int], num_gen: int, train_batch_size: int,
                     device: torch.device, on_gpu: bool) -> None:
        """ Kick off one round of data generation: start NNet runners, send
        step-distribution + target-update nums to each worker, and enqueue
        the per-worker batch counts. """
        # start parallel nnet runners
        self.start_nnet_runners(device, on_gpu)

        # put update data
        for proc_idx, from_main_q in enumerate(self.from_main_qs):
            from_main_q.put((step_probs, self.targ_update_nums.copy()))

        # put work information on to_q
        assert self.to_q is not None

        num_searches: int = num_gen // self.up_args.search_itrs
        if self.up_args.v:
            print(f"Generating {format(num_gen, ',')} training instances with {format(num_searches, ',')} searches")

        assert num_gen % self.up_args.search_itrs == 0, (f"Number of instances to generate per for this updater {num_gen} is not divisible by the max number "
                                                         f"of pathfinding iterations to take during the updater ({self.up_args.search_itrs})")
        up_batch_size: int = train_batch_size if (self.up_args.up_batch_size is None) else self.up_args.up_batch_size
        num_to_send_per: List[int] = split_evenly_w_max(num_searches, self.up_args.procs,
                                                        min(up_batch_size, train_batch_size))
        for num_to_send_per_i in num_to_send_per:
            if num_to_send_per_i > 0:
                self.to_q.put(num_to_send_per_i)

    def get_update_data(self, nowait: bool = False) -> List[List[NDArray]]:
        """ Fetch one batch of training arrays from a worker via ``from_q``
        (blocking unless ``nowait=True``), copy out of shared memory, and
        free the shared blocks. """
        assert self.from_q is not None
        data_l: List[List[NDArray]] = []
        data_get_l: Optional[List[List[SharedNDArray]]]
        if nowait:
            data_get_l = get_nowait_noerr(self.from_q)
        else:
            data_get_l = self.from_q.get()
        if data_get_l is None:
            return []

        for data_get in data_get_l:
            # to np
            data_get_np: List[NDArray] = []
            for data_get_i in data_get:
                data_get_np.append(data_get_i.array.copy())
            data_l.append(data_get_np)

            # status tracking
            self.num_generated += data_get_np[0].shape[0]

            # unlink shared mem
            for arr_shm in data_get:
                arr_shm.close()
                arr_shm.unlink()

        return data_l

    def end_update(self) -> Dict[int, PathFindPerf]:
        """ Send stop signals to workers, collect their time/performance
        summaries, stop the NNet runners, and return the merged per-step
        performance map. """
        assert (self.to_q is not None) and (self.from_q is not None)
        # sending stop signal
        for _ in self.procs:
            self.to_q.put(None)

        # get summary from processes
        step_to_pathperf: Dict[int, PathFindPerf] = dict()
        times_up: Times = Times()
        for _ in self.procs:
            times_up_i, step_to_pathperf_i = self.from_q.get()
            times_up.add_times(times_up_i)
            for step_num_perf, pathperf in step_to_pathperf_i.items():
                if step_num_perf not in step_to_pathperf.keys():
                    step_to_pathperf[step_num_perf] = PathFindPerf()
                step_to_pathperf[step_num_perf] = step_to_pathperf[step_num_perf].comb_perf(pathperf)

        # print
        print(f"Times - {times_up.get_time_str()}")
        if self.up_args.v:
            print(f"Generated {format(self.num_generated, ',')} training instances")
            print_pathfindperf(step_to_pathperf)

        # clean up clean up everybody do your share
        for nnet_name, nnet_par_infos in self.nnet_par_info_l_dict.items():
            nnet_procs: List[BaseProcess] = self.nnet_runner_proc_l_dict[nnet_name]
            stop_nnet_runners(nnet_procs, nnet_par_infos)

        self.num_generated = 0
        self.nnet_runner_proc_l_dict = dict()

        return step_to_pathperf

    def stop_procs(self) -> None:
        """ Send ``None`` to every worker's main queue and join all worker processes. """
        # sending stop signal
        for from_main_q in self.from_main_qs:
            from_main_q.put(None)

        # clean up clean up everybody do your share
        for proc in self.procs:
            proc.join()

        self.procs = []
        self.to_q = None
        self.from_q = None

    def initialize_fns(self) -> None:
        """ Build concrete NNet callables for every registered NNet and bind them to the domain. """
        for nnet_name in self.nnet_par_dict.keys():
            nnet: NNetPar = self.nnet_par_dict[nnet_name]
            nnet_par_info: NNetParInfo = self.nnet_par_info_dict[nnet_name]
            targ_update_num: Optional[int] = self.targ_update_nums.get(nnet_name)
            self.nnet_fn_dict[nnet_name] = nnet.get_nnet_par_fn(nnet_par_info, targ_update_num)
        self.domain.set_nnet_fns(self.nnet_fn_dict)

    def get_pathfind(self) -> P:
        """ Build a fresh pathfinder with this updater's domain and current function bundle. """
        pathfind_kwargs: Dict[str, Any] = self.pathfind_kwargs.copy()
        pathfind_kwargs["domain"] = self.domain
        pathfind_kwargs["functions"] = self._get_pathfind_functions()
        return cast(P, pathfinding_factory.build_class(self.pathfind_name, pathfind_kwargs))

    def set_targ_update_num(self, nnet_name: str, targ_update_num: int) -> None:
        """ Record the target-network iteration number for ``nnet_name`` (used by the NNet runner). """
        self.targ_update_nums[nnet_name] = targ_update_num

    def update_runner(self, to_q: Queue, from_q: Queue, rb_size: int) -> None:
        """ Worker entry point. Runs the generation loop until ``None`` is
        received on ``from_main_q``: for each batch, add instances, step
        the pathfinder, harvest finished-instance data, and push it back. """
        if self.up_args.sync_main:
            assert rb_size > 0, "must use a replay buffer if doing sync_main"
        self._init_replay_buffer(rb_size)

        while True:
            assert self.from_main_q is not None
            data_q: Optional[Tuple[List[int], Dict[str, int]]] = self.from_main_q.get()
            if data_q is None:
                break
            times: Times = Times()

            step_probs, targ_update_nums = data_q
            for nnet_name, targ_update_num in targ_update_nums.items():
                self.set_targ_update_num(nnet_name, targ_update_num)
            self.initialize_fns()

            step_to_pathperf: Dict[int, PathFindPerf] = dict()
            while True:
                batch_size = to_q.get()
                if batch_size is None:
                    break

                pathfind: P = self.get_pathfind()
                # self._set_pathfind_nnet_fns(pathfind)

                insts_rem_last_itr: List[Inst] = []
                put_from_q: List[List[NDArray]] = []
                for _ in range(self.up_args.search_itrs):
                    # add instances
                    self._add_instances(pathfind, insts_rem_last_itr, batch_size, step_probs, times)
                    assert len(pathfind.instances) == batch_size, f"Values were {len(pathfind.instances)} and {batch_size}"

                    # step
                    if self.up_args.sync_main:
                        data: List[NDArray] = self._step_sync_main(pathfind, times)
                        _put_from_q([data], from_q, times)
                    else:
                        self._step(pathfind, times)

                    # remove instances
                    insts_rem_last_itr = pathfind.remove_finished_instances(self.up_args.search_itrs)
                    if len(insts_rem_last_itr) > 0:
                        put_from_q.append(self._get_instance_data(insts_rem_last_itr, rb_size, times))

                    # performance
                    start_time = time.time()
                    self._update_perf(insts_rem_last_itr, step_to_pathperf)
                    times.record_time("update_perf", time.time() - start_time)

                if not self.up_args.sync_main:
                    if len(pathfind.instances) > 0:
                        put_from_q.append(self._get_instance_data(pathfind.instances, rb_size, times))
                    _put_from_q(put_from_q, from_q, times)

                times.add_times(pathfind.times, path=["pathfinding"])

                start_time = time.time()
                del insts_rem_last_itr
                del put_from_q
                del pathfind
                gc.collect()
                times.record_time("gc", time.time() - start_time)

            from_q.put((times, step_to_pathperf))
            self.clear_nnet_fn_dict()
        self.to_main_q = None
        self.from_main_q = None
        self.nnet_par_info_main = None

    def _add_instances(self, pathfind: P, insts_rem: List[Inst], batch_size: int, step_probs: List[int],
                       times: Times) -> None:
        """ Top up the pathfinder with new instances. Reuses step counts from
        finished instances (``insts_rem``) when available, otherwise samples
        step counts from ``step_probs``. """
        if (len(pathfind.instances) == 0) or (len(insts_rem) > 0):
            # get steps generate
            start_time = time.time()
            steps_gen: List[int]
            if len(insts_rem) > 0:
                steps_gen = [int(inst.inst_info[0]) for inst in insts_rem]
            else:
                steps_gen = np.random.choice(self.up_args.step_max + 1, size=batch_size, p=np.array(step_probs)).tolist()
            times.record_time("steps_gen", time.time() - start_time)

            # get instance information and kwargs
            start_time = time.time()
            inst_infos: List[Tuple[int]] = [(step_gen,) for step_gen in steps_gen]
            times.record_time("inst_info", time.time() - start_time)

            instances: List[Inst] = self._make_instances(pathfind, steps_gen, inst_infos, times)

            # add instances
            start_time = time.time()
            pathfind.add_instances(instances)
            times.record_time("inst_add", time.time() - start_time)

    @abstractmethod
    def _step(self, pathfind: P, times: Times) -> None:
        """ Advance the pathfinder by one step (no return value). """
        pass

    @abstractmethod
    def _step_sync_main(self, pathfind: P, times: Times) -> List[NDArray]:
        """ Single-step variant used when ``sync_main`` is enabled; returns one immediate training batch. """
        pass

    @abstractmethod
    def _get_pathfind_functions(self) -> FNs:
        """ Build the ``FNs*`` bundle expected by this updater's pathfinder. """
        pass

    def _get_instance_data(self, instances: List[Inst], rb_size: int, times: Times) -> List[NDArray]:
        """ Dispatch to ``_get_instance_data_norb`` or ``_get_instance_data_rb`` based on ``rb_size``. """
        if rb_size == 0:
            return self._get_instance_data_norb(instances, times)
        else:
            return self._get_instance_data_rb(instances, times)

    @abstractmethod
    def _get_instance_data_norb(self, instances: List[Inst], times: Times) -> List[NDArray]:
        """ Build a training batch directly from finished instances (no replay buffer). """
        pass

    @abstractmethod
    def _get_instance_data_rb(self, instances: List[Inst], times: Times) -> List[NDArray]:
        """ Push finished instances to the replay buffer, then sample a training batch from it. """
        pass

    @abstractmethod
    def _make_instances(self, pathfind: P, steps_gen: List[int], inst_infos: List[Any], times: Times) -> List[Inst]:
        """ Construct fresh pathfinder instances for the given per-instance step counts. """
        pass

    @abstractmethod
    def _init_replay_buffer(self, max_size: int) -> None:
        """ Initialise (or replace) this updater's replay buffer. """
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.up_args.__repr__()})"
```
