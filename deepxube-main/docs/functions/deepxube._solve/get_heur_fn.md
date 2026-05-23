---
id: "func:deepxube._solve.get_heur_fn"
kind: "function"
name: "get_heur_fn"
qualified_name: "deepxube._solve.get_heur_fn"
module: "deepxube._solve"
file: "deepxube/_solve.py"
line_start: 58
line_end: 93
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "domain"
    annotation: "Domain"
    default: null
  - name: "domain_name"
    annotation: "str"
    default: null
  - name: "heur_nnet_str"
    annotation: "Optional[str]"
    default: null
  - name: "heur_file"
    annotation: "Optional[str]"
    default: null
  - name: "heur_type"
    annotation: "Optional[str]"
    default: null
  - name: "nnet_batch_size"
    annotation: "Optional[int]"
    default: null
returns: "Optional[HeurFn]"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg"
    expr: "get_heur_nnet_par_from_arg"
    call_sites: [65]
  - target: "func:deepxube.nnet.nnet_utils.get_device"
    expr: "nnet_utils.get_device"
    call_sites: [66]
  - target: null
    expr: "print"
    call_sites: [67]
  - target: "func:deepxube.nnet.nnet_utils.load_nnet"
    expr: "nnet_utils.load_nnet"
    call_sites: [69]
  - target: null
    expr: "heur_nnet_par.get_nnet"
    call_sites: [69]
  - target: null
    expr: "nnet.eval"
    call_sites: [70]
  - target: null
    expr: "nnet.to"
    call_sites: [71]
  - target: "func:torch.nn.DataParallel"
    expr: "nn.DataParallel"
    call_sites: [72]
  - target: null
    expr: "heur_nnet_par.get_nnet_fn"
    call_sites: [73]
  - target: null
    expr: "heur_type.upper"
    call_sites: [75, 81]
  - target: null
    expr: "len"
    call_sites: [78, 86]
  - target: "func:deepxube._solve.HeurFnZerosV"
    expr: "HeurFnZerosV"
    call_sites: [80]
  - target: null
    expr: "heur_vals_l.append"
    call_sites: [86]
  - target: "func:deepxube._solve.HeurFnZerosQ"
    expr: "HeurFnZerosQ"
    call_sites: [89]
  - target: null
    expr: "ValueError"
    call_sites: [91]
raises:
  - exception: "ValueError"
    call_sites: [91]
reads_attrs: []
writes_attrs: []
---

# `deepxube._solve.get_heur_fn`

**File:** [deepxube/_solve.py:58](../../../../deepxube/_solve.py#L58)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_heur_fn(domain: Domain, domain_name: str, heur_nnet_str: Optional[str], heur_file: Optional[str], heur_type: Optional[str], nnet_batch_size: Optional[int]) -> Optional[HeurFn]
```

## Docstring

:return: Loaded ``HeurFn`` from file, an all-zeros fallback, or ``None`` if no heuristic is specified. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `domain` | `Domain` | — |
| `domain_name` | `str` | — |
| `heur_nnet_str` | `Optional[str]` | — |
| `heur_file` | `Optional[str]` | — |
| `heur_type` | `Optional[str]` | — |
| `nnet_batch_size` | `Optional[int]` | — |

## Returns

`Optional[HeurFn]`

## Calls

- `get_heur_nnet_par_from_arg` → `func:deepxube.utils.command_line_utils.get_heur_nnet_par_from_arg` (lines: 65)
- `nnet_utils.get_device` → `func:deepxube.nnet.nnet_utils.get_device` (lines: 66)
- `nnet_utils.load_nnet` → `func:deepxube.nnet.nnet_utils.load_nnet` (lines: 69)
- `nn.DataParallel` → `func:torch.nn.DataParallel` (lines: 72)
- `HeurFnZerosV` → `func:deepxube._solve.HeurFnZerosV` (lines: 80)
- `HeurFnZerosQ` → `func:deepxube._solve.HeurFnZerosQ` (lines: 89)

### Unresolved
- `print` (lines: 67)
- `heur_nnet_par.get_nnet` (lines: 69)
- `nnet.eval` (lines: 70)
- `nnet.to` (lines: 71)
- `heur_nnet_par.get_nnet_fn` (lines: 73)
- `heur_type.upper` (lines: 75, 81)
- `len` (lines: 78, 86)
- `heur_vals_l.append` (lines: 86)
- `ValueError` (lines: 91)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 91)

## Source

```python
def get_heur_fn(domain: Domain, domain_name: str, heur_nnet_str: Optional[str], heur_file: Optional[str], heur_type: Optional[str],
                nnet_batch_size: Optional[int]) -> Optional[HeurFn]:
    """ :return: Loaded ``HeurFn`` from file, an all-zeros fallback, or ``None`` if no heuristic is specified. """
    heur_fn: Optional[HeurFn] = None
    if heur_nnet_str is not None:
        assert heur_file is not None
        assert heur_type is not None
        heur_nnet_par: HeurNNetPar = get_heur_nnet_par_from_arg(domain, domain_name, heur_nnet_str, heur_type)[0]
        device, devices, on_gpu = nnet_utils.get_device()
        print("device: %s, devices: %s, on_gpu: %s" % (device, devices, on_gpu))

        nnet: nn.Module = nnet_utils.load_nnet(heur_file, heur_nnet_par.get_nnet())
        nnet.eval()
        nnet.to(device)
        nnet = nn.DataParallel(nnet)
        heur_fn = heur_nnet_par.get_nnet_fn(nnet, nnet_batch_size, device, None)
    elif heur_type is not None:
        if heur_type.upper() == "V":
            class HeurFnZerosV(HeurFnV):
                def __call__(self, states_in: List[State], goals_in: List[Goal]) -> List[float]:
                    return [0.0] * len(states_in)

            heur_fn = HeurFnZerosV()
        elif heur_type.upper() in {"QFIX", "QIN"}:
            class HeurFnZerosQ(HeurFnQ):
                def __call__(self, states_in: List[State], goals_in: List[Goal], actions_l_in: List[List[Action]]) -> List[List[float]]:
                    heur_vals_l: List[List[float]] = []
                    for actions_in in actions_l_in:
                        heur_vals_l.append([0.0] * len(actions_in))
                    return heur_vals_l

            heur_fn = HeurFnZerosQ()
        else:
            raise ValueError(f"Unknown heur type {heur_type}")

    return heur_fn
```
