---
id: "func:deepxube.factories.pathfinding_factory.get_pathfind_functions"
kind: "function"
name: "get_pathfind_functions"
qualified_name: "deepxube.factories.pathfinding_factory.get_pathfind_functions"
module: "deepxube.factories.pathfinding_factory"
file: "deepxube/factories/pathfinding_factory.py"
line_start: 22
line_end: 62
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "pathfind_name"
    annotation: "str"
    default: null
  - name: "heur_fn"
    annotation: "Optional[HeurFn]"
    default: null
  - name: "policy_fn"
    annotation: "Optional[PolicyFn]"
    default: null
returns: "Any"
docstring_source: "present"
callees:
  - target: "func:deepxube.factories.pathfinding_factory.get_type"
    expr: "pathfinding_factory.get_type"
    call_sites: [40]
  - target: null
    expr: "pathfind_t.functions_type"
    call_sites: [41]
  - target: null
    expr: "isinstance"
    call_sites: [43, 46, 52, 56]
  - target: "func:deepxube.base.pathfinding.FNsHeurV"
    expr: "FNsHeurV"
    call_sites: [44]
  - target: "func:deepxube.base.pathfinding.FNsHeurQ"
    expr: "FNsHeurQ"
    call_sites: [47]
  - target: "func:deepxube.base.pathfinding.FNsPolicy"
    expr: "FNsPolicy"
    call_sites: [50]
  - target: "func:deepxube.base.pathfinding.FNsHeurVPolicy"
    expr: "FNsHeurVPolicy"
    call_sites: [54]
  - target: "func:deepxube.base.pathfinding.FNsHeurQPolicy"
    expr: "FNsHeurQPolicy"
    call_sites: [58]
  - target: null
    expr: "ValueError"
    call_sites: [62]
raises:
  - exception: "ValueError"
    call_sites: [62]
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.pathfinding_factory.get_pathfind_functions`

**File:** [deepxube/factories/pathfinding_factory.py:22](../../../../deepxube/factories/pathfinding_factory.py#L22)
**Visibility:** public
**Kind:** function

## Signature

```python
def get_pathfind_functions(pathfind_name: str, heur_fn: Optional[HeurFn], policy_fn: Optional[PolicyFn]) -> Any
```

## Docstring

Package heuristic and policy callables into the ``FNs*`` dataclass
expected by the named pathfinder.

Returns whichever of ``FNsHeurV``, ``FNsHeurQ``, ``FNsPolicy``,
``FNsHeurVPolicy``, or ``FNsHeurQPolicy`` the pathfinder's
``functions_type()`` declares.

:param pathfind_name: Key of a registered ``PathFind`` subclass.
:param heur_fn: Heuristic function, required if the pathfinder uses one.
    Must be a ``HeurFnV`` for V-type pathfinders and a ``HeurFnQ`` for
    Q-type.
:param policy_fn: Policy function, required if the pathfinder uses one.
:return: A populated ``FNs*`` dataclass, or ``None`` if the pathfinder's
    ``functions_type`` is ``Any`` (i.e. supervised pathfinders).
:raises ValueError: If the pathfinder's ``functions_type`` is not one of
    the known ``FNs*`` classes.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `pathfind_name` | `str` | — |
| `heur_fn` | `Optional[HeurFn]` | — |
| `policy_fn` | `Optional[PolicyFn]` | — |

## Returns

`Any`

## Calls

- `pathfinding_factory.get_type` → `func:deepxube.factories.pathfinding_factory.get_type` (lines: 40)
- `FNsHeurV` → `func:deepxube.base.pathfinding.FNsHeurV` (lines: 44)
- `FNsHeurQ` → `func:deepxube.base.pathfinding.FNsHeurQ` (lines: 47)
- `FNsPolicy` → `func:deepxube.base.pathfinding.FNsPolicy` (lines: 50)
- `FNsHeurVPolicy` → `func:deepxube.base.pathfinding.FNsHeurVPolicy` (lines: 54)
- `FNsHeurQPolicy` → `func:deepxube.base.pathfinding.FNsHeurQPolicy` (lines: 58)

### Unresolved
- `pathfind_t.functions_type` (lines: 41)
- `isinstance` (lines: 43, 46, 52, 56)
- `ValueError` (lines: 62)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Raises

- `ValueError` (lines: 62)

## Source

```python
def get_pathfind_functions(pathfind_name: str, heur_fn: Optional[HeurFn], policy_fn: Optional[PolicyFn]) -> Any:
    """ Package heuristic and policy callables into the ``FNs*`` dataclass
    expected by the named pathfinder.

    Returns whichever of ``FNsHeurV``, ``FNsHeurQ``, ``FNsPolicy``,
    ``FNsHeurVPolicy``, or ``FNsHeurQPolicy`` the pathfinder's
    ``functions_type()`` declares.

    :param pathfind_name: Key of a registered ``PathFind`` subclass.
    :param heur_fn: Heuristic function, required if the pathfinder uses one.
        Must be a ``HeurFnV`` for V-type pathfinders and a ``HeurFnQ`` for
        Q-type.
    :param policy_fn: Policy function, required if the pathfinder uses one.
    :return: A populated ``FNs*`` dataclass, or ``None`` if the pathfinder's
        ``functions_type`` is ``Any`` (i.e. supervised pathfinders).
    :raises ValueError: If the pathfinder's ``functions_type`` is not one of
        the known ``FNs*`` classes.
    """
    pathfind_t: Type[PathFind] = pathfinding_factory.get_type(pathfind_name)
    functions_type: Any = pathfind_t.functions_type()
    if functions_type is FNsHeurV:
        assert (heur_fn is not None) and isinstance(heur_fn, HeurFnV)
        return FNsHeurV(heur_fn)
    elif functions_type is FNsHeurQ:
        assert (heur_fn is not None) and isinstance(heur_fn, HeurFnQ)
        return FNsHeurQ(heur_fn)
    elif functions_type is FNsPolicy:
        assert policy_fn is not None
        return FNsPolicy(policy_fn)
    elif functions_type is FNsHeurVPolicy:
        assert (heur_fn is not None) and isinstance(heur_fn, HeurFnV)
        assert policy_fn is not None
        return FNsHeurVPolicy(heur_fn, policy_fn)
    elif functions_type is FNsHeurQPolicy:
        assert (heur_fn is not None) and isinstance(heur_fn, HeurFnQ)
        assert policy_fn is not None
        return FNsHeurQPolicy(heur_fn, policy_fn)
    elif functions_type is Any:
        return None
    else:
        raise ValueError(f"Unknown Function type {functions_type}")
```
