""" Abstract base classes for training-data updaters.

An ``Update`` runs the pathfinder for a configured number of iterations,
collects the states/edges expanded along the way, and emits per-iteration
numpy arrays ready to be fed to the heuristic or policy network's training
step. Concrete subclasses in ``deepxube/updaters/`` specialise for supervised
vs. RL, V vs. Q, and with/without Hindsight Experience Replay (HER), and
register themselves with ``updater_factory``.
"""

from typing import List, Dict, Tuple, Any, Generic, TypeVar, Optional, cast, Type
from abc import ABC, abstractmethod
import time
from dataclasses import dataclass
from multiprocessing import Queue
from multiprocessing.process import BaseProcess
from multiprocessing.context import SpawnContext  # noqa

import numpy as np
import torch
from numpy.typing import NDArray

from deepxube.nnet.nnet_utils import NNetParInfo, NNetCallable, NNetPar, get_nnet_par_infos, start_nnet_fn_runners, stop_nnet_runners
from deepxube.base.domain import Domain, State, Action, Goal, GoalSampleableFromState
from deepxube.base.heuristic import HeurNNetPar, HeurNNetParV, HeurNNetParQ, HeurFn, HeurFnV, HeurFnQ, PolicyNNetPar, PolicyFn
from deepxube.base.pathfinding import FNs, FNsP, FNsHV, FNsHQ, FNsHeur, PathFind, PathFindSup, Instance, InstanceNode, InstanceEdge, get_path, Node
from deepxube.factories.pathfinding_factory import pathfinding_factory
from deepxube.pathfinding.utils.performance import PathFindPerf, print_pathfindperf
from deepxube.utils.command_line_utils import get_pathfind_name_kwargs
from deepxube.utils.data_utils import SharedNDArray, np_to_shnd, get_nowait_noerr
from deepxube.utils.misc_utils import split_evenly, split_evenly_w_max
from deepxube.utils.timing_utils import Times
import gc

import copy
from torch.multiprocessing import get_context


FNsH = TypeVar('FNsH', bound=FNsHeur)


# TODO par nnets per GPU?
@dataclass
class UpArgs:
    """ Each time an instance is solved, a new one is created with the same number of steps to maintain training data
    balance.

    :param procs: Number of parallel workers used to compute update
    :param up_itrs: How many iterations worth of training instances to obtain for each update
    :param step_max: Maximum number of steps to take when generating problem instances.
    :param search_itrs: Maximum number of pathfinding iterationos to take for each generated problem instances
    States and corresponding goals seen during search will be added to training instances.
    :param ub_heur_solns: if True, the target cost-to-go will be min(backup, path_cost_from_state)
    :param backup: 1 is Bellman and -1 is tree backup (i.e. Limited Horizon Bellman-based Learning)
    :param policy_rand_prob: Probability of sampling random actions for training policy (to prevent mode collapse)
    :param up_gen_itrs: How many iterations worth of data to generate per udpate. If None, set to up_itrs
    :param up_batch_size: Maximum number of searches to do at a time. Helps manage memory.
    Decrease if memory is running out during updater. None if as large as possible
    :param nnet_batch_size: Batch size of each nnet used for each process updater. Make smaller if running out
    of memory. None if as large as possible.
    :param v: True if update is verbose.
    :param sync_main: if True, number of processes can affect order in which data is seen
    """
    procs: int
    up_itrs: int
    step_max: int
    search_itrs: int
    ub_heur_solns: bool = False
    backup: int = 1
    policy_rand_prob: float = 0.0
    up_gen_itrs: Optional[int] = None
    up_batch_size: Optional[int] = None
    nnet_batch_size: Optional[int] = None
    sync_main: bool = False
    v: bool = False

    def get_up_gen_itrs(self) -> int:
        """ Return ``up_gen_itrs`` if set, else fall back to ``up_itrs``. """
        return self.up_itrs if (self.up_gen_itrs is None) else self.up_gen_itrs


def _put_from_q(data_l: List[List[NDArray]], from_q: Queue, times: Times) -> None:
    """ Copy each ndarray in ``data_l`` into fresh shared memory and push the
    resulting ``SharedNDArray`` handles onto ``from_q`` for the main process. """
    start_time = time.time()

    data_shm_l: List[List[SharedNDArray]] = []
    for data in data_l:
        data_shm_l.append([np_to_shnd(data_i) for data_i in data])

    from_q.put(data_shm_l)

    for data_shm in data_shm_l:
        for arr_shm in data_shm:
            arr_shm.close()

    times.record_time("put", time.time() - start_time)


Inst = TypeVar('Inst', bound=Instance)
D = TypeVar('D', bound=Domain)
P = TypeVar('P', bound=PathFind)


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


class UpdateHER(Update[GoalSampleableFromState, FNs, P, Inst], ABC):
    """ Mixin for updaters that perform Hindsight Experience Replay: failed
    instances have their goals relabelled to an actually-reached state. """

    def _step_sync_main(self, pathfind: P, times: Times) -> List[NDArray]:
        """ Not supported: HER requires post-search goal relabelling. """
        raise NotImplementedError("Cannot train with sync_main if also doing hindsight experience replay (HER) since goal relabeling is done after search is "
                                  "complete.")

    def _get_instance_data_norb(self, instances: List[Inst], times: Times) -> List[NDArray]:
        """ Not supported: HER requires a replay buffer. """
        raise NotImplementedError("Must use replay buffer if doing HER.")

    def _get_her_goals(self, instances: List[Inst], times: Times) -> Tuple[List[Inst], List[Goal]]:
        """ If instance is not finisheed and solved, get deepest states out all nodes that have children + root node for relabeled goal.
            :return: Instances and their corresponding goals (order of instances changes)
        """
        # get states/goals or mark for goal relabelling
        instances_goalkeep: List[Inst] = []
        instances_relabel: List[Inst] = []

        rand_keeps: List[float] = cast(List[float], np.random.uniform(0, 1, size=len(instances)).tolist())
        for instance, rand_keep in zip(instances, rand_keeps):
            if instance.finished() and instance.has_soln():
                instances_goalkeep.append(instance)
            else:
                instances_relabel.append(instance)

        # get goals goalkeep
        goals_goalkeep: List[Goal] = [instance.root_node.goal for instance in instances_goalkeep]

        # get relabeled goals
        goals_relabel: List[Goal] = []
        if len(instances_relabel) > 0:
            # get start states and deepest states
            start_time = time.time()
            states_start: List[State] = []
            states_deepest: List[State] = []
            for instance in instances_relabel:
                states_start.append(instance.root_node.state)

                # get all descendants that have children
                nodes_desc: List[Node] = instance.root_node.get_all_descendants()
                node_desc_w_children: List[Node] = [node_desc for node_desc in nodes_desc if len(node_desc.edge_dict) > 0]

                # get state of deepest node
                state_deepest: State = instance.root_node.state
                deepest_depth: int = 0
                for node in node_desc_w_children:
                    depth: int = len(get_path(node)[0])
                    if depth > deepest_depth:
                        deepest_depth = depth
                        state_deepest = node.state
                states_deepest.append(state_deepest)

            times.record_time("her_node_deepest", time.time() - start_time)

            # relabel
            start_time = time.time()
            goals_relabel = self.domain.sample_goal_from_state(states_start, states_deepest)
            times.record_time("her_relabel", time.time() - start_time)

        return instances_goalkeep + instances_relabel, goals_goalkeep + goals_relabel


HNet = TypeVar('HNet', bound=HeurNNetPar)
H = TypeVar('H', bound=HeurFn)


class UpdateHasHeur(Update[D, FNsH, P, Inst], Generic[D, FNsH, P, Inst, HNet, H], ABC):
    """ Mixin for updaters that own a heuristic NNet under the ``"heur"`` key. """

    @staticmethod
    def heur_name() -> str:
        """ :return: Fixed NNet key for the heuristic network. """
        return 'heur'

    def set_heur_nnet(self, heur_nnet: HNet) -> None:
        """ Register the heuristic NNet parameter object. """
        self.add_nnet_par(self.heur_name(), heur_nnet)

    def set_heur_file(self, heur_file: str) -> None:
        """ Record the heuristic network's checkpoint path. """
        self.set_nnet_file(self.heur_name(), heur_file)

    def get_heur_nnet_par(self) -> HNet:
        """ :return: Registered heuristic NNet parameter object. """
        return cast(HNet, self.nnet_par_dict[self.heur_name()])

    def get_heur_fn(self) -> H:
        """ :return: Current heuristic-function callable. """
        return self._get_heur_fn_from_dict()

    def _get_heur_fn_from_dict(self) -> H:
        """ Fetch the heuristic callable from the NNet-function dict. """
        return cast(H, self.nnet_fn_dict[self.heur_name()])


class UpdateHasPolicy(Update[D, FNsP, P, Inst], ABC):
    """ Mixin for updaters that own a policy NNet under the ``"policy"`` key. """

    @staticmethod
    def policy_name() -> str:
        """ :return: Fixed NNet key for the policy network. """
        return 'policy'

    def set_policy_nnet(self, policy_nnet: PolicyNNetPar) -> None:
        """ Register the policy NNet parameter object. """
        self.add_nnet_par(self.policy_name(), policy_nnet)

    def set_policy_file(self, policy_file: str) -> None:
        """ Record the policy network's checkpoint path. """
        self.set_nnet_file(self.policy_name(), policy_file)

    def get_policy_nnet_par(self) -> PolicyNNetPar:
        """ :return: Registered policy NNet parameter object. """
        return cast(PolicyNNetPar, self.nnet_par_dict[self.policy_name()])

    def get_policy_fn(self) -> PolicyFn:
        """ :return: Current policy-function callable. """
        return self._get_policy_fn_from_dict()

    def _get_policy_fn_from_dict(self) -> PolicyFn:
        """ Fetch the policy callable from the NNet-function dict. """
        return cast(PolicyFn, self.nnet_fn_dict[self.policy_name()])


PS = TypeVar('PS', bound=PathFindSup)


class UpdateSup(Update[D, Any, PS, Inst], ABC):
    """ Supervised updater base: uses a ``PathFindSup`` random-walk pathfinder and no replay buffer. """

    @staticmethod
    def functions_type() -> Type[Any]:
        """ :return: ``Any`` — supervised pathfinders carry no function bundle. """
        return Any

    def _step(self, pathfind: PS, times: Times) -> None:
        """ Advance the supervised pathfinder by one step. """
        pathfind.step()

    def _get_pathfind_functions(self) -> Any:
        """ :return: ``None`` — supervised pathfinders need no functions. """
        return None

    def _make_instances(self, pathfind: PS, steps_gen: List[int], inst_infos: List[Any], times: Times) -> List[Inst]:
        """ Build instances via random walks of the given step counts. """
        return pathfind.make_instances_rw(steps_gen, inst_infos)

    def _step_sync_main(self, pathfind: PS, times: Times) -> List[NDArray]:
        """ Not supported for supervised updaters. """
        raise NotImplementedError("No sync_main option for supervised update")

    def _get_instance_data_rb(self, instances: List[Inst], times: Times) -> List[NDArray]:
        """ Not supported: supervised updaters do not use a replay buffer. """
        raise NotImplementedError("No replay buffer used with supervised update")

    def _init_replay_buffer(self, max_size: int) -> None:
        """ No-op: supervised updaters have no replay buffer. """
        pass


class UpdateRL(Update[D, FNs, P, Inst], ABC):
    """ Reinforcement-learning updater base: builds problem instances by
    sampling start/goal pairs from the domain (not random walks). """

    def _make_instances(self, pathfind: P, steps_gen: List[int], inst_infos: List[Any], times: Times) -> List[Inst]:
        """ Sample start states and goals from the domain, then hand them to the pathfinder. """
        # get states/goals
        times_states: Times = Times()
        states_gen, goals_gen = self.domain.sample_problem_instances(steps_gen, times=times_states)
        times.add_times(times_states, ["get_states"])

        return pathfind.make_instances(states_gen, goals_gen, inst_infos=inst_infos, compute_root_vals=False)


class UpdateHeur(UpdateHasHeur[D, FNsH, P, Inst, HNet, H]):
    """ Updater specialised on training a heuristic network. """

    @abstractmethod
    def get_heur_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        """ :return: Shape/dtype of each training-array slot for this heuristic. """
        pass

    def get_heur_fn(self) -> H:
        """ :return: Heuristic function; routed through the main process when ``sync_main``. """
        if not self.up_args.sync_main:
            return super().get_heur_fn()
        else:
            assert self.nnet_par_info_main is not None
            return cast(H, self.get_heur_nnet_par().get_nnet_par_fn(self.nnet_par_info_main, None))

    def _get_targ_heur_fn(self) -> H:
        """ :return: The target-network heuristic function (from the NNet-fn dict). """
        return self._get_heur_fn_from_dict()


class UpdatePolicy(UpdateHasPolicy[D, FNsP, P, Inst], ABC):
    """ Updater specialised on training a policy network. """

    def get_policy_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        """ :return: Shape/dtype of each training-array slot for the policy. """
        states, goals = self.domain.sample_problem_instances([0])
        actions: List[Action] = self.domain.sample_state_action(states)
        inputs_nnet: List[NDArray[Any]] = self.get_policy_nnet_par().to_np_train(states, goals, actions)

        shapes_dtypes: List[Tuple[Tuple[int, ...], np.dtype]] = []
        for inputs_nnet_i in inputs_nnet:
            shapes_dtypes.append((inputs_nnet_i[0].shape, inputs_nnet_i.dtype))

        return shapes_dtypes

    def get_policy_fn(self) -> PolicyFn:
        """ :return: Policy function. ``sync_main`` is not yet supported. """
        if not self.up_args.sync_main:
            return super().get_policy_fn()
        else:
            raise NotImplementedError("sync_main not yet implemented for policy_fn")


class UpdateHeurV(UpdateHeur[D, FNsHV, P, InstanceNode, HeurNNetParV, HeurFnV], ABC):
    """ Heuristic updater for V-type networks (scalar cost-to-go output). """

    def get_heur_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        """ :return: Input shapes/dtypes plus a scalar float64 target slot. """
        states, goals = self.domain.sample_problem_instances([0])
        inputs_nnet: List[NDArray[Any]] = self.get_heur_nnet_par().to_np(states, goals)

        shapes_dtypes: List[Tuple[Tuple[int, ...], np.dtype]] = []
        for inputs_nnet_i in inputs_nnet:
            shapes_dtypes.append((inputs_nnet_i[0].shape, inputs_nnet_i.dtype))
        shapes_dtypes.append((tuple(), np.dtype(np.float64)))

        return shapes_dtypes


class UpdateHeurQ(UpdateHeur[D, FNsHQ, P, InstanceEdge, HeurNNetParQ, HeurFnQ], ABC):
    """ Heuristic updater for Q-type networks (per-action cost-to-go). """

    def get_heur_train_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        """ :return: Input shapes/dtypes plus a scalar float64 target slot. """
        states, goals = self.domain.sample_problem_instances([0])
        actions: List[Action] = self.domain.sample_state_action(states)
        inputs_nnet: List[NDArray[Any]] = self.get_heur_nnet_par().to_np(states, goals, [[action] for action in actions])

        shapes_dtypes: List[Tuple[Tuple[int, ...], np.dtype]] = []
        for inputs_nnet_i in inputs_nnet:
            shapes_dtypes.append((inputs_nnet_i[0].shape, inputs_nnet_i.dtype))
        shapes_dtypes.append((tuple(), np.dtype(np.float64)))

        return shapes_dtypes
