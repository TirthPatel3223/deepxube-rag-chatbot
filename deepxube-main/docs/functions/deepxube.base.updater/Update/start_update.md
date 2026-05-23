---
id: "func:deepxube.base.updater.Update.start_update"
kind: "method"
name: "start_update"
qualified_name: "deepxube.base.updater.Update.start_update"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 245
line_end: 271
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
  - name: "step_probs"
    annotation: "List[int]"
    default: null
  - name: "num_gen"
    annotation: "int"
    default: null
  - name: "train_batch_size"
    annotation: "int"
    default: null
  - name: "device"
    annotation: "torch.device"
    default: null
  - name: "on_gpu"
    annotation: "bool"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.updater.Update.start_nnet_runners"
    expr: "self.start_nnet_runners"
    call_sites: [251]
  - target: null
    expr: "enumerate"
    call_sites: [254]
  - target: null
    expr: "from_main_q.put"
    call_sites: [255]
  - target: null
    expr: "self.targ_update_nums.copy"
    call_sites: [255]
  - target: null
    expr: "print"
    call_sites: [262]
  - target: null
    expr: "format"
    call_sites: [262]
  - target: "func:deepxube.utils.misc_utils.split_evenly_w_max"
    expr: "split_evenly_w_max"
    call_sites: [267]
  - target: null
    expr: "min"
    call_sites: [268]
  - target: null
    expr: "self.to_q.put"
    call_sites: [271]
raises: []
reads_attrs:
  - "self.from_main_qs"
  - "self.targ_update_nums"
  - "self.to_q"
  - "self.up_args"
writes_attrs: []
---

# `deepxube.base.updater.Update.start_update`

**File:** [deepxube/base/updater.py:245](../../../../deepxube/base/updater.py#L245)
**Class:** `Update`
**Visibility:** public
**Kind:** method

## Signature

```python
def start_update(self, step_probs: List[int], num_gen: int, train_batch_size: int, device: torch.device, on_gpu: bool) -> None
```

## Docstring

Kick off one round of data generation: start NNet runners, send
step-distribution + target-update nums to each worker, and enqueue
the per-worker batch counts. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `step_probs` | `List[int]` | — |
| `num_gen` | `int` | — |
| `train_batch_size` | `int` | — |
| `device` | `torch.device` | — |
| `on_gpu` | `bool` | — |

## Returns

`None`

## Calls

- `self.start_nnet_runners` → `func:deepxube.base.updater.Update.start_nnet_runners` (lines: 251)
- `split_evenly_w_max` → `func:deepxube.utils.misc_utils.split_evenly_w_max` (lines: 267)

### Unresolved
- `enumerate` (lines: 254)
- `from_main_q.put` (lines: 255)
- `self.targ_update_nums.copy` (lines: 255)
- `print` (lines: 262)
- `format` (lines: 262)
- `min` (lines: 268)
- `self.to_q.put` (lines: 271)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.from_main_qs`
- `self.targ_update_nums`
- `self.to_q`
- `self.up_args`

## Source

```python
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
```
