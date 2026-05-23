---
id: "func:deepxube.domains.cube3.Cube3.get_input_info_flat_sga"
kind: "method"
name: "get_input_info_flat_sga"
qualified_name: "deepxube.domains.cube3.Cube3.get_input_info_flat_sga"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 561
line_end: 563
class: "Cube3"
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
  - target: "func:deepxube.domains.cube3.Cube3.get_num_acts"
    expr: "self.get_num_acts"
    call_sites: [563]
raises: []
reads_attrs:
  - "self.num_colors"
  - "self.num_stickers"
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3.get_input_info_flat_sga`

**File:** [deepxube/domains/cube3.py:561](../../../../deepxube/domains/cube3.py#L561)
**Class:** `Cube3`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_input_info_flat_sga(self) -> Tuple[List[int], List[int]]
```

## Docstring

:return: Flat (state+goal+action) input descriptor. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`Tuple[List[int], List[int]]`

## Calls

- `self.get_num_acts` → `func:deepxube.domains.cube3.Cube3.get_num_acts` (lines: 563)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.num_colors`
- `self.num_stickers`

## Source

```python
    def get_input_info_flat_sga(self) -> Tuple[List[int], List[int]]:
        """ :return: Flat (state+goal+action) input descriptor. """
        return [self.num_stickers, 1], [self.num_colors, self.get_num_acts()]
```
