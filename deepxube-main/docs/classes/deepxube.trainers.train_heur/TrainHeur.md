---
id: "class:deepxube.trainers.train_heur.TrainHeur"
kind: "class"
name: "TrainHeur"
qualified_name: "deepxube.trainers.train_heur.TrainHeur"
module: "deepxube.trainers.train_heur"
file: "deepxube/trainers/train_heur.py"
line_start: 18
line_end: 52
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Train[HeurNNet, UpdateHeur]"
    resolved_id: null
methods:
  - "func:deepxube.trainers.train_heur.TrainHeur.data_parallel"
  - "func:deepxube.trainers.train_heur.TrainHeur._train_itr"
  - "func:deepxube.trainers.train_heur.TrainHeur._add_post_up_info"
  - "func:deepxube.trainers.train_heur.TrainHeur._get_shapes_dtypes"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.trainers.train_heur.TrainHeur`

**File:** [deepxube/trainers/train_heur.py:18](../../../deepxube/trainers/train_heur.py#L18)
**Abstract:** no

## Docstring

``Train`` subclass for heuristic networks; drives MSE training against cost-to-go labels. 

## Inheritance

**Direct bases:**
- `Train[HeurNNet, UpdateHeur]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `data_parallel` *(trivial, skipped)* — *(no docstring)*
- `_train_itr`
- `_add_post_up_info`
- `_get_shapes_dtypes` *(trivial, skipped)* — *(no docstring)*

## Source

```python
class TrainHeur(Train[HeurNNet, UpdateHeur]):
    """ ``Train`` subclass for heuristic networks; drives MSE training against cost-to-go labels. """

    @staticmethod
    def data_parallel() -> bool:
        return True

    def _train_itr(self, batch: List[NDArray], first_itr_in_update: bool, times: Times) -> float:
        """ Run one MSE gradient step on the heuristic network; :return: scalar loss for this batch. """
        start_time = time.time()
        inputs_batch_np: List[NDArray] = batch[:-1]
        ctgs_batch_np: NDArray = batch[-1]
        ctgs_batch_np = np.expand_dims(ctgs_batch_np.astype(np.float32), 1)

        self.nnet.train()
        update_optimizer(self.optimizer, self.nnet, self.status.itr)
        ctgs_batch_nnet, loss = train_heur_nnet_step(self.nnet, inputs_batch_np, ctgs_batch_np, self.optimizer, nn.MSELoss(), self.device,
                                                     self.status.itr, self.train_args, self.train_start_time)
        self.writer.add_scalar("train/loss", loss, self.status.itr)

        if first_itr_in_update:
            self.train_summary.itr_to_in_out[self.status.itr] = (ctgs_batch_np, ctgs_batch_nnet)
        times.record_time("train", time.time() - start_time)
        return loss

    def _add_post_up_info(self) -> List[str]:
        """ :return: Summary strings for cost-to-go mean/min/max from the latest data-generation update. """
        ctgs_mean, ctgs_min, ctgs_max = ctgs_summary([self.db.arrays[-1]])
        self.writer.add_scalar("train/ctgs/mean", ctgs_mean, self.status.itr)
        self.writer.add_scalar("train/ctgs/min", ctgs_min, self.status.itr)
        self.writer.add_scalar("train/ctgs/max", ctgs_max, self.status.itr)
        return [f"cost-to-go (mean/min/max): {ctgs_mean:.2f}/{ctgs_min:.2f}/{ctgs_max:.2f}"]

    def _get_shapes_dtypes(self) -> List[Tuple[Tuple[int, ...], np.dtype]]:
        return self.updater.get_heur_train_shapes_dtypes()
```
