---
id: "func:deepxube._cli.domain_info"
kind: "function"
name: "domain_info"
qualified_name: "deepxube._cli.domain_info"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 50
line_end: 80
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
  - target: "func:deepxube.factories.domain_factory.domain_factory.get_all_class_names"
    expr: "domain_factory.get_all_class_names"
    call_sites: [54]
  - target: null
    expr: "args.names.split"
    call_sites: [56]
  - target: "func:deepxube.factories.domain_factory.domain_factory.get_type"
    expr: "domain_factory.get_type"
    call_sites: [59]
  - target: null
    expr: "print"
    call_sites: [60, 63, 67, 71, 73, 77, 79, 80]
  - target: "func:deepxube.factories.domain_factory.domain_factory.get_parser"
    expr: "domain_factory.get_parser"
    call_sites: [61]
  - target: "func:textwrap.indent"
    expr: "textwrap.indent"
    call_sites: [63, 67, 71, 73, 77, 79]
  - target: null
    expr: "parser.help"
    call_sites: [63]
  - target: null
    expr: "', '.join"
    call_sites: [66]
  - target: "func:deepxube._cli.get_immediate_mixins"
    expr: "get_immediate_mixins"
    call_sites: [66]
  - target: "func:deepxube.factories.nnet_input_factory.get_domain_nnet_input_keys"
    expr: "get_domain_nnet_input_keys"
    call_sites: [70]
  - target: "func:deepxube.factories.nnet_input_factory.get_nnet_input_t"
    expr: "get_nnet_input_t"
    call_sites: [73]
  - target: "func:deepxube.factories.pathfinding_factory.get_domain_compat_pathfind_names"
    expr: "get_domain_compat_pathfind_names"
    call_sites: [76]
  - target: "func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_type"
    expr: "pathfinding_factory.get_type"
    call_sites: [79]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli.domain_info`

**File:** [deepxube/_cli.py:50](../../../../deepxube/_cli.py#L50)
**Visibility:** public
**Kind:** function

## Signature

```python
def domain_info(args: argparse.Namespace) -> None
```

## Docstring

Print mixins, NNet inputs, and compatible pathfinding algorithms for each registered domain. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `args` | `argparse.Namespace` | — |

## Returns

`None`

## Calls

- `domain_factory.get_all_class_names` → `func:deepxube.factories.domain_factory.domain_factory.get_all_class_names` (lines: 54)
- `domain_factory.get_type` → `func:deepxube.factories.domain_factory.domain_factory.get_type` (lines: 59)
- `domain_factory.get_parser` → `func:deepxube.factories.domain_factory.domain_factory.get_parser` (lines: 61)
- `textwrap.indent` → `func:textwrap.indent` (lines: 63, 67, 71, 73, 77, 79)
- `get_immediate_mixins` → `func:deepxube._cli.get_immediate_mixins` (lines: 66)
- `get_domain_nnet_input_keys` → `func:deepxube.factories.nnet_input_factory.get_domain_nnet_input_keys` (lines: 70)
- `get_nnet_input_t` → `func:deepxube.factories.nnet_input_factory.get_nnet_input_t` (lines: 73)
- `get_domain_compat_pathfind_names` → `func:deepxube.factories.pathfinding_factory.get_domain_compat_pathfind_names` (lines: 76)
- `pathfinding_factory.get_type` → `func:deepxube.factories.pathfinding_factory.pathfinding_factory.get_type` (lines: 79)

### Unresolved
- `args.names.split` (lines: 56)
- `print` (lines: 60, 63, 67, 71, 73, 77, 79, 80)
- `parser.help` (lines: 63)
- `', '.join` (lines: 66)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def domain_info(args: argparse.Namespace) -> None:
    """ Print mixins, NNet inputs, and compatible pathfinding algorithms for each registered domain. """
    domain_names: List[str]
    if args.names is None:
        domain_names = domain_factory.get_all_class_names()
    else:
        domain_names = args.names.split(",")

    for domain_name in domain_names:
        domain_t: Type[Domain] = domain_factory.get_type(domain_name)
        print(f"Domain: {domain_name}, {domain_t}")
        parser: Optional[Parser] = domain_factory.get_parser(domain_name)
        if parser is not None:
            print(textwrap.indent("Parser: " + parser.help(), '\t'))

        # mixins
        mixin_str: str = ', '.join([f"{x}" for x in get_immediate_mixins(domain_t, Domain)])
        print(textwrap.indent(f"Mixins: {mixin_str}", '\t'))

        # nnet inputs
        nnet_input_t_keys: List[Tuple[str, str]] = get_domain_nnet_input_keys(domain_name)
        print(textwrap.indent("NNet Inputs:", '\t'))
        for nnet_input_t_key in nnet_input_t_keys:
            print(textwrap.indent(f"Name: {nnet_input_t_key[1]}, Type: {get_nnet_input_t(nnet_input_t_key)}", '\t\t'))

        # pathfinding
        pathfind_names: List[str] = get_domain_compat_pathfind_names(domain_t)
        print(textwrap.indent("Pathfinding:", '\t'))
        for pathfind_name in pathfind_names:
            print(textwrap.indent(f"Name: {pathfind_name}, Type: {pathfinding_factory.get_type(pathfind_name)}", '\t\t'))
        print("")
```
