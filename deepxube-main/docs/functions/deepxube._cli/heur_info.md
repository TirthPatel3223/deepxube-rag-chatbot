---
id: "func:deepxube._cli.heur_info"
kind: "function"
name: "heur_info"
qualified_name: "deepxube._cli.heur_info"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 83
line_end: 98
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "args"
    annotation: "argparse.Namespace"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.factories.heuristic_factory.heuristic_factory.get_all_class_names"
    expr: "heuristic_factory.get_all_class_names"
    call_sites: [87]
  - target: null
    expr: "args.names.split"
    call_sites: [89]
  - target: "func:deepxube.factories.heuristic_factory.heuristic_factory.get_type"
    expr: "heuristic_factory.get_type"
    call_sites: [92]
  - target: null
    expr: "print"
    call_sites: [93, 94, 97, 98]
  - target: "func:textwrap.indent"
    expr: "textwrap.indent"
    call_sites: [94, 97]
  - target: null
    expr: "heur_nnet_t.nnet_input_type"
    call_sites: [94]
  - target: "func:deepxube.factories.heuristic_factory.heuristic_factory.get_parser"
    expr: "heuristic_factory.get_parser"
    call_sites: [95]
  - target: null
    expr: "parser.help"
    call_sites: [97]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli.heur_info`

**File:** [deepxube/_cli.py:83](../../../../deepxube/_cli.py#L83)
**Visibility:** public
**Kind:** function

## Signature

```python
def heur_info(args: argparse.Namespace) -> None
```

## Docstring

Print expected NNet input type and parser help for each registered heuristic network. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `args` | `argparse.Namespace` | — |

## Returns

`None`

## Calls

- `heuristic_factory.get_all_class_names` → `func:deepxube.factories.heuristic_factory.heuristic_factory.get_all_class_names` (lines: 87)
- `heuristic_factory.get_type` → `func:deepxube.factories.heuristic_factory.heuristic_factory.get_type` (lines: 92)
- `textwrap.indent` → `func:textwrap.indent` (lines: 94, 97)
- `heuristic_factory.get_parser` → `func:deepxube.factories.heuristic_factory.heuristic_factory.get_parser` (lines: 95)

### Unresolved
- `args.names.split` (lines: 89)
- `print` (lines: 93, 94, 97, 98)
- `heur_nnet_t.nnet_input_type` (lines: 94)
- `parser.help` (lines: 97)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def heur_info(args: argparse.Namespace) -> None:
    """ Print expected NNet input type and parser help for each registered heuristic network. """
    heur_nnet_names: List[str]
    if args.names is None:
        heur_nnet_names = heuristic_factory.get_all_class_names()
    else:
        heur_nnet_names = args.names.split(",")

    for heur_nnet_name in heur_nnet_names:
        heur_nnet_t: Type[HeurNNet] = heuristic_factory.get_type(heur_nnet_name)
        print(f"Heur NNet: {heur_nnet_name}, {heur_nnet_t}")
        print(textwrap.indent(f"NNet_Input type expected: {heur_nnet_t.nnet_input_type()}", '\t'))
        parser: Optional[Parser] = heuristic_factory.get_parser(heur_nnet_name)
        if parser is not None:
            print(textwrap.indent("Parser: " + parser.help(), '\t'))
        print("")
```
