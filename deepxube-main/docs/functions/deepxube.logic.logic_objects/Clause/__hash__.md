---
id: "func:deepxube.logic.logic_objects.Clause.__hash__"
kind: "method"
name: "__hash__"
qualified_name: "deepxube.logic.logic_objects.Clause.__hash__"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 226
line_end: 271
class: "Clause"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "int"
docstring_source: "present"
callees:
  - target: null
    expr: "lit_nodes.append"
    call_sites: [234, 237]
  - target: "func:deepxube.logic.logic_objects.LitNode"
    expr: "LitNode"
    call_sites: [234, 237]
  - target: null
    expr: "enumerate"
    call_sites: [240, 241, 244, 245]
  - target: null
    expr: "lit_node1.var_nodes[var_idx1].add_neighbor"
    call_sites: [247]
  - target: null
    expr: "var_nodes.extend"
    call_sites: [252]
  - target: null
    expr: "lit_node.prop_up"
    call_sites: [256, 267]
  - target: null
    expr: "range"
    call_sites: [260]
  - target: null
    expr: "lit_node.prop_down"
    call_sites: [262]
  - target: "func:deepxube.logic.logic_objects.prop_across"
    expr: "prop_across"
    call_sites: [264]
  - target: null
    expr: "sum"
    call_sites: [269]
raises: []
reads_attrs:
  - "self.body"
  - "self.hash"
  - "self.head"
writes_attrs:
  - "self.hash"
---

# `deepxube.logic.logic_objects.Clause.__hash__`

**File:** [deepxube/logic/logic_objects.py:226](../../../../deepxube/logic/logic_objects.py#L226)
**Class:** `Clause`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __hash__(self) -> int
```

## Docstring

:return: Structure hash computed by WL-style message-passing over the literal/variable graph. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`int`

## Calls

- `LitNode` → `func:deepxube.logic.logic_objects.LitNode` (lines: 234, 237)
- `prop_across` → `func:deepxube.logic.logic_objects.prop_across` (lines: 264)

### Unresolved
- `lit_nodes.append` (lines: 234, 237)
- `enumerate` (lines: 240, 241, 244, 245)
- `lit_node1.var_nodes[var_idx1].add_neighbor` (lines: 247)
- `var_nodes.extend` (lines: 252)
- `lit_node.prop_up` (lines: 256, 267)
- `range` (lines: 260)
- `lit_node.prop_down` (lines: 262)
- `sum` (lines: 269)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.hash`

**Reads:**
- `self.body`
- `self.hash`
- `self.head`

## Source

```python
    def __hash__(self) -> int:
        """ :return: Structure hash computed by WL-style message-passing over the literal/variable graph. """
        if self.hash is not None:
            return self.hash

        # make lit nodes
        lit_nodes: List[LitNode] = []
        for lit in [self.head]:
            lit_nodes.append(LitNode(lit.predicate, False, lit.arguments))

        for lit in self.body:
            lit_nodes.append(LitNode(lit.predicate, True, lit.arguments))

        # make connections between variable nodes
        for lit1_idx, lit_node1 in enumerate(lit_nodes):
            for lit2_idx, lit_node2 in enumerate(lit_nodes):
                if lit1_idx == lit2_idx:
                    continue
                for var_idx1, var_name1 in enumerate(lit_node1.var_names):
                    for var_idx2, var_name2 in enumerate(lit_node2.var_names):
                        if var_name1 == var_name2:
                            lit_node1.var_nodes[var_idx1].add_neighbor(lit_node2.var_nodes[var_idx2])

        # get all variable nodes
        var_nodes: List[VarNode] = []
        for lit_node in lit_nodes:
            var_nodes.extend(lit_node.var_nodes)

        # init representation
        for lit_node in lit_nodes:
            lit_node.prop_up()

        # propagate
        self.hash = 0
        for _ in range(10):
            for lit_node in lit_nodes:
                lit_node.prop_down()

            prop_across(var_nodes)

            for lit_node in lit_nodes:
                lit_node.prop_up()

        self.hash = sum([lit_node.rep for lit_node in lit_nodes])

        return self.hash
```
