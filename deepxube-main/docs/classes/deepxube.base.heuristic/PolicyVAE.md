---
id: "class:deepxube.base.heuristic.PolicyVAE"
kind: "class"
name: "PolicyVAE"
qualified_name: "deepxube.base.heuristic.PolicyVAE"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 128
line_end: 196
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PolicyNNet[PNNetIn]"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.PolicyVAE.__init__"
  - "func:deepxube.base.heuristic.PolicyVAE.forward"
  - "func:deepxube.base.heuristic.PolicyVAE.train_fprop"
  - "func:deepxube.base.heuristic.PolicyVAE.latent_shape"
  - "func:deepxube.base.heuristic.PolicyVAE.encode"
  - "func:deepxube.base.heuristic.PolicyVAE.decode"
  - "func:deepxube.base.heuristic.PolicyVAE._compute_recon_loss"
  - "func:deepxube.base.heuristic.PolicyVAE.__repr__"
attributes:
  - name: "self.kl_weight"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.mse_criterion"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.norm_dist"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.PolicyVAE`

**File:** [deepxube/base/heuristic.py:128](../../../deepxube/base/heuristic.py#L128)
**Abstract:** yes

## Docstring

Conditional VAE policy: encodes (state, goal, action) into a Normal latent
and decodes back to actions. Loss = reconstruction MSE + KL × ``kl_weight``. 

## Inheritance

**Direct bases:**
- `PolicyNNet[PNNetIn]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `forward`
- `train_fprop`
- `latent_shape` *(trivial, skipped)*
- `encode` *(trivial, skipped)*
- `decode` *(trivial, skipped)*
- `_compute_recon_loss`
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.kl_weight` | — | __init__ |
| `self.mse_criterion` | — | __init__ |
| `self.norm_dist` | — | __init__ |

## Source

```python
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
```
