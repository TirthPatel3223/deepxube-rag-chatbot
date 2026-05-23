---
id: "func:deepxube.base.updater.Update.start_procs"
kind: "method"
name: "start_procs"
qualified_name: "deepxube.base.updater.Update.start_procs"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 209
line_end: 243
class: "Update"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "rb_size"
    annotation: "int"
    default: null
returns: "Tuple[Queue, List[Queue]]"
docstring_source: "present"
callees:
  - target: "func:copy.deepcopy"
    expr: "copy.deepcopy"
    call_sites: [213]
  - target: null
    expr: "range"
    call_sites: [213]
  - target: "func:torch.multiprocessing.get_context"
    expr: "get_context"
    call_sites: [216]
  - target: null
    expr: "ctx.Queue"
    call_sites: [217, 221, 234, 235]
  - target: "func:deepxube.base.updater.Update.set_nnet_par_info_l_dict"
    expr: "self.set_nnet_par_info_l_dict"
    call_sites: [219]
  - target: null
    expr: "enumerate"
    call_sites: [220]
  - target: null
    expr: "self.from_main_qs.append"
    call_sites: [222]
  - target: "func:deepxube.base.updater.set_main_qs"
    expr: "updater.set_main_qs"
    call_sites: [223]
  - target: null
    expr: "self.nnet_par_info_l_dict.keys"
    call_sites: [224]
  - target: "func:deepxube.base.updater.set_nnet_par_info"
    expr: "updater.set_nnet_par_info"
    call_sites: [225]
  - target: null
    expr: "len"
    call_sites: [228, 230]
  - target: "func:deepxube.utils.misc_utils.split_evenly"
    expr: "split_evenly"
    call_sites: [230]
  - target: null
    expr: "min"
    call_sites: [231]
  - target: null
    expr: "zip"
    call_sites: [237]
  - target: null
    expr: "ctx.Process"
    call_sites: [238]
  - target: null
    expr: "proc.start"
    call_sites: [240]
  - target: null
    expr: "self.procs.append"
    call_sites: [241]
raises: []
reads_attrs:
  - "self.from_main_qs"
  - "self.from_q"
  - "self.nnet_par_info_l_dict"
  - "self.procs"
  - "self.to_q"
  - "self.up_args"
writes_attrs:
  - "self.from_main_qs"
  - "self.from_q"
  - "self.procs"
  - "self.to_q"
---

# `deepxube.base.updater.Update.start_procs`

**File:** [deepxube/base/updater.py:209](../../../../deepxube/base/updater.py#L209)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def start_procs(self, rb_size: int) -> Tuple[Queue, List[Queue]]
```

## Docstring

Spawn worker processes, assign queue triples, and return the main-side queues. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `rb_size` | `int` | — |

## Returns

`Tuple[Queue, List[Queue]]`

## Calls

- `copy.deepcopy` → `func:copy.deepcopy` (lines: 213)
- `get_context` → `func:torch.multiprocessing.get_context` (lines: 216)
- `self.set_nnet_par_info_l_dict` → `func:deepxube.base.updater.Update.set_nnet_par_info_l_dict` (lines: 219)
- `updater.set_main_qs` → `func:deepxube.base.updater.set_main_qs` (lines: 223)
- `updater.set_nnet_par_info` → `func:deepxube.base.updater.set_nnet_par_info` (lines: 225)
- `split_evenly` → `func:deepxube.utils.misc_utils.split_evenly` (lines: 230)

### Unresolved
- `range` (lines: 213)
- `ctx.Queue` (lines: 217, 221, 234, 235)
- `enumerate` (lines: 220)
- `self.from_main_qs.append` (lines: 222)
- `self.nnet_par_info_l_dict.keys` (lines: 224)
- `len` (lines: 228, 230)
- `min` (lines: 231)
- `zip` (lines: 237)
- `ctx.Process` (lines: 238)
- `proc.start` (lines: 240)
- `self.procs.append` (lines: 241)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.from_main_qs`
- `self.from_q`
- `self.procs`
- `self.to_q`

**Reads:**
- `self.from_main_qs`
- `self.from_q`
- `self.nnet_par_info_l_dict`
- `self.procs`
- `self.to_q`
- `self.up_args`

## Source

```python
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
```
