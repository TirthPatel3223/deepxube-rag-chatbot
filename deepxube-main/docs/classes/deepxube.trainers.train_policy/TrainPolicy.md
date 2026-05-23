---
id: "class:deepxube.trainers.train_policy.TrainPolicy"
kind: "class"
name: "TrainPolicy"
qualified_name: "deepxube.trainers.train_policy.TrainPolicy"
module: "deepxube.trainers.train_policy"
file: "deepxube/trainers/train_policy.py"
line_start: 16
line_end: 39
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Train[PolicyNNet, UpdatePolicy]"
    resolved_id: null
methods:
  - "func:deepxube.trainers.train_policy.TrainPolicy.data_parallel"
  - "func:deepxube.trainers.train_policy.TrainPolicy._train_itr"
  - "func:deepxube.trainers.train_policy.TrainPolicy._add_post_up_info"
  - "func:deepxube.trainers.train_policy.TrainPolicy._get_shapes_dtypes"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.trainers.train_policy.TrainPolicy`

**File:** [deepxube/trainers/train_policy.py:16](../../../deepxube/trainers/train_policy.py#L16)
**Abstract:** no

## Docstring

``Train`` subclass for policy (VAE) networks; drives training using the policy network's own loss function. 

## Inheritance

**Direct bases:**
- `Train[PolicyNNet, UpdatePolicy]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `data_parallel` *(trivial, skipped)* — *(no docstring)*
- `_train_itr`
- `_add_post_up_info` *(trivial, skipped)* — *(no docstring)*
- `_get_shapes_dtypes` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class TrainPolicy(Train[PolicyNNet, UpdatePolicy]):
    """ ``Train`` subclass for policy (VAE) networks; drives training using the policy network's own loss function. """

    @staticmethod
    def data_parallel() -> bool:
        return False

    def _train_itr(self, batch: List[NDArray], first_itr_in_update: bool, times: Times) -> float:
        """ Run one policy gradient step; :return: scalar loss for this batch. """
        start_time = time.time()

        self.nnet.train()
        update_optimizer(self.optimizer, self.nnet, self.status.itr)
        loss = train_policy_nnet_step(self.nnet, batch, self.optimizer, self.device, self.status.itr, self.train_args, self.train_start_time)
        self.writer.add_scalar("train/loss", loss, self.status.itr)

        times.record_time("train", time.time() - start_time)
        return loss

    def _add_post_up_info(self) -> List[str]:
        return []

    def _get_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        return self.updater.get_policy_train_shapes_dtypes()
```
