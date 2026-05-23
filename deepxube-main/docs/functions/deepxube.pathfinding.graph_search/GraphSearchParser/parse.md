---
id: "func:deepxube.pathfinding.graph_search.GraphSearchParser.parse"
kind: "method"
name: "parse"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchParser.parse"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 290
line_end: 306
class: "GraphSearchParser"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "args_str"
    annotation: "str"
    default: null
returns: "Dict[str, Any]"
docstring_source: "present"
callees:
  - target: null
    expr: "args_str.split"
    call_sites: [292]
  - target: null
    expr: "dict"
    call_sites: [293]
  - target: "func:re.search"
    expr: "re.search"
    call_sites: [295, 296, 297]
  - target: null
    expr: "int"
    call_sites: [299]
  - target: null
    expr: "batch_size_re.group"
    call_sites: [299]
  - target: null
    expr: "float"
    call_sites: [301, 303]
  - target: null
    expr: "weight_re.group"
    call_sites: [301]
  - target: null
    expr: "eps_re.group"
    call_sites: [303]
  - target: null
    expr: "ValueError"
    call_sites: [305]
raises:
  - exception: "ValueError"
    call_sites: [305]
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.GraphSearchParser.parse`

**File:** [deepxube/pathfinding/graph_search.py:290](../../../../deepxube/pathfinding/graph_search.py#L290)
**Class:** `GraphSearchParser`
**Visibility:** public
**Kind:** method

## Signature

```python
def parse(self, args_str: str) -> Dict[str, Any]
```

## Docstring

Parse an underscore-separated arg string into ``batch_size``, ``weight``, and/or ``eps`` kwargs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `args_str` | `str` | — |

## Returns

`Dict[str, Any]`

## Calls

- `re.search` → `func:re.search` (lines: 295, 296, 297)

### Unresolved
- `args_str.split` (lines: 292)
- `dict` (lines: 293)
- `int` (lines: 299)
- `batch_size_re.group` (lines: 299)
- `float` (lines: 301, 303)
- `weight_re.group` (lines: 301)
- `eps_re.group` (lines: 303)
- `ValueError` (lines: 305)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 305)

## Source

```python
    def parse(self, args_str: str) -> Dict[str, Any]:
        """ Parse an underscore-separated arg string into ``batch_size``, ``weight``, and/or ``eps`` kwargs. """
        args_str_l: List[str] = args_str.split("_")
        kwargs: Dict[str, Any] = dict()
        for args_str_i in args_str_l:
            batch_size_re = re.search(r"^(\S+)B$", args_str_i)
            weight_re = re.search(r"^(\S+)W", args_str_i)
            eps_re = re.search(r"^(\S+)E", args_str_i)
            if batch_size_re is not None:
                kwargs["batch_size"] = int(batch_size_re.group(1))
            elif weight_re is not None:
                kwargs["weight"] = float(weight_re.group(1))
            elif eps_re is not None:
                kwargs["eps"] = float(eps_re.group(1))
            else:
                raise ValueError(f"Unexpected argument {args_str_i!r}")
        return kwargs
```
