---
id: "func:deepxube.base.updater.Update._add_instances"
kind: "method"
name: "_add_instances"
qualified_name: "deepxube.base.updater.Update._add_instances"
module: "deepxube.base.updater"
file: "deepxube/base/updater.py"
line_start: 447
line_end: 472
class: "Update"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "pathfind"
    annotation: "P"
    default: null
  - name: "insts_rem"
    annotation: "List[Inst]"
    default: null
  - name: "batch_size"
    annotation: "int"
    default: null
  - name: "step_probs"
    annotation: "List[int]"
    default: null
  - name: "times"
    annotation: "Times"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "len"
    call_sites: [452, 456]
  - target: "func:time.time"
    expr: "time.time"
    call_sites: [454, 460, 463, 465, 470, 472]
  - target: null
    expr: "int"
    call_sites: [457]
  - target: null
    expr: "np.random.choice(self.up_args.step_max + 1, size=batch_size, p=np.array(step_probs)).tolist"
    call_sites: [459]
  - target: null
    expr: "np.random.choice"
    call_sites: [459]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [459]
  - target: null
    expr: "times.record_time"
    call_sites: [460, 465, 472]
  - target: "func:deepxube.base.updater.Update._make_instances"
    expr: "self._make_instances"
    call_sites: [467]
  - target: null
    expr: "pathfind.add_instances"
    call_sites: [471]
raises: []
reads_attrs:
  - "self.up_args"
writes_attrs: []
---

# `deepxube.base.updater.Update._add_instances`

**File:** [deepxube/base/updater.py:447](../../../../deepxube/base/updater.py#L447)
**Class:** `Update`
**Visibility:** private
**Kind:** method

## Signature

```python
def _add_instances(self, pathfind: P, insts_rem: List[Inst], batch_size: int, step_probs: List[int], times: Times) -> None
```

## Docstring

Top up the pathfinder with new instances. Reuses step counts from
finished instances (``insts_rem``) when available, otherwise samples
step counts from ``step_probs``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `pathfind` | `P` | — |
| `insts_rem` | `List[Inst]` | — |
| `batch_size` | `int` | — |
| `step_probs` | `List[int]` | — |
| `times` | `Times` | — |

## Returns

`None`

## Calls

- `time.time` → `func:time.time` (lines: 454, 460, 463, 465, 470, 472)
- `np.array` → `func:numpy.array` (lines: 459)
- `self._make_instances` → `func:deepxube.base.updater.Update._make_instances` (lines: 467)

### Unresolved
- `len` (lines: 452, 456)
- `int` (lines: 457)
- `np.random.choice(self.up_args.step_max + 1, size=batch_size, p=np.array(step_probs)).tolist` (lines: 459)
- `np.random.choice` (lines: 459)
- `times.record_time` (lines: 460, 465, 472)
- `pathfind.add_instances` (lines: 471)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.up_args`

## Source

```python
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
```
