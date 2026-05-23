---
id: "func:deepxube.pathfinding.graph_search.GraphSearchParser.help"
kind: "method"
name: "help"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchParser.help"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 308
line_end: 311
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
returns: "str"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.graph_search.GraphSearchParser._alg_name"
    expr: "self._alg_name"
    call_sites: [311]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.graph_search.GraphSearchParser.help`

**File:** [deepxube/pathfinding/graph_search.py:308](../../../../deepxube/pathfinding/graph_search.py#L308)
**Class:** `GraphSearchParser`
**Visibility:** public
**Kind:** method

## Signature

```python
def help(self) -> str
```

## Docstring

:return: CLI usage string describing ``B``/``W``/``E`` suffixes with an example. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`str`

## Calls

- `self._alg_name` → `func:deepxube.pathfinding.graph_search.GraphSearchParser._alg_name` (lines: 311)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def help(self) -> str:
        """ :return: CLI usage string describing ``B``/``W``/``E`` suffixes with an example. """
        return ("<int>B (batch size), <float>W (weight), <float>E (epsilon for chance to randomly pop node).\n"
                f"E.g. {self._alg_name()}.10B_0.5W_0.1E")
```
