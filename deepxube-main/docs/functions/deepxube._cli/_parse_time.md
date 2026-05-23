---
id: "func:deepxube._cli._parse_time"
kind: "function"
name: "_parse_time"
qualified_name: "deepxube._cli._parse_time"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 396
line_end: 406
class: null
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "parser"
    annotation: "ArgumentParser"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "parser.add_argument"
    call_sites: [398, 399, 400, 401, 402, 403, 404, 405]
  - target: null
    expr: "parser.set_defaults"
    call_sites: [406]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli._parse_time`

**File:** [deepxube/_cli.py:396](../../../../deepxube/_cli.py#L396)
**Visibility:** private
**Kind:** function

## Signature

```python
def _parse_time(parser: ArgumentParser) -> None
```

## Docstring

Register timing arguments and set ``time_test_args`` as the handler. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `parser` | `ArgumentParser` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `parser.add_argument` (lines: 398, 399, 400, 401, 402, 403, 404, 405)
- `parser.set_defaults` (lines: 406)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _parse_time(parser: ArgumentParser) -> None:
    """ Register timing arguments and set ``time_test_args`` as the handler. """
    parser.add_argument('--domain', type=str, required=True, help="Domain name and arguments.")
    parser.add_argument('--heur', type=str, default=None, help="Heuristic name and arguments.")
    parser.add_argument('--heur_type', type=str, default="V", help="V, QFix, QIn.")
    parser.add_argument('--policy', type=str, default=None, help="Policy name and arguments.")
    parser.add_argument('--policy_samp', type=int, default=10, help="")
    parser.add_argument('--policy_rand', type=int, default=5, help="")
    parser.add_argument('--num_insts', type=int, default=10, help="Number of problem instances to generate.")
    parser.add_argument('--step_max', type=int, default=10, help="Randomly generates problem instances with between 0 and step_max steps.")
    parser.set_defaults(func=time_test_args)
```
