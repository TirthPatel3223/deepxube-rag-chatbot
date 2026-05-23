---
id: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHER._get_pathfind_functions"
kind: "method"
name: "_get_pathfind_functions"
qualified_name: "deepxube.updaters.updater_q_rl.UpdateHeurQRLHER._get_pathfind_functions"
module: "deepxube.updaters.updater_q_rl"
file: "deepxube/updaters/updater_q_rl.py"
line_start: 271
line_end: 273
class: "UpdateHeurQRLHER"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "FNsHeurQ"
docstring_source: "present"
callees:
  - target: "func:deepxube.base.pathfinding.FNsHeurQ"
    expr: "FNsHeurQ"
    call_sites: [273]
  - target: "func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHER.get_heur_fn"
    expr: "self.get_heur_fn"
    call_sites: [273]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.updaters.updater_q_rl.UpdateHeurQRLHER._get_pathfind_functions`

**File:** [deepxube/updaters/updater_q_rl.py:271](../../../../deepxube/updaters/updater_q_rl.py#L271)
**Class:** `UpdateHeurQRLHER`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_pathfind_functions(self) -> FNsHeurQ
```

## Docstring

Build the ``FNsHeurQ`` bundle using this updater's heuristic fn. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`FNsHeurQ`

## Calls

- `FNsHeurQ` → `func:deepxube.base.pathfinding.FNsHeurQ` (lines: 273)
- `self.get_heur_fn` → `func:deepxube.updaters.updater_q_rl.UpdateHeurQRLHER.get_heur_fn` (lines: 273)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
    def _get_pathfind_functions(self) -> FNsHeurQ:
        """ Build the ``FNsHeurQ`` bundle using this updater's heuristic fn. """
        return FNsHeurQ(self.get_heur_fn())
```
