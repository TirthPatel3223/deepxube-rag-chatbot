---
id: "func:deepxube.factories.heuristic_factory.PolicyNNetParFacClass.get_nnet"
kind: "method"
name: "get_nnet"
qualified_name: "deepxube.factories.heuristic_factory.PolicyNNetParFacClass.get_nnet"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 189
line_end: 197
class: "PolicyNNetParFacClass"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "PolicyNNet"
docstring_source: "present"
callees:
  - target: null
    expr: "self.nnet_kwargs.copy"
    call_sites: [195]
  - target: "func:deepxube.factories.heuristic_factory.PolicyNNetParFacClass._get_nnet_input"
    expr: "self._get_nnet_input"
    call_sites: [196]
  - target: null
    expr: "policy_factory.build_class"
    call_sites: [197]
raises: []
reads_attrs:
  - "self.nnet_kwargs"
  - "self.nnet_name"
writes_attrs: []
---

# `deepxube.factories.heuristic_factory.PolicyNNetParFacClass.get_nnet`

**File:** [deepxube/factories/heuristic_factory.py:189](../../../../deepxube/factories/heuristic_factory.py#L189)
**Class:** `PolicyNNetParFacClass`
**Visibility:** public
**Kind:** method

## Signature

```python
def get_nnet(self) -> PolicyNNet
```

## Docstring

Construct the policy network, injecting the lazily-built
``PolicyNNetIn`` into the factory kwargs.

:return: A freshly-constructed ``PolicyNNet``.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`PolicyNNet`

## Calls

- `self._get_nnet_input` → `func:deepxube.factories.heuristic_factory.PolicyNNetParFacClass._get_nnet_input` (lines: 196)

### Unresolved
- `self.nnet_kwargs.copy` (lines: 195)
- `policy_factory.build_class` (lines: 197)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.nnet_kwargs`
- `self.nnet_name`

## Source

```python
    def get_nnet(self) -> PolicyNNet:
        """ Construct the policy network, injecting the lazily-built
        ``PolicyNNetIn`` into the factory kwargs.

        :return: A freshly-constructed ``PolicyNNet``.
        """
        nnet_params: Dict = self.nnet_kwargs.copy()
        nnet_params['nnet_input'] = self._get_nnet_input()
        return policy_factory.build_class(self.nnet_name, nnet_params)
```
