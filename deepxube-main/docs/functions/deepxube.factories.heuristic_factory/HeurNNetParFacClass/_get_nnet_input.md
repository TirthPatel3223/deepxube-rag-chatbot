---
id: "func:deepxube.factories.heuristic_factory.HeurNNetParFacClass._get_nnet_input"
kind: "method"
name: "_get_nnet_input"
qualified_name: "deepxube.factories.heuristic_factory.HeurNNetParFacClass._get_nnet_input"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 144
line_end: 152
class: "HeurNNetParFacClass"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "NNetInput"
docstring_source: "present"
callees:
  - target: null
    expr: "get_nnet_input_t(self.nnet_input_name)"
    call_sites: [151]
  - target: "func:deepxube.factories.nnet_input_factory.get_nnet_input_t"
    expr: "get_nnet_input_t"
    call_sites: [151]
raises: []
reads_attrs:
  - "self.domain"
  - "self.nnet_input"
  - "self.nnet_input_name"
writes_attrs:
  - "self.nnet_input"
---

# `deepxube.factories.heuristic_factory.HeurNNetParFacClass._get_nnet_input`

**File:** [deepxube/factories/heuristic_factory.py:144](../../../../deepxube/factories/heuristic_factory.py#L144)
**Class:** `HeurNNetParFacClass`
**Visibility:** private
**Kind:** method

## Signature

```python
def _get_nnet_input(self) -> NNetInput
```

## Docstring

Lazily build (once) and return the ``NNetInput`` instance for the
stored ``nnet_input_name`` + domain.

:return: The cached ``NNetInput`` instance.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`NNetInput`

## Calls

- `get_nnet_input_t` → `func:deepxube.factories.nnet_input_factory.get_nnet_input_t` (lines: 151)

### Unresolved
- `get_nnet_input_t(self.nnet_input_name)` (lines: 151)

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
    def _get_nnet_input(self) -> NNetInput:
        """ Lazily build (once) and return the ``NNetInput`` instance for the
        stored ``nnet_input_name`` + domain.

        :return: The cached ``NNetInput`` instance.
        """
        if self.nnet_input is None:
            self.nnet_input = get_nnet_input_t(self.nnet_input_name)(domain=self.domain)
        return self.nnet_input
```
