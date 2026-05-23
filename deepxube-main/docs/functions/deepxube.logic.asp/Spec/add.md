---
id: "func:deepxube.logic.asp.Spec.add"
kind: "method"
name: "add"
qualified_name: "deepxube.logic.asp.Spec.add"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 82
line_end: 88
class: "Spec"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "spec_add"
    annotation: "'Spec'"
    default: null
returns: "'Spec'"
docstring_source: "present"
callees:
  - target: "func:deepxube.logic.asp.Spec"
    expr: "Spec"
    call_sites: [84]
raises: []
reads_attrs:
  - "self.atoms_false"
  - "self.atoms_true"
  - "self.goal_false"
  - "self.goal_true"
  - "self.models_banned"
writes_attrs: []
---

# `deepxube.logic.asp.Spec.add`

**File:** [deepxube/logic/asp.py:82](../../../../deepxube/logic/asp.py#L82)
**Class:** `Spec`
**Visibility:** public
**Kind:** method

## Signature

```python
def add(self, spec_add: 'Spec') -> 'Spec'
```

## Docstring

:return: A new ``Spec`` that is the union of this spec and ``spec_add``. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `spec_add` | `'Spec'` | — |

## Returns

`'Spec'`

## Calls

- `Spec` → `func:deepxube.logic.asp.Spec` (lines: 84)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.atoms_false`
- `self.atoms_true`
- `self.goal_false`
- `self.goal_true`
- `self.models_banned`

## Source

```python
    def add(self, spec_add: 'Spec') -> 'Spec':
        """ :return: A new ``Spec`` that is the union of this spec and ``spec_add``. """
        return Spec(goal_true=self.goal_true + spec_add.goal_true,
                    goal_false=self.goal_false + spec_add.goal_false,
                    atoms_true=self.atoms_true + spec_add.atoms_true,
                    atoms_false=self.atoms_false + spec_add.atoms_false,
                    models_banned=self.models_banned + spec_add.models_banned)
```
