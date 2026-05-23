""" Abstract heuristic and policy network base classes plus their parallelisable
``*Par`` wrappers.

A ``HeurNNet`` (V- or Q-type) outputs cost-to-go scalars; a ``PolicyNNet``
outputs sampled action distributions. The ``*Par`` classes pair an NNet
parameter object with the per-state numpy conversion (``to_np``) and produce
either an in-process callable or one routed through a worker queue. """

from abc import abstractmethod, ABC
from typing import List, Any, TypeVar, Generic, cast, Tuple, Optional, Type, Protocol, runtime_checkable, Union

import numpy as np
from numpy.typing import NDArray

from deepxube.base.domain import Domain, State, Goal, Action
from deepxube.base.nnet_input import NNetInput, PolicyNNetIn
from deepxube.nnet.nnet_utils import NNetParInfo, nnet_batched, NNetPar, get_nnet_par_out
from deepxube.utils import misc_utils

import torch
from torch import nn, Tensor
import torch.optim as optim
from torch.optim.optimizer import Optimizer

import random


In = TypeVar('In', bound=NNetInput)


class DeepXubeNNet(nn.Module, Generic[In], ABC):
    """ Common base for heuristic and policy networks. Holds the ``NNetInput``,
    declares the LR schedule, and asserts type compatibility on construction. """

    @staticmethod
    @abstractmethod
    def nnet_input_type() -> Type[In]:
        """ :return: The ``NNetInput`` subclass this network expects. """
        pass

    def __init__(self, nnet_input: In):
        """ Bind the ``NNetInput`` and initialise default learning-rate parameters. """
        super().__init__()
        assert isinstance(nnet_input, self.nnet_input_type()), f"NNetInput {nnet_input} must be an instance of {self.nnet_input_type()}."
        self.nnet_input: In = nnet_input
        self.lr: float = 0.001
        self.lr_d: float = 0.9999993

    @abstractmethod
    def forward(self, inputs: List[Tensor]) -> List[Tensor]:
        """ Standard PyTorch forward pass over the per-input tensor list. """
        pass

    def get_optimizer(self) -> Optimizer:
        """ :return: Default Adam optimiser at lr=0.001. """
        return optim.Adam(self.parameters(), lr=0.001)

    def update_optimizer(self, optimizer: Optimizer, train_itr: int) -> None:
        """ Apply geometric LR decay ``lr * lr_d ** train_itr`` to every param group. """
        lr_itr: float = self.lr * (self.lr_d ** train_itr)
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr_itr


# neural networks

class HeurNNet(DeepXubeNNet[In]):
    """ Heuristic network. With ``q_fix=True``, the last input tensor is treated
    as action indices and only those columns of the output are returned. """

    def __init__(self, nnet_input: In, out_dim: int, q_fix: bool, **kwargs: Any):
        """ Store output dimension and fixed-Q flag.

        :param out_dim: Number of network outputs (1 for V; ``num_acts`` for fixed Q).
        :param q_fix: If True, the network returns one output per fixed action and
            ``forward`` indexes the requested columns.
        """
        super().__init__(nnet_input)
        self.out_dim: int = out_dim
        self.q_fix: bool = q_fix

    def forward(self, inputs: List[Tensor]) -> List[Tensor]:
        """ Run the body and, if ``q_fix``, gather only the requested action columns. """
        if self.q_fix:
            action_idxs: Tensor = inputs[-1].long()
            x: Tensor = self._forward(inputs[:-1])
            return [torch.gather(x, 1, action_idxs)]
        else:
            return [self._forward(inputs)]

    @abstractmethod
    def _forward(self, inputs: List[Tensor]) -> Tensor:
        """ Subclass forward body returning a single output tensor. """
        pass


PNNetIn = TypeVar('PNNetIn', bound=PolicyNNetIn)


class PolicyNNet(DeepXubeNNet[PNNetIn], ABC):
    """ Policy network base. ``forward`` produces sampled actions plus their density;
    ``train_fprop`` produces the loss given (state, goal, action) triples. """

    @abstractmethod
    def forward(self, states_goals: List[Tensor]) -> List[Tensor]:
        """ Condition on states and goals to sample actions

        :param states_goals:
        :return: List of tensors representing actions with the last Tensor representing the probability density of actions
        """
        pass

    @abstractmethod
    def train_fprop(self, states_goals_actions: List[Tensor]) -> Tuple[Tensor, str]:
        """

        :param states_goals_actions:
        :return: loss, info to print
        """
        pass


def _flatten_list(data_l: List[Tensor]) -> Tensor:
    """ Concatenate every tensor in ``data_l`` into a single flat tensor. """
    return torch.cat([torch.flatten(data_i) for data_i in data_l])


class PolicyVAE(PolicyNNet[PNNetIn]):
    """ Conditional VAE policy: encodes (state, goal, action) into a Normal latent
    and decodes back to actions. Loss = reconstruction MSE + KL × ``kl_weight``. """

    def __init__(self, nnet_input: PNNetIn, kl_weight: float, **kwargs: Any):
        """ Store the KL weight and a unit-normal prior. """
        super().__init__(nnet_input)
        self.norm_dist = torch.distributions.Normal(0, 1)
        self.kl_weight: float = kl_weight
        self.mse_criterion = nn.MSELoss()

    def forward(self, states_goals: List[Tensor]) -> List[Tensor]:
        """ Sample a latent from the prior and decode it into actions + log-prob. """
        z: Tensor = self.norm_dist.sample((states_goals[0].shape[0],) + self.latent_shape()).to(states_goals[0].device)
        recons: List[Tensor] = self.decode(states_goals, z)
        return recons + [self.norm_dist.log_prob(z).sum(dim=1, keepdim=True)]

    def train_fprop(self, states_goals_actions: List[Tensor]) -> Tuple[Tensor, str]:
        """ Encode → KL + reparameterised decode → MSE reconstruction; returns total loss + log string. """
        split_idx: int = self.nnet_input.states_goals_actions_split_idx()
        states_goals: List[Tensor] = states_goals_actions[:split_idx]
        actions: List[Tensor] = states_goals_actions[split_idx:]

        actions_proc, mu, logvar = self.encode(states_goals, actions)
        sum_dims: Tuple[int, ...] = tuple(range(1, len(mu.shape)))
        loss_kl: Tensor = torch.mean(-0.5 * torch.sum(1 + logvar - mu ** 2 - logvar.exp(), dim=sum_dims), dim=0)

        sigma = torch.exp(logvar / 2.0)
        z = mu + sigma * self.norm_dist.sample(mu.shape).to(mu.device)
        actions_recon: List[Tensor] = self.decode(states_goals, z)

        loss_recon: Tensor = self._compute_recon_loss(actions_proc, actions_recon)
        loss: Tensor = loss_recon + (self.kl_weight * loss_kl)

        print_str: str = f"loss_recon: {loss_recon.item():.2E}, loss_kl: {loss_kl.item():.2E}"
        return loss, print_str

    @abstractmethod
    def latent_shape(self) -> Tuple[int, ...]:
        """ :return: Shape of the per-sample latent vector (excluding batch dim). """
        pass

    @abstractmethod
    def encode(self, states_goals: List[Tensor], actions: List[Tensor]) -> Tuple[List[Tensor], Tensor, Tensor]:
        """ Conditon on states and goals and map actions to mu and logvar

        :param states_goals:
        :param actions:
        :return: processed input actions, mu, and logvar
        """

    @abstractmethod
    def decode(self, states_goals: List[Tensor], z: Tensor) -> List[Tensor]:
        """ Conditon on states and goals and map sampled latent to reconstructed actions

        :param states_goals:
        :param z: Latent state
        :return:
        """

    def _compute_recon_loss(self, action_proc: List[Tensor], actions_recon: List[Tensor]) -> Tensor:
        """ MSE between flattened processed-input actions and reconstructed actions. """
        actions_proc_flat: Tensor = _flatten_list(action_proc)
        actions_recon_flat: Tensor = _flatten_list(actions_recon)
        loss_recon: Tensor = self.mse_criterion(actions_proc_flat, actions_recon_flat)
        return loss_recon

    def __repr__(self) -> str:
        return f"{super().__repr__()}\nKL Weight: {self.kl_weight}"


# functions

@runtime_checkable
class HeurFnV(Protocol):
    """ Callable protocol for V-type heuristic functions: ``(states, goals) -> [ctg]``. """

    def __call__(self, states: List[State], goals: List[Goal]) -> List[float]:
        """ Return one cost-to-go per (state, goal) pair. """
        ...


@runtime_checkable
class HeurFnQ(Protocol):
    """ Callable protocol for Q-type heuristic functions: ``(states, goals, actions_l) -> [[q_per_action]]``. """

    def __call__(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
        """ Return per-(state, goal) Q-values, one per action in the corresponding ``actions_l[i]``. """
        ...


HeurFn = Union[HeurFnV, HeurFnQ]


@runtime_checkable
class PolicyFn(Protocol):
    """ Callable protocol for policy functions: maps states/goals to sampled actions and their pdfs. """

    def __call__(self, domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
        """ Map states and goals to sampled actions along with their probability (or log probability) densities

        """
        ...


# parallelizable functions

H = TypeVar('H', bound=HeurFn)


class HeurNNetPar(NNetPar[H]):
    """ Parallelisable wrapper for a heuristic network: pairs the network's
    construction recipe with a per-state numpy converter so callables can be
    handed to worker processes. """

    @abstractmethod
    def get_nnet(self) -> HeurNNet:
        """ :return: A freshly-constructed heuristic network. """
        pass

    @abstractmethod
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> H:
        """ :return: An in-process callable that runs ``nnet`` on (state, goal[, actions]) lists. """
        pass

    @abstractmethod
    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> H:
        """ :return: A callable that routes inference through the worker queue triple. """
        pass


class HeurNNetParV(HeurNNetPar[HeurFnV]):
    """ V-type heuristic ``Par``: scalar cost-to-go output, clamped non-negative. """

    @staticmethod
    def _get_output(heurs: NDArray[np.float64], update_num: Optional[int]) -> List[float]:
        """ Clamp to non-negative; on ``update_num == 0`` return all zeros (warmup). """
        heurs = np.maximum(heurs[:, 0], 0)
        if (update_num is not None) and (update_num == 0):
            heurs = heurs * 0
        return cast(List[float], heurs.astype(np.float64).tolist())

    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device,
                    update_num: Optional[int]) -> HeurFnV:
        """ Build an in-process V-heuristic callable that batches through ``nnet``. """
        nnet.eval()

        def heuristic_fn(states: List[State], goals: List[Goal]) -> List[float]:
            inputs_nnet: List[NDArray] = self.to_np(states, goals)
            heurs: NDArray[np.float64] = nnet_batched(nnet, inputs_nnet, batch_size, device)[0]

            return self._get_output(heurs, update_num)
        return heuristic_fn

    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnV:
        """ Build a V-heuristic callable that delegates to a worker NNet runner. """
        def heuristic_fn(states: List[State], goals: List[Goal]) -> List[float]:
            inputs_nnet: List[NDArray] = self.to_np(states, goals)
            heurs: NDArray[np.float64] = get_nnet_par_out(inputs_nnet, nnet_par_info)[0]

            return self._get_output(heurs, update_num)

        return heuristic_fn

    @abstractmethod
    def to_np(self, states: List[State], goals: List[Goal]) -> List[NDArray[Any]]:
        """ Convert state/goal lists into per-tensor numpy inputs. """
        pass


class HeurNNetParQ(HeurNNetPar[HeurFnQ]):
    """ Q-type heuristic ``Par`` base; concrete subclasses are the fixed-output and action-input variants. """

    @abstractmethod
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> HeurFnQ:
        """ :return: In-process Q-heuristic callable. """
        pass

    @abstractmethod
    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnQ:
        """ :return: Worker-routed Q-heuristic callable. """
        pass

    @abstractmethod
    def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]:
        """ Convert (state, goal, per-state action list) into numpy inputs. """
        pass


class HeurNNetParQFixOut(HeurNNetParQ, ABC):
    """ DQN with a fixed output shape

    """
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> HeurFnQ:
        """ In-process callable that runs the fixed-output Q network and slices per-state outputs. """
        nnet.eval()

        def heuristic_fn(states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
            inputs_nnet: List[NDArray] = self._get_input(states, goals, actions_l)
            q_vals_np: NDArray[np.float64] = nnet_batched(nnet, inputs_nnet, batch_size, device)[0]
            return self._get_output(states, q_vals_np, update_num)

        return heuristic_fn

    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnQ:
        """ Worker-queue-routed variant of ``get_nnet_fn``. """
        def heuristic_fn(states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
            inputs_nnet: List[NDArray] = self._get_input(states, goals, actions_l)
            q_vals_np: NDArray[np.float64] = get_nnet_par_out(inputs_nnet, nnet_par_info)[0]
            return self._get_output(states, q_vals_np, update_num)

        return heuristic_fn

    def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]:
        """ Validate equal action counts then delegate to ``_to_np_fixed_acts``. """
        self._check_same_num_acts(actions_l)
        return self._to_np_fixed_acts(states, goals, actions_l)

    @abstractmethod
    def _to_np_fixed_acts(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]:
        """ Subclass hook: build numpy inputs given equal-length per-state action lists. """
        pass

    def _get_input(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray]:
        """ Prepare numpy inputs for the network (delegates to ``to_np``). """
        inputs_nnet: List[NDArray] = self.to_np(states, goals, actions_l)
        return inputs_nnet

    @staticmethod
    def _get_output(states: List[State], q_vals_np: NDArray[np.float64], update_num: Optional[int]) -> List[List[float]]:
        """ Clamp Q-values non-negative; zero on ``update_num == 0``; split into per-state lists. """
        assert q_vals_np.shape[0] == len(states)
        q_vals_np = np.maximum(q_vals_np, 0)
        if (update_num is not None) and (update_num == 0):
            q_vals_np = q_vals_np * 0
        q_vals_l: List[List[float]] = [q_vals_np[state_idx].astype(np.float64).tolist() for state_idx in
                                       range(len(states))]
        return q_vals_l

    @staticmethod
    def _check_same_num_acts(actions_l: List[List[Action]]) -> None:
        """ Assert every per-state action list has the same length. """
        assert len(set(len(actions) for actions in actions_l)) == 1, "num actions should be the same for all instances"


class HeurNNetParQIn(HeurNNetParQ, ABC):
    """ DQN that takes a single action as input

    """
    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device,
                    update_num: Optional[int]) -> HeurFnQ:
        """ In-process callable that flattens per-state actions, runs the action-input Q network, and unflattens the result. """
        nnet.eval()

        def heuristic_fn(states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
            inputs_nnet, states_rep, split_idxs = self._get_input(states, goals, actions_l)
            q_vals_np: NDArray = nnet_batched(nnet, inputs_nnet, batch_size, device)[0]
            return self._get_output(states_rep, q_vals_np, split_idxs, update_num)

        return heuristic_fn

    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> HeurFnQ:
        """ Worker-queue-routed variant of ``get_nnet_fn``. """
        def heuristic_fn(states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[List[float]]:
            inputs_nnet, states_rep, split_idxs = self._get_input(states, goals, actions_l)
            q_vals_np: NDArray = get_nnet_par_out(inputs_nnet, nnet_par_info)[0]
            return self._get_output(states_rep, q_vals_np, split_idxs, update_num)

        return heuristic_fn

    def to_np(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> List[NDArray[Any]]:
        """ Assert one action per state, then delegate to ``_to_np_one_act``. """
        assert all((len(actions) == 1) for actions in actions_l), "there should only be one action per state/goal pair"
        actions_one: List[Action] = [actions[0] for actions in actions_l]
        return self._to_np_one_act(states, goals, actions_one)

    @abstractmethod
    def _to_np_one_act(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray[Any]]:
        """ Subclass hook: build numpy inputs for one action per (state, goal). """
        pass

    def _get_input(self, states: List[State], goals: List[Goal], actions_l: List[List[Action]]) -> Tuple[List[NDArray], List[State], List[int]]:
        """ Flatten per-state actions, replicate states/goals to match, and produce numpy inputs + split indices. """
        actions_flat, split_idxs = misc_utils.flatten(actions_l)
        states_rep: List[State] = []
        goals_rep: List[Goal] = []
        for state, goal, actions in zip(states, goals, actions_l, strict=True):
            states_rep.extend([state] * len(actions))
            goals_rep.extend([goal] * len(actions))
        inputs_nnet: List[NDArray] = self._to_np_one_act(states_rep, goals_rep, actions_flat)

        return inputs_nnet, states_rep, split_idxs

    @staticmethod
    def _get_output(states_rep: List[State], q_vals_np: NDArray[np.float64], split_idxs: List[int], update_num: Optional[int]) -> List[List[float]]:
        """ Clamp non-negative, zero on warmup, then unflatten back into per-state Q-value lists. """
        assert q_vals_np.shape[0] == len(states_rep)
        q_vals_np = np.maximum(q_vals_np[:, 0], 0)
        if (update_num is not None) and (update_num == 0):
            q_vals_np = q_vals_np * 0

        q_vals_flat: List[float] = q_vals_np.astype(np.float64).tolist()
        q_vals_l: List[List[float]] = misc_utils.unflatten(q_vals_flat, split_idxs)
        return q_vals_l


def policy_fn_rand(domain: Domain, states: List[State], num_rand: int) -> Tuple[List[List[Action]], List[List[float]]]:
    """ Sample ``num_rand`` random actions per state from the domain, with uniform pdf. """
    if num_rand == 0:
        return [[] for _ in states], [[] for _ in states]

    states_rep: List[List[State]] = []
    for state in states:
        states_rep.append([state] * num_rand)

    states_rep_flat, split_idxs = misc_utils.flatten(states_rep)

    actions_samp_flat: List[Action] = domain.sample_state_action(states_rep_flat)
    actions_samp_l: List[List[Action]] = misc_utils.unflatten(actions_samp_flat, split_idxs)

    probs_l: List[List[float]] = []
    for actions_samp_i in actions_samp_l:
        probs_l.append([1.0 / len(actions_samp_i)] * len(actions_samp_i))

    return actions_samp_l, probs_l


def _combine_nnet_with_rand(domain: Domain, actions_l: List[List[Action]], pdfs_l: List[List[float]], states: List[State],
                            num_rand: int) -> Tuple[List[List[Action]], List[List[float]]]:
    """ Append ``num_rand`` random actions (with sampled-pdf placeholders) to each per-state action list. """
    actions_rand_l: List[List[Action]] = policy_fn_rand(domain, states, num_rand)[0]

    actions_comb_l: List[List[Action]] = []
    pdfs_comb_l: List[List[float]] = []
    # get nnet actions
    for state_idx in range(len(states)):
        actions_rand_i: List[Action] = actions_rand_l[state_idx]
        actions_comb_l.append(actions_l[state_idx] + actions_rand_i)
        pdfs_i: List[float] = pdfs_l[state_idx]
        pdfs_comb_l.append(pdfs_i + random.choices(pdfs_i, k=len(actions_rand_i)))

    return actions_comb_l, pdfs_comb_l


class PolicyNNetPar(NNetPar[PolicyFn]):
    """ Parallelisable wrapper for a policy network: builds a callable that samples
    ``num_samp`` actions from the network plus ``num_rand`` random actions per state. """

    def __init__(self, num_samp: int, num_rand: int):
        """ Store the sample counts.

        :param num_samp: Number of network-sampled actions per state.
        :param num_rand: Number of random (mode-collapse guard) actions per state.
        """
        self.num_samp: int = num_samp
        self.num_rand: int = num_rand

    def get_nnet_fn(self, nnet: nn.Module, batch_size: Optional[int], device: torch.device, update_num: Optional[int]) -> PolicyFn:
        """ Build an in-process policy callable. On warmup (``update_num == 0``) returns purely random actions. """
        nnet.eval()
        if (update_num is not None) and (update_num == 0):
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                assert len(states) == len(goals)  # to stop PyCharm from complaining
                return policy_fn_rand(domain, states, self.num_samp + self.num_rand)
        else:
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                inputs_nnet_rep: List[NDArray] = self._get_nnet_inputs_rep(states, goals, self.num_samp)
                nnet_out_np: List[NDArray[np.float64]] = nnet_batched(nnet, inputs_nnet_rep, batch_size, device)

                actions_l, pdfs_l = self._np_to_acts_and_pdfs(nnet_out_np[0:-1], nnet_out_np[-1], len(states), self.num_samp)
                return _combine_nnet_with_rand(domain, actions_l, pdfs_l, states, self.num_rand)

        return policy_fn

    def get_nnet_par_fn(self, nnet_par_info: NNetParInfo, update_num: Optional[int]) -> PolicyFn:
        """ Worker-queue-routed variant of ``get_nnet_fn``. """
        if (update_num is not None) and (update_num == 0):
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                assert len(states) == len(goals)  # to stop PyCharm from complaining
                return policy_fn_rand(domain, states, self.num_samp + self.num_rand)
        else:
            def policy_fn(domain: Domain, states: List[State], goals: List[Goal]) -> Tuple[List[List[Action]], List[List[float]]]:
                inputs_nnet_rep: List[NDArray] = self._get_nnet_inputs_rep(states, goals, self.num_samp)
                nnet_out_np: List[NDArray[np.float64]] = get_nnet_par_out(inputs_nnet_rep, nnet_par_info)

                actions_l, pdfs_l = self._np_to_acts_and_pdfs(nnet_out_np[0:-1], nnet_out_np[-1], len(states), self.num_samp)
                return _combine_nnet_with_rand(domain, actions_l, pdfs_l, states, self.num_rand)

        return policy_fn

    @abstractmethod
    def get_nnet(self) -> PolicyNNet:
        """ :return: A freshly-constructed policy network. """
        pass

    @abstractmethod
    def to_np_fn(self, states: List[State], goals: List[Goal]) -> List[NDArray[Any]]:
        """ Inference-side numpy conversion (no actions). """
        pass

    @abstractmethod
    def to_np_train(self, states: List[State], goals: List[Goal], actions: List[Action]) -> List[NDArray[Any]]:
        """ Training-side numpy conversion (target actions included). """
        pass

    @abstractmethod
    def _nnet_out_to_actions(self, nnet_out: List[NDArray[np.float64]]) -> List[Action]:
        """ Decode raw network outputs into ``Action`` objects. """
        pass

    def _get_nnet_inputs_rep(self, states: List[State], goals: List[Goal], num_samp: int) -> List[NDArray]:
        """ Repeat each (state, goal) input row ``num_samp`` times so the network samples multiple actions per state in one batch. """
        inputs_nnet: List[NDArray] = self.to_np_fn(states, goals)
        inputs_nnet_rep_interleave: List[NDArray] = []
        for inputs_nnet_i in inputs_nnet:
            inputs_nnet_rep_interleave.append(np.repeat(inputs_nnet_i, num_samp, axis=0))
        return inputs_nnet_rep_interleave

    def _np_to_acts_and_pdfs(self, actions_np: List[NDArray[np.float64]], pdfs_np: NDArray[np.float64], num_states: int,
                             num_samp: int) -> Tuple[List[List[Action]], List[List[float]]]:
        """ Slice the interleaved (state, sample) outputs back into per-state lists of actions and pdfs. """
        assert len(pdfs_np.shape) == 2
        assert pdfs_np.shape[1] == 1

        actions_l: List[List[Action]] = []
        pdfs_l: List[List[float]] = []
        for state_idx in range(num_states):
            start_idx: int = state_idx * num_samp
            end_idx: int = start_idx + num_samp
            actions_np_state: List[NDArray[np.float64]] = [actions_np_i[start_idx:end_idx] for actions_np_i in actions_np]
            pdfs_state: List[float] = pdfs_np[start_idx:end_idx, 0].tolist()

            actions_l.append(self._nnet_out_to_actions(actions_np_state))
            pdfs_l.append(pdfs_state)

        return actions_l, pdfs_l

    def __repr__(self) -> str:
        return f"{self.get_nnet()}\n#Samp: {self.num_samp}, #Rand Samp: {self.num_rand}"
