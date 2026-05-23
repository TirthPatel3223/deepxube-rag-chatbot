---
id: "func:deepxube.factories.heuristic_factory.HeurNNetParFacClass.get_nnet"
kind: "method"
name: "get_nnet"
qualified_name: "deepxube.factories.heuristic_factory.HeurNNetParFacClass.get_nnet"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 130
line_end: 142
class: "HeurNNetParFacClass"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "HeurNNet"
docstring_source: "present"
callees:
  - target: null
    expr: "self.nnet_kwargs.copy"
    call_sites: [138]
  - target: "func:deepxube.factories.heuristic_factory.HeurNNetParFacClass._get_nnet_input"
    expr: "self._get_nnet_input"
    call_sites: [139]
  - target: "func:deepxube.factories.heuristic_factory.build_class"
    expr: "heuristic_factory.build_class"
    call_sites: [142]
raises: []
reads_attrs:
  - "self.nnet_kwargs"
  - "self.nnet_name"
  - "self.out_dim"
  - "self.q_fix"
writes_attrs: []
---

# `deepxube.factories.heuristic_factory.HeurNNetParFacClass.get_nnet`

**File:** [deepxube/factories/heuristic_factory.py:130](../../../../deepxube/factories/heuristic_factory.py#L130)
**Class:** `HeurNNetParFacClass`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_nnet(self) -> HeurNNet
```

## Docstring

Construct the heuristic network, injecting the lazily-built
``NNetInput`` plus the Q-fix flag and output dimension into the
factory kwargs.

:return: A freshly-constructed ``HeurNNet`` ready for training
    or inference.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`HeurNNet`

## Calls

- `self._get_nnet_input` → `func:deepxube.factories.heuristic_factory.HeurNNetParFacClass._get_nnet_input` (lines: 139)
- `heuristic_factory.build_class` → `func:deepxube.factories.heuristic_factory.build_class` (lines: 142)

### Unresolved
- `self.nnet_kwargs.copy` (lines: 138)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.nnet_kwargs`
- `self.nnet_name`
- `self.out_dim`
- `self.q_fix`

## Source

```python
    def get_nnet(self) -> HeurNNet:
        """ Construct the heuristic network, injecting the lazily-built
        ``NNetInput`` plus the Q-fix flag and output dimension into the
        factory kwargs.

        :return: A freshly-constructed ``HeurNNet`` ready for training
            or inference.
        """
        nnet_params: Dict = self.nnet_kwargs.copy()
        nnet_params['nnet_input'] = self._get_nnet_input()
        nnet_params['q_fix'] = self.q_fix
        nnet_params['out_dim'] = self.out_dim
        return heuristic_factory.build_class(self.nnet_name, nnet_params)
```
