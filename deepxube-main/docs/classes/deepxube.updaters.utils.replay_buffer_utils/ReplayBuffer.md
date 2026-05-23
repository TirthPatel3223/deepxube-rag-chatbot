---
id: "class:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer"
kind: "class"
name: "ReplayBuffer"
qualified_name: "deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer"
module: "deepxube.updaters.utils.replay_buffer_utils"
file: "deepxube/updaters/utils/replay_buffer_utils.py"
line_start: 30
line_end: 87
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters:
  - "Elem"
  - "SampRet"
bases:
  - name: "Generic[Elem, SampRet]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.__init__"
  - "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.add"
  - "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.sample"
  - "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.size"
  - "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.max_size"
  - "func:deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer._elems_to_ret"
attributes:
  - name: "self.deque"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer`

**File:** [deepxube/updaters/utils/replay_buffer_utils.py:30](../../../deepxube/updaters/utils/replay_buffer_utils.py#L30)
**Abstract:** yes
**Generic parameters:** `Elem, SampRet`

## Docstring

Generic fixed-capacity replay buffer backed by a bounded deque with
uniform random sampling. Concrete subclasses differ only in the element
tuple shape and the unpacking done by ``_elems_to_ret``.

## Inheritance

**Direct bases:**
- `Generic[Elem, SampRet]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `add` *(trivial, skipped)*
- `sample`
- `size` *(trivial, skipped)*
- `max_size` *(trivial, skipped)*
- `_elems_to_ret` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.deque` | — | __init__ |

## Source

```python
class ReplayBuffer(Generic[Elem, SampRet], ABC):
    """ Generic fixed-capacity replay buffer backed by a bounded deque with
    uniform random sampling. Concrete subclasses differ only in the element
    tuple shape and the unpacking done by ``_elems_to_ret``.
    """

    def __init__(self, max_size: int):
        """ Create an empty buffer of the given capacity.

        :param max_size: Maximum number of elements; once exceeded, the
            oldest elements are dropped (``deque`` semantics).
        """
        self.deque: Deque[Elem] = deque([], max_size)

    def add(self, data: List[Elem]) -> None:
        """ Append a batch of elements, evicting oldest if full.

        :param data: List of new elements to push.
        """
        self.deque.extend(data)

    def sample(self, num: int) -> SampRet:
        """ Uniformly sample ``num`` elements (with replacement) and unpack
        them into per-field lists via ``_elems_to_ret``.

        :param num: Number of elements to sample.
        :return: A tuple of per-field lists, defined by the subclass.
        """
        assert self.size() > 0, f"Replay buffer size should not be {self.size()}"
        idxs: List[int] = np.random.randint(0, len(self.deque), size=num).tolist()
        elems: List[Elem] = [self.deque[idx] for idx in idxs]
        return self._elems_to_ret(elems)

    def size(self) -> int:
        """ Return the current number of elements in the buffer.

        :return: Number of elements currently stored.
        """
        return len(self.deque)

    def max_size(self) -> int:
        """ Return the configured capacity.

        :return: The ``max_size`` passed at construction.
        """
        maxlen: Optional[int] = self.deque.maxlen
        assert maxlen is not None

        return maxlen

    @abstractmethod
    def _elems_to_ret(self, elems: List[Elem]) -> SampRet:
        """ Unpack a list of element tuples into parallel per-field lists.

        :param elems: Sampled element tuples.
        :return: Per-field lists in the subclass's return format.
        """
        pass
```
