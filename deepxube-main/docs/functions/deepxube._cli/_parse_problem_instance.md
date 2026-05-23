---
id: "func:deepxube._cli._parse_problem_instance"
kind: "function"
name: "_parse_problem_instance"
qualified_name: "deepxube._cli._parse_problem_instance"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 409
line_end: 417
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
    call_sites: [411, 412, 413, 414, 415, 416]
  - target: null
    expr: "parser.set_defaults"
    call_sites: [417]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli._parse_problem_instance`

**File:** [deepxube/_cli.py:409](../../../../deepxube/_cli.py#L409)
**Visibility:** private
**Kind:** function

## Signature

```python
def _parse_problem_instance(parser: ArgumentParser) -> None
```

## Docstring

Register problem-instance generation arguments and set ``problem_inst_gen`` as the handler. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `parser` | `ArgumentParser` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `parser.add_argument` (lines: 411, 412, 413, 414, 415, 416)
- `parser.set_defaults` (lines: 417)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _parse_problem_instance(parser: ArgumentParser) -> None:
    """ Register problem-instance generation arguments and set ``problem_inst_gen`` as the handler. """
    parser.add_argument('--domain', type=str, required=True, help="Domain name and arguments.")
    parser.add_argument('--step_min', type=int, default=0, help="Minimum number of steps to take")
    parser.add_argument('--step_max', type=int, required=True, help="Maximum number of steps to take (inclusive)")
    parser.add_argument('--num', type=int, required=True, help="Number of problem instances to generate.")
    parser.add_argument('--file', type=str, required=True, help="File to which problem instances are stored.")
    parser.add_argument('--redo', action='store_true', default=False, help="If true, generate problem instances even if file already exists.")
    parser.set_defaults(func=problem_inst_gen)
```
