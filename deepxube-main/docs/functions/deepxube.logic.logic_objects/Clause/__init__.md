---
id: "func:deepxube.logic.logic_objects.Clause.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.logic.logic_objects.Clause.__init__"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 100
line_end: 111
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
  - name: "head"
    annotation: "Literal"
    default: null
  - name: "body"
    annotation: "Tuple[Literal, ...]"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "set"
    call_sites: [106]
  - target: null
    expr: "self.all_vars.update"
    call_sites: [107, 109]
raises: []
reads_attrs:
  - "self.all_vars"
  - "self.body"
  - "self.hash"
  - "self.head"
writes_attrs:
  - "self.all_vars"
  - "self.body"
  - "self.hash"
  - "self.head"
---

# `deepxube.logic.logic_objects.Clause.__init__`

**File:** [deepxube/logic/logic_objects.py:100](../../../../deepxube/logic/logic_objects.py#L100)
**Class:** `Clause`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, head: Literal, body: Tuple[Literal, ...])
```

## Docstring

Store head/body literals and collect the set of all variable names across the clause. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `head` | `Literal` | — |
| `body` | `Tuple[Literal, ...]` | — |

## Returns

*(Not annotated.)*

## Calls

*(No resolved calls.)*

### Unresolved
- `set` (lines: 106)
- `self.all_vars.update` (lines: 107, 109)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.all_vars`
- `self.body`
- `self.hash`
- `self.head`

**Reads:**
- `self.all_vars`
- `self.body`
- `self.hash`
- `self.head`

## Source

```python
    def __init__(self, head: Literal, body: Tuple[Literal, ...]):
        """ Store head/body literals and collect the set of all variable names across the clause. """
        self.head: Literal = head
        self.body: Tuple[Literal, ...] = body

        # compute all the 'vars' in the program
        self.all_vars: Set[str] = set()
        self.all_vars.update(head.arguments)
        for literal in (self.head,) + self.body:
            self.all_vars.update(literal.arguments)

        self.hash: Optional[int] = None
```
