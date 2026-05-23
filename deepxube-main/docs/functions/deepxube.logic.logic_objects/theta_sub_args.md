---
id: "func:deepxube.logic.logic_objects.theta_sub_args"
kind: "function"
name: "theta_sub_args"
qualified_name: "deepxube.logic.logic_objects.theta_sub_args"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 365
line_end: 396
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "args1"
    annotation: "Tuple[str, ...]"
    default: null
  - name: "args2"
    annotation: "Tuple[str, ...]"
    default: null
  - name: "idxs_not_subbed"
    annotation: "List[int]"
    default: null
  - name: "subs_prev"
    annotation: "Dict[str, str]"
    default: null
  - name: "subs_forbid"
    annotation: "Dict[str, List[str]]"
    default: null
returns: "Optional[Dict[str, str]]"
docstring_source: "present"
callees:
  - target: null
    expr: "subs_prev.copy"
    call_sites: [369]
  - target: null
    expr: "subs.get"
    call_sites: [375, 383]
  - target: null
    expr: "subs_forbid.get"
    call_sites: [380]
  - target: null
    expr: "arg1[0].isupper"
    call_sites: [387]
  - target: null
    expr: "arg1[0].isalpha"
    call_sites: [387]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.logic.logic_objects.theta_sub_args`

**File:** [deepxube/logic/logic_objects.py:365](../../../../deepxube/logic/logic_objects.py#L365)
**Visibility:** public
**Kind:** function

## Signature

```python
def theta_sub_args(args1: Tuple[str, ...], args2: Tuple[str, ...], idxs_not_subbed: List[int], subs_prev: Dict[str, str], subs_forbid: Dict[str, List[str]]) -> Optional[Dict[str, str]]
```

## Docstring

Extend ``subs_prev`` with un-substituted argument positions; :return: updated dict or ``None`` on conflict. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `args1` | `Tuple[str, ...]` | — |
| `args2` | `Tuple[str, ...]` | — |
| `idxs_not_subbed` | `List[int]` | — |
| `subs_prev` | `Dict[str, str]` | — |
| `subs_forbid` | `Dict[str, List[str]]` | — |

## Returns

`Optional[Dict[str, str]]`

## Calls

*(No resolved calls.)*

### Unresolved
- `subs_prev.copy` (lines: 369)
- `subs.get` (lines: 375, 383)
- `subs_forbid.get` (lines: 380)
- `arg1[0].isupper` (lines: 387)
- `arg1[0].isalpha` (lines: 387)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def theta_sub_args(args1: Tuple[str, ...], args2: Tuple[str, ...], idxs_not_subbed: List[int],
                   subs_prev: Dict[str, str], subs_forbid: Dict[str, List[str]]) -> Optional[Dict[str, str]]:
    """ Extend ``subs_prev`` with un-substituted argument positions; :return: updated dict or ``None`` on conflict. """
    # assuming previous subs checked already if not negate
    subs: Dict[str, str] = subs_prev.copy()

    for idx in idxs_not_subbed:
        arg1: str = args1[idx]
        arg2: str = args2[idx]

        arg1_sub: Optional[str] = subs.get(arg1)
        if (arg1_sub is not None) and (arg1_sub != arg2):
            return None
        else:
            # check if neq constraint not violated
            args_other: Optional[List[str]] = subs_forbid.get(arg1, [])
            if args_other is not None:
                for arg_other in args_other:
                    arg_other_sub: Optional[str] = subs.get(arg_other)
                    if (arg_other_sub is not None) and (arg_other_sub == arg2):
                        return None

            is_var: bool = arg1[0].isupper() and arg1[0].isalpha()
            if is_var:
                # is variable, make substitution
                subs[arg1] = arg2
            else:
                # not variable, cannot substitute
                if arg1 != arg2:
                    return None

    return subs
```
