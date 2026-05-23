---
id: "func:deepxube.pathfinding.beam_search.BeamSearchParser.help"
kind: "method"
name: "help"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchParser.help"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 321
line_end: 324
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
returns: "str"
docstring_source: "present"
callees:
  - target: "func:deepxube.pathfinding.beam_search.BeamSearchParser._alg_name"
    expr: "self._alg_name"
    call_sites: [324]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.pathfinding.beam_search.BeamSearchParser.help`

**File:** [deepxube/pathfinding/beam_search.py:321](../../../../deepxube/pathfinding/beam_search.py#L321)
**Class:** `BeamSearchParser`
**Visibility:** public
**Kind:** method

## Signature

```python
def help(self) -> str
```

## Docstring

:return: CLI usage string describing ``B``/``T``/``E`` suffixes with an example. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`str`

## Calls

- `self._alg_name` → `func:deepxube.pathfinding.beam_search.BeamSearchParser._alg_name` (lines: 324)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def help(self) -> str:
        """ :return: CLI usage string describing ``B``/``T``/``E`` suffixes with an example. """
        return ("<int>B (beam size), <float>T (temperature for Boltzmann distribution), <float>E (epsilon for chance to randomly select node).\n"
                f"E.g. {self._alg_name()}.10B_1.0T_0.1E")
```
