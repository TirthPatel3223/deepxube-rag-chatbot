---
id: "class:deepxube.factories.heuristic_factory.PolicyNNetParFacClass"
kind: "class"
name: "PolicyNNetParFacClass"
qualified_name: "deepxube.factories.heuristic_factory.PolicyNNetParFacClass"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 165
line_end: 218
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "PolicyNNetPar"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.factories.heuristic_factory.PolicyNNetParFacClass.__init__"
  - "func:deepxube.factories.heuristic_factory.PolicyNNetParFacClass.get_nnet"
  - "func:deepxube.factories.heuristic_factory.PolicyNNetParFacClass._get_nnet_input"
  - "func:deepxube.factories.heuristic_factory.PolicyNNetParFacClass.__getstate__"
attributes:
  - name: "self.domain"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_input"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_input_name"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_kwargs"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.nnet_name"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.factories.heuristic_factory.PolicyNNetParFacClass`

**File:** [deepxube/factories/heuristic_factory.py:165](../../../deepxube/factories/heuristic_factory.py#L165)
**Abstract:** yes

## Docstring

Shared plumbing for factory-built ``PolicyNNetPar`` subclasses,
analogous to ``HeurNNetParFacClass`` but for policy networks.

## Inheritance

**Direct bases:**
- `PolicyNNetPar`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `get_nnet`
- `_get_nnet_input`
- `__getstate__` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.domain` | — | __init__ |
| `self.nnet_input` | — | __init__ |
| `self.nnet_input_name` | — | __init__ |
| `self.nnet_kwargs` | — | __init__ |
| `self.nnet_name` | — | __init__ |

## Source

```python
class PolicyNNetParFacClass(PolicyNNetPar, ABC):
    """ Shared plumbing for factory-built ``PolicyNNetPar`` subclasses,
    analogous to ``HeurNNetParFacClass`` but for policy networks.
    """

    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str, nnet_kwargs: Dict[str, Any], num_samp: int, num_rand: int):
        """ Store the domain, input key, and network parameters for later
        lazy construction.

        :param domain: The domain the policy operates on.
        :param nnet_input_name: ``(domain_name, nnet_input_name)`` key into
            the nnet-input registry; must resolve to a ``PolicyNNetIn``.
        :param nnet_name: Registration key of the policy network.
        :param nnet_kwargs: Keyword arguments for the network constructor.
        :param num_samp: Number of sampled actions per state for training.
        :param num_rand: Number of random actions mixed in.
        """
        super().__init__(num_samp, num_rand)
        self.domain: Domain = domain
        self.nnet_input_name: Tuple[str, str] = nnet_input_name
        self.nnet_input: Optional[PolicyNNetIn] = None
        self.nnet_name: str = nnet_name
        self.nnet_kwargs: Dict[str, Any] = nnet_kwargs

    def get_nnet(self) -> PolicyNNet:
        """ Construct the policy network, injecting the lazily-built
        ``PolicyNNetIn`` into the factory kwargs.

        :return: A freshly-constructed ``PolicyNNet``.
        """
        nnet_params: Dict = self.nnet_kwargs.copy()
        nnet_params['nnet_input'] = self._get_nnet_input()
        return policy_factory.build_class(self.nnet_name, nnet_params)

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

    def __getstate__(self) -> Dict:
        """ Drop ``self.nnet_input`` before pickling; see
        ``HeurNNetParFacClass.__getstate__``.

        :return: ``self.__dict__`` with ``nnet_input`` cleared.
        """
        self.nnet_input = None
        return self.__dict__
```
