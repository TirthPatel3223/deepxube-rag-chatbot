---
id: "func:deepxube._cli._parse_viz_info"
kind: "function"
name: "_parse_viz_info"
qualified_name: "deepxube._cli._parse_viz_info"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 385
line_end: 393
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
    call_sites: [387, 388, 389, 390, 391]
  - target: null
    expr: "parser.set_defaults"
    call_sites: [393]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli._parse_viz_info`

**File:** [deepxube/_cli.py:385](../../../../deepxube/_cli.py#L385)
**Visibility:** private
**Kind:** function

## Signature

```python
def _parse_viz_info(parser: ArgumentParser) -> None
```

## Docstring

Register visualization arguments and set ``viz`` as the handler. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `parser` | `ArgumentParser` | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `parser.add_argument` (lines: 387, 388, 389, 390, 391)
- `parser.set_defaults` (lines: 393)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def _parse_viz_info(parser: ArgumentParser) -> None:
    """ Register visualization arguments and set ``viz`` as the handler. """
    parser.add_argument('--domain', type=str, required=True, help="Domain name and arguments.")
    parser.add_argument('--steps', type=int, default=0, help="Number of steps to take to generate problem instnace.")
    parser.add_argument('--file', type=str, default=None, help="If given, visualize results from file.")
    parser.add_argument('--idx', type=int, default=0, help="Index of problem instance in file.")
    parser.add_argument('--soln', action='store_true', default=False, help="If true, then assumes file contains solutions for problem instances and will "
                                                                           "visualize them.")
    parser.set_defaults(func=viz)
```
