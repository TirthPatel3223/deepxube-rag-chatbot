---
id: "func:deepxube.pathfinding.beam_search.BeamSearchParser.parse"
kind: "method"
name: "parse"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchParser.parse"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 303
line_end: 319
class: "BeamSearchParser"
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
    call_sites: [305]
  - target: null
    expr: "dict"
    call_sites: [306]
  - target: "func:re.search"
    expr: "re.search"
    call_sites: [308, 309, 310]
  - target: null
    expr: "int"
    call_sites: [312]
  - target: null
    expr: "beam_re.group"
    call_sites: [312]
  - target: null
    expr: "float"
    call_sites: [314, 316]
  - target: null
    expr: "temp_re.group"
    call_sites: [314]
  - target: null
    expr: "eps_re.group"
    call_sites: [316]
  - target: null
    expr: "ValueError"
    call_sites: [318]
raises:
  - exception: "ValueError"
    call_sites: [318]
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.beam_search.BeamSearchParser.parse`

**File:** [deepxube/pathfinding/beam_search.py:303](../../../../deepxube/pathfinding/beam_search.py#L303)
**Class:** `BeamSearchParser`
**Visibility:** public
**Kind:** method

## Signature

```python
def parse(self, args_str: str) -> Dict[str, Any]
```

## Docstring

Parse an underscore-separated arg string into ``beam_size``, ``temp``, and/or ``eps`` kwargs. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `args_str` | `str` | — |

## Returns

`Dict[str, Any]`

## Calls

- `re.search` → `func:re.search` (lines: 308, 309, 310)

### Unresolved
- `args_str.split` (lines: 305)
- `dict` (lines: 306)
- `int` (lines: 312)
- `beam_re.group` (lines: 312)
- `float` (lines: 314, 316)
- `temp_re.group` (lines: 314)
- `eps_re.group` (lines: 316)
- `ValueError` (lines: 318)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 318)

## Source

```python
    def parse(self, args_str: str) -> Dict[str, Any]:
        """ Parse an underscore-separated arg string into ``beam_size``, ``temp``, and/or ``eps`` kwargs. """
        args_str_l: List[str] = args_str.split("_")
        kwargs: Dict[str, Any] = dict()
        for args_str_i in args_str_l:
            beam_re = re.search(r"^(\S+)B$", args_str_i)
            temp_re = re.search(r"^(\S+)T", args_str_i)
            eps_re = re.search(r"^(\S+)E", args_str_i)
            if beam_re is not None:
                kwargs["beam_size"] = int(beam_re.group(1))
            elif temp_re is not None:
                kwargs["temp"] = float(temp_re.group(1))
            elif eps_re is not None:
                kwargs["eps"] = float(eps_re.group(1))
            else:
                raise ValueError(f"Unexpected argument {args_str_i!r}")
        return kwargs
```
