---
id: "func:deepxube._cli.pathfinding_info"
kind: "function"
name: "pathfinding_info"
qualified_name: "deepxube._cli.pathfinding_info"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 101
line_end: 121
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
  - target: "func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_all_class_names"
    expr: "pathfinding_factory.get_all_class_names"
    call_sites: [105]
  - target: null
    expr: "args.names.split"
    call_sites: [107]
  - target: "func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_type"
    expr: "pathfinding_factory.get_type"
    call_sites: [110]
  - target: null
    expr: "print"
    call_sites: [111, 113, 115, 116, 120, 121]
  - target: null
    expr: "', '.join"
    call_sites: [112]
  - target: "func:deepxube._cli.get_immediate_mixins"
    expr: "get_immediate_mixins"
    call_sites: [112]
  - target: "func:textwrap.indent"
    expr: "textwrap.indent"
    call_sites: [113, 115, 116, 120]
  - target: null
    expr: "pathfind_t.domain_type"
    call_sites: [115]
  - target: null
    expr: "pathfind_t.functions_type"
    call_sites: [116]
  - target: "func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_parser"
    expr: "pathfinding_factory.get_parser"
    call_sites: [118]
  - target: null
    expr: "parser.help"
    call_sites: [120]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli.pathfinding_info`

**File:** [deepxube/_cli.py:101](../../../../deepxube/_cli.py#L101)
**Visibility:** public
**Kind:** function

## Signature

```python
def pathfinding_info(args: argparse.Namespace) -> None
```

## Docstring

Print mixins, domain/function type requirements, and parser help for each registered pathfinder. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `args` | `argparse.Namespace` | — |

## Returns

`None`

## Calls

- `pathfinding_factory.get_all_class_names` → `func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_all_class_names` (lines: 105)
- `pathfinding_factory.get_type` → `func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_type` (lines: 110)
- `get_immediate_mixins` → `func:deepxube._cli.get_immediate_mixins` (lines: 112)
- `textwrap.indent` → `func:textwrap.indent` (lines: 113, 115, 116, 120)
- `pathfinding_factory.get_parser` → `func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_parser` (lines: 118)

### Unresolved
- `args.names.split` (lines: 107)
- `print` (lines: 111, 113, 115, 116, 120, 121)
- `', '.join` (lines: 112)
- `pathfind_t.domain_type` (lines: 115)
- `pathfind_t.functions_type` (lines: 116)
- `parser.help` (lines: 120)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def pathfinding_info(args: argparse.Namespace) -> None:
    """ Print mixins, domain/function type requirements, and parser help for each registered pathfinder. """
    names: List[str]
    if args.names is None:
        names = pathfinding_factory.get_all_class_names()
    else:
        names = args.names.split(",")

    for name in names:
        pathfind_t: Type[PathFind] = pathfinding_factory.get_type(name)
        print(f"PathFind: {name}, {pathfind_t}")
        mixin_str: str = ', '.join([f"{x}" for x in get_immediate_mixins(pathfind_t, PathFind)])
        print(textwrap.indent(f"Mixins: {mixin_str}", '\t'))

        print(textwrap.indent(f"Domain type expected: {pathfind_t.domain_type()}", '\t'))
        print(textwrap.indent(f"Functions type expected: {pathfind_t.functions_type()}", '\t'))

        parser: Optional[Parser] = pathfinding_factory.get_parser(name)
        if parser is not None:
            print(textwrap.indent("Parser: " + parser.help(), '\t'))
        print("")
```
