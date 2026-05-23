---
id: "func:deepxube.base.trainer.DataBuffer.sample"
kind: "method"
name: "sample"
qualified_name: "deepxube.base.trainer.DataBuffer.sample"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 96
line_end: 102
class: "DataBuffer"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "num"
    annotation: "int"
    default: null
returns: "List[NDArray]"
docstring_source: "present"
callees:
  - target: null
    expr: "np.random.randint"
    call_sites: [98]
  - target: "func:deepxube.base.trainer.DataBuffer.size"
    expr: "self.size"
    call_sites: [98]
  - target: "func:deepxube.utils.data_utils.sel_l"
    expr: "sel_l"
    call_sites: [100]
raises: []
reads_attrs:
  - "self.arrays"
writes_attrs: []
---

# `deepxube.base.trainer.DataBuffer.sample`

**File:** [deepxube/base/trainer.py:96](../../../../deepxube/base/trainer.py#L96)
**Class:** `DataBuffer`
**Visibility:** public
**Kind:** method

## Signature

```python
def sample(self, num: int) -> List[NDArray]
```

## Docstring

Uniformly sample ``num`` rows (with replacement) from every stored array. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `num` | `int` | — |

## Returns

`List[NDArray]`

## Calls

- `self.size` → `func:deepxube.base.trainer.DataBuffer.size` (lines: 98)
- `sel_l` → `func:deepxube.utils.data_utils.sel_l` (lines: 100)

### Unresolved
- `np.random.randint` (lines: 98)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.arrays`

## Source

```python
    def sample(self, num: int) -> List[NDArray]:
        """ Uniformly sample ``num`` rows (with replacement) from every stored array. """
        sel_idxs: NDArray = np.random.randint(self.size(), size=num)

        arrays_samp: List[NDArray] = sel_l(self.arrays, sel_idxs)

        return arrays_samp
```
