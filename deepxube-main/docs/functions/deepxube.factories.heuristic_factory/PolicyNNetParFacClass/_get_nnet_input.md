---
id: "func:deepxube.factories.heuristic_factory.PolicyNNetParFacClass._get_nnet_input"
kind: "method"
name: "_get_nnet_input"
qualified_name: "deepxube.factories.heuristic_factory.PolicyNNetParFacClass._get_nnet_input"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 199
line_end: 209
class: "PolicyNNetParFacClass"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "PolicyNNetIn"
docstring_source: "present"
callees:
  - target: null
    expr: "get_nnet_input_t(self.nnet_input_name)"
    call_sites: [206]
  - target: "func:deepxube.factories.nnet_input_factory.get_nnet_input_t"
    expr: "get_nnet_input_t"
    call_sites: [206]
  - target: null
    expr: "isinstance"
    call_sites: [207]
raises: []
reads_attrs:
  - "self.domain"
  - "self.nnet_input"
  - "self.nnet_input_name"
writes_attrs:
  - "self.nnet_input"
---

# `deepxube.factories.heuristic_factory.PolicyNNetParFacClass._get_nnet_input`

**File:** [deepxube/factories/heuristic_factory.py:199](../../../../deepxube/factories/heuristic_factory.py#L199)
**Class:** `PolicyNNetParFacClass`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_nnet_input(self) -> PolicyNNetIn
```

## Docstring

Lazily build (once) the ``PolicyNNetIn`` instance, asserting that
the registered class implements the ``PolicyNNetIn`` mixin.

:return: The cached ``PolicyNNetIn`` instance.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`PolicyNNetIn`

## Calls

- `get_nnet_input_t` → `func:deepxube.factories.nnet_input_factory.get_nnet_input_t` (lines: 206)

### Unresolved
- `get_nnet_input_t(self.nnet_input_name)` (lines: 206)
- `isinstance` (lines: 207)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.nnet_input`

**Reads:**
- `self.domain`
- `self.nnet_input`
- `self.nnet_input_name`

## Source

```python
    def _get_nnet_input(self) -> PolicyNNetIn:
        """ Lazily build (once) the ``PolicyNNetIn`` instance, asserting that
        the registered class implements the ``PolicyNNetIn`` mixin.

        :return: The cached ``PolicyNNetIn`` instance.
        """
        if self.nnet_input is None:
            nnet_input: NNetInput = get_nnet_input_t(self.nnet_input_name)(domain=self.domain)
            assert isinstance(nnet_input, PolicyNNetIn)
            self.nnet_input = nnet_input
        return self.nnet_input
```
