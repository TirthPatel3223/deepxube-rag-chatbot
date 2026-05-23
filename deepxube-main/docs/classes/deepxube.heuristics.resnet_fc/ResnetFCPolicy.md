---
id: "class:deepxube.heuristics.resnet_fc.ResnetFCPolicy"
kind: "class"
name: "ResnetFCPolicy"
qualified_name: "deepxube.heuristics.resnet_fc.ResnetFCPolicy"
module: "deepxube.heuristics.resnet_fc"
file: "deepxube/heuristics/resnet_fc.py"
line_start: 62
line_end: 124
is_abstract: false
is_dataclass: false
decorators:
  - "@policy_factory.register_class('resnet_fc')"
generic_parameters: []
bases:
  - name: "PolicyVAE[FlatInPolicy]"
    resolved_id: null
methods:
  - "func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.nnet_input_type"
  - "func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.__init__"
  - "func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.latent_shape"
  - "func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.encode"
  - "func:deepxube.heuristics.resnet_fc.ResnetFCPolicy.decode"
attributes:
  - name: "self.decoder"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.enc_dim"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.encoder"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.res_dim"
    annotation: null
    default: null
    from: "__init__"
factory_registrations:
  - factory: "deepxube.factories.heuristic_factory.policy_factory"
    key: "resnet_fc"
docstring_source: "present"
---

# `deepxube.heuristics.resnet_fc.ResnetFCPolicy`

**File:** [deepxube/heuristics/resnet_fc.py:62](../../../deepxube/heuristics/resnet_fc.py#L62)
**Abstract:** no
**Decorators:** `@policy_factory.register_class('resnet_fc')`

## Docstring

FC-ResNet VAE policy: encodes (state, goal, action) to a Gaussian latent, then decodes latent + state/goal to
action logits. 

## Inheritance

**Direct bases:**
- `PolicyVAE[FlatInPolicy]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Factory registration

- Factory `deepxube.factories.heuristic_factory.policy_factory` under key `resnet_fc`

## Methods

- `nnet_input_type` *(trivial, skipped)*
- `__init__`
- `latent_shape` *(trivial, skipped)*
- `encode`
- `decode`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.decoder` | — | __init__ |
| `self.enc_dim` | — | __init__ |
| `self.encoder` | — | __init__ |
| `self.res_dim` | — | __init__ |

## Source

```python
class ResnetFCPolicy(PolicyVAE[FlatInPolicy]):
    """ FC-ResNet VAE policy: encodes (state, goal, action) to a Gaussian latent, then decodes latent + state/goal to
    action logits. """

    @staticmethod
    def nnet_input_type() -> Type[FlatInPolicy]:
        """ :return: ``FlatInPolicy``. """
        return FlatInPolicy

    def __init__(self, nnet_input: FlatInPolicy, kl_weight: float, enc_dim: int = 10, res_dim: int = 1000, num_blocks: int = 4, batch_norm: bool = False,
                 weight_norm: bool = False, group_norm: int = -1, act_fn: str = "RELU"):
        """ Build encoder (state+goal+action → latent) and decoder (state+goal+z → action logits). """
        super().__init__(nnet_input, kl_weight)
        # one hots
        input_dims, one_hot_depths = self.nnet_input.get_input_info()
        input_dims_sg: List[int] = input_dims[:self.nnet_input.states_goals_actions_split_idx()]
        one_hot_depths_sg: List[int] = one_hot_depths[:self.nnet_input.states_goals_actions_split_idx()]
        input_dims_acts: List[int] = input_dims[self.nnet_input.states_goals_actions_split_idx():]
        one_hot_depths_acts: List[int] = one_hot_depths[self.nnet_input.states_goals_actions_split_idx():]

        self.one_hots_sg, input_dim_sg = make_onehots(input_dims_sg, one_hot_depths_sg)
        self.one_hots_acts, input_dim_acts = make_onehots(input_dims_acts, one_hot_depths_acts)
        input_dim_tot: int = input_dim_sg + input_dim_acts

        self.enc_dim: int = enc_dim

        # res net
        self.res_dim: int = res_dim

        def res_block_init() -> nn.Module:
            return FullyConnectedModel(res_dim, [res_dim] * 2, [act_fn, "LINEAR"],
                                       batch_norms=[batch_norm] * 2, weight_norms=[weight_norm] * 2,
                                       group_norms=[group_norm] * 2)

        self.encoder = nn.Sequential(
            nn.Linear(input_dim_tot, res_dim),
            ResnetModel(res_block_init, num_blocks, act_fn),
            nn.Linear(res_dim, self.enc_dim * 2)
        )

        self.decoder = nn.Sequential(
            nn.Linear(input_dim_sg + self.enc_dim, res_dim),
            ResnetModel(res_block_init, num_blocks, act_fn),
            nn.Linear(res_dim, input_dim_acts)
        )

    def latent_shape(self) -> Tuple[int, ...]:
        """ :return: Shape of the latent vector ``(enc_dim,)``. """
        return (self.enc_dim,)

    def encode(self, states_goals: List[Tensor], actions: List[Tensor]) -> Tuple[List[Tensor], Tensor, Tensor]:
        """ :return: Tuple of (one-hot actions, mu, log-var) produced by the VAE encoder. """
        states_goals_oh: List[Tensor] = [one_hot(input_i) for input_i, one_hot in zip(states_goals, self.one_hots_sg)]
        actions_oh: List[Tensor] = [one_hot(input_i) for input_i, one_hot in zip(actions, self.one_hots_acts)]
        mu_logvar: Tensor = self.encoder(torch.cat(states_goals_oh + actions_oh, dim=1))

        return actions_oh, mu_logvar[:, :self.enc_dim], mu_logvar[:, self.enc_dim:]

    def decode(self, states_goals: List[Tensor], z: Tensor) -> List[Tensor]:
        """ :return: Reconstructed action logit tensors decoded from latent ``z`` and the one-hot state/goal. """
        states_goals_oh: List[Tensor] = [one_hot(input_i) for input_i, one_hot in zip(states_goals, self.one_hots_sg)]
        x: Tensor = self.decoder(torch.cat(states_goals_oh + [z], dim=1))
        return [x]
```
