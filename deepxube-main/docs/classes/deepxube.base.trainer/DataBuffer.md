---
id: "class:deepxube.base.trainer.DataBuffer"
kind: "class"
name: "DataBuffer"
qualified_name: "deepxube.base.trainer.DataBuffer"
module: "deepxube.base.trainer"
file: "deepxube/base/trainer.py"
line_start: 62
line_end: 129
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.base.trainer.DataBuffer.__init__"
  - "func:deepxube.base.trainer.DataBuffer.add"
  - "func:deepxube.base.trainer.DataBuffer.sample"
  - "func:deepxube.base.trainer.DataBuffer.size"
  - "func:deepxube.base.trainer.DataBuffer.clear"
  - "func:deepxube.base.trainer.DataBuffer._add_circular"
attributes:
  - name: "self.add_idx"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.arrays"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.curr_size"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.max_size"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.trainer.DataBuffer`

**File:** [deepxube/base/trainer.py:62](../../../deepxube/base/trainer.py#L62)
**Abstract:** no

## Docstring

Fixed-size circular numpy buffer holding several aligned arrays. Used
to accumulate generated training data between updater rounds and sample
minibatches uniformly at random. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `add`
- `sample`
- `size` *(trivial, skipped)*
- `clear` *(trivial, skipped)*
- `_add_circular`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.add_idx` | — | __init__ |
| `self.arrays` | — | __init__ |
| `self.curr_size` | — | __init__ |
| `self.max_size` | — | __init__ |

## Source

```python
class DataBuffer:
    """ Fixed-size circular numpy buffer holding several aligned arrays. Used
    to accumulate generated training data between updater rounds and sample
    minibatches uniformly at random. """

    def __init__(self, max_size: int, shapes: List[Tuple[int, ...]], dtypes: List[np.dtype]):
        """ Pre-allocate one numpy array per (shape, dtype) at full ``max_size``.

        :param max_size: Capacity in rows.
        :param shapes: Shape (excluding leading row dim) for each parallel array.
        :param dtypes: Dtype for each parallel array.
        """
        self.arrays: List[NDArray] = []
        self.max_size: int = max_size
        self.curr_size: int = 0
        self.add_idx: int = 0

        # first add
        start_time = time.time()
        print(f"Initializing data buffer with max size {format(self.max_size, ',')}")
        print("Input array sizes:")
        for array_idx, (shape, dtype) in enumerate(zip(shapes, dtypes)):
            print(f"index: {array_idx}, dtype: {dtype}, shape:", shape)
            array: NDArray = np.empty((self.max_size,) + shape, dtype=dtype)
            self.arrays.append(array)

        print(f"Data buffer initialized. Time: {time.time() - start_time}")

    def add(self, arrays_add: List[NDArray]) -> None:
        """ Append the rows of ``arrays_add`` (parallel across all stored arrays) circularly. """
        self.curr_size = min(self.curr_size + arrays_add[0].shape[0], self.max_size)
        assert len(self.arrays) > 0, "Data buffer should have at least one array."
        self._add_circular(arrays_add)

    def sample(self, num: int) -> List[NDArray]:
        """ Uniformly sample ``num`` rows (with replacement) from every stored array. """
        sel_idxs: NDArray = np.random.randint(self.size(), size=num)

        arrays_samp: List[NDArray] = sel_l(self.arrays, sel_idxs)

        return arrays_samp

    def size(self) -> int:
        """ :return: Number of rows currently populated. """
        return self.curr_size

    def clear(self) -> None:
        """ Reset the buffer to empty without freeing storage. """
        self.curr_size = 0
        self.add_idx = 0

    def _add_circular(self, arrays_add: List[NDArray]) -> None:
        """ Wrap-around append into the pre-allocated arrays. """
        start_idx: int = 0
        num_add: int = arrays_add[0].shape[0]
        assert len(self.arrays) == len(arrays_add), "should have same number of arrays"
        while start_idx < num_add:
            num_add_i: int = min(num_add - start_idx, self.max_size - self.add_idx)
            end_idx: int = start_idx + num_add_i
            add_idx_end: int = self.add_idx + num_add_i

            for input_idx in range(len(self.arrays)):
                self.arrays[input_idx][self.add_idx:add_idx_end] = arrays_add[input_idx][start_idx:end_idx]

            start_idx = end_idx
            self.add_idx = add_idx_end
            if self.add_idx == self.max_size:
                self.add_idx = 0
```
