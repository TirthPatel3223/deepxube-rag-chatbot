---
id: "class:deepxube.base.updater.UpdateSup"
kind: "class"
name: "UpdateSup"
qualified_name: "deepxube.base.updater.UpdateSup"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 650
line_end: 680
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Update[D, Any, PS, Inst]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.updater.UpdateSup.functions_type"
  - "func:deepxube.base.updater.UpdateSup._step"
  - "func:deepxube.base.updater.UpdateSup._get_pathfind_functions"
  - "func:deepxube.base.updater.UpdateSup._make_instances"
  - "func:deepxube.base.updater.UpdateSup._step_sync_main"
  - "func:deepxube.base.updater.UpdateSup._get_instance_data_rb"
  - "func:deepxube.base.updater.UpdateSup._init_replay_buffer"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.updater.UpdateSup`

**File:** [deepxube/base/updater.py:650](../../../deepxube/base/updater.py#L650)
**Abstract:** yes

## Docstring

Supervised updater base: uses a ``PathFindSup`` random-walk pathfinder and no replay buffer. 

## Inheritance

**Direct bases:**
- `Update[D, Any, PS, Inst]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `functions_type` *(trivial, skipped)*
- `_step` *(trivial, skipped)*
- `_get_pathfind_functions` *(trivial, skipped)*
- `_make_instances` *(trivial, skipped)*
- `_step_sync_main` *(trivial, skipped)*
- `_get_instance_data_rb` *(trivial, skipped)*
- `_init_replay_buffer` *(trivial, skipped)*

## Source

```python
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
```
