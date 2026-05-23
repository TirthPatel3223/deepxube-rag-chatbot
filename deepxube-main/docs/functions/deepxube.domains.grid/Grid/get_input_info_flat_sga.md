---
id: "func:deepxube.domains.grid.Grid.get_input_info_flat_sga"
kind: "method"
name: "get_input_info_flat_sga"
qualified_name: "deepxube.domains.grid.Grid.get_input_info_flat_sga"
module: "deepxube.domains.grid"
file: "deepxube/domains/grid.py"
line_start: 110
line_end: 112
class: "Grid"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "Tuple[List[int], List[int]]"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.grid.Grid.get_num_acts"
    expr: "self.get_num_acts"
    call_sites: [112]
raises: []
reads_attrs:
  - "self.dim"
writes_attrs: []
---

# `deepxube.domains.grid.Grid.get_input_info_flat_sga`

**File:** [deepxube/domains/grid.py:110](../../../../deepxube/domains/grid.py#L110)
**Class:** `Grid`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_input_info_flat_sga(self) -> Tuple[List[int], List[int]]
```

## Docstring

:return: Flat (state+goal+action) input descriptor used by the NNet. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`Tuple[List[int], List[int]]`

## Calls

- `self.get_num_acts` → `func:deepxube.domains.grid.Grid.get_num_acts` (lines: 112)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.dim`

## Source

```python
    def get_input_info_flat_sga(self) -> Tuple[List[int], List[int]]:
        """ :return: Flat (state+goal+action) input descriptor used by the NNet. """
        return [4, 1], [self.dim, self.get_num_acts()]
```
