---
id: "func:deepxube.domains.lightsout.LightsOut.get_input_info_flat_sga"
kind: "method"
name: "get_input_info_flat_sga"
qualified_name: "deepxube.domains.lightsout.LightsOut.get_input_info_flat_sga"
module: "deepxube.domains.lightsout"
file: "deepxube/domains/lightsout.py"
line_start: 104
line_end: 106
class: "LightsOut"
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
  - target: "func:deepxube.domains.lightsout.LightsOut.get_num_acts"
    expr: "self.get_num_acts"
    call_sites: [106]
raises: []
reads_attrs:
  - "self.num_tiles"
writes_attrs: []
---

# `deepxube.domains.lightsout.LightsOut.get_input_info_flat_sga`

**File:** [deepxube/domains/lightsout.py:104](../../../../deepxube/domains/lightsout.py#L104)
**Class:** `LightsOut`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_input_info_flat_sga(self) -> Tuple[List[int], List[int]]
```

## Docstring

:return: Flat (state+goal+action) input descriptor for the NNet. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`Tuple[List[int], List[int]]`

## Calls

- `self.get_num_acts` → `func:deepxube.domains.lightsout.LightsOut.get_num_acts` (lines: 106)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.num_tiles`

## Source

```python
    def get_input_info_flat_sga(self) -> Tuple[List[int], List[int]]:
        """ :return: Flat (state+goal+action) input descriptor for the NNet. """
        return [self.num_tiles, 1], [1, self.get_num_acts()]
```
