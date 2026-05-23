---
id: "func:deepxube.logic.logic_objects.LitNode.prop_down"
kind: "method"
name: "prop_down"
qualified_name: "deepxube.logic.logic_objects.LitNode.prop_down"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 80
line_end: 83
class: "LitNode"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "enumerate"
    call_sites: [82]
  - target: null
    expr: "hash"
    call_sites: [83]
raises: []
reads_attrs:
  - "self.rep"
  - "self.var_nodes"
writes_attrs: []
---

# `deepxube.logic.logic_objects.LitNode.prop_down`

**File:** [deepxube/logic/logic_objects.py:80](../../../../deepxube/logic/logic_objects.py#L80)
**Class:** `LitNode`
**Visibility:** public
**Kind:** method

## Signature

```python
def prop_down(self) -> None
```

## Docstring

Propagate this literal's rep down into its variable nodes. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

*(No resolved calls.)*

### Unresolved
- `enumerate` (lines: 82)
- `hash` (lines: 83)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.rep`
- `self.var_nodes`

## Source

```python
    def prop_down(self) -> None:
        """ Propagate this literal's rep down into its variable nodes. """
        for var_idx, var_node in enumerate(self.var_nodes):
            var_node.rep = hash((self.rep, var_idx))
```
