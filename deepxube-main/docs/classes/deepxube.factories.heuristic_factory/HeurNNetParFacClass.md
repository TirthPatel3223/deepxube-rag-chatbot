---
id: "class:deepxube.factories.heuristic_factory.HeurNNetParFacClass"
kind: "class"
name: "HeurNNetParFacClass"
qualified_name: "deepxube.factories.heuristic_factory.HeurNNetParFacClass"
module: "deepxube.factories.heuristic_factory"
file: "deepxube/factories/heuristic_factory.py"
line_start: 99
line_end: 162
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "HeurNNetPar"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.factories.heuristic_factory.HeurNNetParFacClass.__init__"
  - "func:deepxube.factories.heuristic_factory.HeurNNetParFacClass.get_nnet"
  - "func:deepxube.factories.heuristic_factory.HeurNNetParFacClass._get_nnet_input"
  - "func:deepxube.factories.heuristic_factory.HeurNNetParFacClass.__getstate__"
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
  - name: "self.out_dim"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.q_fix"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.factories.heuristic_factory.HeurNNetParFacClass`

**File:** [deepxube/factories/heuristic_factory.py:99](../../../deepxube/factories/heuristic_factory.py#L99)
**Abstract:** yes

## Docstring

Shared plumbing for factory-built ``HeurNNetPar`` subclasses.

Holds the (domain, input-registry-key, network-name, kwargs, Q-fix flag,
output dim) needed to lazily construct both the ``NNetInput`` and the
heuristic network. Subclasses differ only in which ``StateGoalIn`` /
``StateGoalActFixIn`` / ``StateGoalActIn`` mixin the input must satisfy.

## Inheritance

**Direct bases:**
- `HeurNNetPar`
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
| `self.out_dim` | — | __init__ |
| `self.q_fix` | — | __init__ |

## Source

```python
class HeurNNetParFacClass(HeurNNetPar, ABC):
    """ Shared plumbing for factory-built ``HeurNNetPar`` subclasses.

    Holds the (domain, input-registry-key, network-name, kwargs, Q-fix flag,
    output dim) needed to lazily construct both the ``NNetInput`` and the
    heuristic network. Subclasses differ only in which ``StateGoalIn`` /
    ``StateGoalActFixIn`` / ``StateGoalActIn`` mixin the input must satisfy.
    """

    def __init__(self, domain: Domain, nnet_input_name: Tuple[str, str], nnet_name: str, nnet_kwargs: Dict[str, Any], q_fix: bool, out_dim: int):
        """ Store the domain, input key, and network parameters for later
        lazy construction.

        :param domain: The domain the input and network operate on.
        :param nnet_input_name: ``(domain_name, nnet_input_name)`` key into
            the nnet-input registry.
        :param nnet_name: Registration key of the heuristic network.
        :param nnet_kwargs: Keyword arguments for the network constructor.
        :param q_fix: ``True`` for a fixed-output-dim Q-network
            (one output per action).
        :param out_dim: Number of heuristic outputs (1 for V, ``num_acts``
            for fixed Q).
        """
        self.domain: Domain = domain
        self.nnet_input_name: Tuple[str, str] = nnet_input_name
        self.nnet_input: Optional[NNetInput] = None
        self.nnet_name: str = nnet_name
        self.nnet_kwargs: Dict[str, Any] = nnet_kwargs
        self.q_fix: bool = q_fix
        self.out_dim: int = out_dim

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

    def _get_nnet_input(self) -> NNetInput:
        """ Lazily build (once) and return the ``NNetInput`` instance for the
        stored ``nnet_input_name`` + domain.

        :return: The cached ``NNetInput`` instance.
        """
        if self.nnet_input is None:
            self.nnet_input = get_nnet_input_t(self.nnet_input_name)(domain=self.domain)
        return self.nnet_input

    def __getstate__(self) -> Dict:
        """ Drop ``self.nnet_input`` before pickling so worker processes
        rebuild it locally rather than sharing a (possibly unpicklable)
        cached one.

        :return: ``self.__dict__`` with ``nnet_input`` cleared.
        """
        self.nnet_input = None
        return self.__dict__
```
