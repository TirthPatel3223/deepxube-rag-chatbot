---
id: "func:deepxube.base.updater.Update.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.base.updater.Update.__init__"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 136
line_end: 165
class: "Update"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "domain"
    annotation: "D"
    default: null
  - name: "pathfind_arg"
    annotation: "str"
    default: null
  - name: "up_args"
    annotation: "UpArgs"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs"
    expr: "get_pathfind_name_kwargs"
    call_sites: [141]
  - target: null
    expr: "dict"
    call_sites: [145, 146, 147, 151, 152, 155, 156]
  - target: null
    expr: "domain.get_nnet_pars"
    call_sites: [148]
  - target: "func:deepxube.base.updater.Update.add_nnet_par"
    expr: "self.add_nnet_par"
    call_sites: [149]
  - target: "func:deepxube.base.updater.Update.set_nnet_file"
    expr: "self.set_nnet_file"
    call_sites: [150]
raises: []
reads_attrs:
  - "self.domain"
  - "self.from_main_q"
  - "self.from_main_qs"
  - "self.from_q"
  - "self.nnet_file_dict"
  - "self.nnet_fn_dict"
  - "self.nnet_par_dict"
  - "self.nnet_par_info_dict"
  - "self.nnet_par_info_l_dict"
  - "self.nnet_par_info_main"
  - "self.nnet_runner_proc_l_dict"
  - "self.num_generated"
  - "self.pathfind_arg"
  - "self.pathfind_kwargs"
  - "self.pathfind_name"
  - "self.procs"
  - "self.q_id"
  - "self.targ_update_nums"
  - "self.to_main_q"
  - "self.to_q"
  - "self.up_args"
writes_attrs:
  - "self.domain"
  - "self.from_main_q"
  - "self.from_main_qs"
  - "self.from_q"
  - "self.nnet_file_dict"
  - "self.nnet_fn_dict"
  - "self.nnet_par_dict"
  - "self.nnet_par_info_dict"
  - "self.nnet_par_info_l_dict"
  - "self.nnet_par_info_main"
  - "self.nnet_runner_proc_l_dict"
  - "self.num_generated"
  - "self.pathfind_arg"
  - "self.pathfind_kwargs"
  - "self.pathfind_name"
  - "self.procs"
  - "self.q_id"
  - "self.targ_update_nums"
  - "self.to_main_q"
  - "self.to_q"
  - "self.up_args"
---

# `deepxube.base.updater.Update.__init__`

**File:** [deepxube/base/updater.py:136](../../../../deepxube/base/updater.py#L136)
**Class:** `Update`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, domain: D, pathfind_arg: str, up_args: UpArgs)
```

## Docstring

Store the domain, parse the pathfinding argument, and register
every NNet supplied by ``domain.get_nnet_pars``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `domain` | `D` | — |
| `pathfind_arg` | `str` | — |
| `up_args` | `UpArgs` | — |

## Returns

*(Not annotated.)*

## Calls

- `get_pathfind_name_kwargs` → `func:deepxube.utils.command_line_utils.get_pathfind_name_kwargs` (lines: 141)
- `self.add_nnet_par` → `func:deepxube.base.updater.Update.add_nnet_par` (lines: 149)
- `self.set_nnet_file` → `func:deepxube.base.updater.Update.set_nnet_file` (lines: 150)

### Unresolved
- `dict` (lines: 145, 146, 147, 151, 152, 155, 156)
- `domain.get_nnet_pars` (lines: 148)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.domain`
- `self.from_main_q`
- `self.from_main_qs`
- `self.from_q`
- `self.nnet_file_dict`
- `self.nnet_fn_dict`
- `self.nnet_par_dict`
- `self.nnet_par_info_dict`
- `self.nnet_par_info_l_dict`
- `self.nnet_par_info_main`
- `self.nnet_runner_proc_l_dict`
- `self.num_generated`
- `self.pathfind_arg`
- `self.pathfind_kwargs`
- `self.pathfind_name`
- `self.procs`
- `self.q_id`
- `self.targ_update_nums`
- `self.to_main_q`
- `self.to_q`
- `self.up_args`

**Reads:**
- `self.domain`
- `self.from_main_q`
- `self.from_main_qs`
- `self.from_q`
- `self.nnet_file_dict`
- `self.nnet_fn_dict`
- `self.nnet_par_dict`
- `self.nnet_par_info_dict`
- `self.nnet_par_info_l_dict`
- `self.nnet_par_info_main`
- `self.nnet_runner_proc_l_dict`
- `self.num_generated`
- `self.pathfind_arg`
- `self.pathfind_kwargs`
- `self.pathfind_name`
- `self.procs`
- `self.q_id`
- `self.targ_update_nums`
- `self.to_main_q`
- `self.to_q`
- `self.up_args`

## Source

```python
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
```
