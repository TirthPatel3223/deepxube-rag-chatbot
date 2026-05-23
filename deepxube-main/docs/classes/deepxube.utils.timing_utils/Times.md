---
id: "class:deepxube.utils.timing_utils.Times"
kind: "class"
name: "Times"
qualified_name: "deepxube.utils.timing_utils.Times"
module: "deepxube.utils.timing_utils"
file: "deepxube/utils/timing_utils.py"
line_start: 64
line_end: 191
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.utils.timing_utils.Times.__init__"
  - "func:deepxube.utils.timing_utils.Times.record_time"
  - "func:deepxube.utils.timing_utils.Times.add_times"
  - "func:deepxube.utils.timing_utils.Times.reset_times"
  - "func:deepxube.utils.timing_utils.Times.get_total_time"
  - "func:deepxube.utils.timing_utils.Times.get_time_str"
  - "func:deepxube.utils.timing_utils.Times.__str__"
  - "func:deepxube.utils.timing_utils.Times.__repr__"
attributes:
  - name: "self.counts"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.sub_counts"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.sub_times"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.times"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.utils.timing_utils.Times`

**File:** [deepxube/utils/timing_utils.py:64](../../../deepxube/utils/timing_utils.py#L64)
**Abstract:** no

## Docstring

Hierarchical timer with named buckets and optional nested sub-timers.

Use ``record_time("name", dt)`` to accumulate elapsed seconds for a bucket,
or ``record_time("name", dt, path=["outer", "inner"])`` to push the entry
into a nested ``Times`` at that path. Merge per-process timers back into
a single one with ``add_times``.

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `record_time`
- `add_times`
- `reset_times`
- `get_total_time`
- `get_time_str`
- `__str__` *(trivial, skipped)* — *(no docstring)*
- `__repr__` *(trivial, skipped)* — *(no docstring)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.counts` | — | __init__ |
| `self.sub_counts` | — | __init__ |
| `self.sub_times` | — | __init__ |
| `self.times` | — | __init__ |

## Source

```python
class Times:
    """ Hierarchical timer with named buckets and optional nested sub-timers.

    Use ``record_time("name", dt)`` to accumulate elapsed seconds for a bucket,
    or ``record_time("name", dt, path=["outer", "inner"])`` to push the entry
    into a nested ``Times`` at that path. Merge per-process timers back into
    a single one with ``add_times``.
    """

    def __init__(self, time_names: Optional[List[str]] = None) -> None:
        """ Create a new ``Times`` with optional pre-declared bucket names.

        :param time_names: Names of buckets to start with at zero. If
            ``None``, buckets are created lazily on first ``record_time``.
        """
        if time_names is None:
            time_names = []

        self.times: OrderedDict[str, float] = init_times(time_names)
        self.counts: OrderedDict[str, int] = init_counts(time_names)

        self.sub_times: Dict[str, Times] = dict()
        self.sub_counts: Dict[str, int] = dict()

    def record_time(self, time_name: str, time_elapsed: float, path: Optional[List[str]] = None) -> None:
        """ Accumulate ``time_elapsed`` seconds into bucket ``time_name``.

        If ``path`` is given, the entry is recorded inside a nested
        ``Times`` at that path. Missing path segments are created. The
        ``path`` list is consumed (first element popped).

        :param time_name: Bucket name within the innermost ``Times``.
        :param time_elapsed: Seconds to add.
        :param path: Optional list of sub-timer names for nesting.
        """
        if (path is not None) and (len(path) > 0):
            path_0: str = path.pop(0)
            if path_0 not in self.sub_times:
                self.sub_times[path_0] = Times()
                self.sub_counts[path_0] = 0

            self.sub_times[path_0].record_time(time_name, time_elapsed, path=path)
            self.sub_counts[path_0] += 1
        else:
            if time_name not in self.times.keys():
                self.times[time_name] = 0
                self.counts[time_name] = 0

            self.times[time_name] += time_elapsed
            self.counts[time_name] += 1

    def add_times(self, time: 'Times', path: Optional[List[str]] = None) -> None:
        """ Merge another ``Times`` into this one, bucket-wise (and
        recursively across sub-timers).

        :param time: Source timer whose counts and times will be added in.
        :param path: Optional path under which to nest ``time``. Missing
            path segments are created. ``path`` is consumed.
        """
        if (path is not None) and (len(path) > 0):
            path_0: str = path.pop(0)
            if path_0 not in self.sub_times:
                self.sub_times[path_0] = Times()
                self.sub_counts[path_0] = 0
            self.sub_times[path_0].add_times(time, path=path)
            self.sub_counts[path_0] += sum(time.counts.values())
        else:
            add_times(self.times, time.times)
            add_counts(self.counts, time.counts)
            for sub_time_name in time.sub_times.keys():
                if sub_time_name not in self.sub_times.keys():
                    self.sub_times[sub_time_name] = Times()
                    self.sub_counts[sub_time_name] = 0

                self.sub_times[sub_time_name].add_times(time.sub_times[sub_time_name])
                self.sub_counts[sub_time_name] += sum(time.sub_times[sub_time_name].counts.values())

    def reset_times(self) -> None:
        """ Zero every bucket and count, recursively across all sub-timers.
        Existing bucket names are retained.
        """
        for key in self.times.keys():
            self.times[key] = 0.0
            self.counts[key] = 0

        for sub_time in self.sub_times.values():
            sub_time.reset_times()

    def get_total_time(self) -> float:
        """ Return the sum of every bucket in this timer and all sub-timers.

        :return: Total accumulated seconds.
        """
        time_tot: float = 0.0
        for time_elapsed in self.times.values():
            time_tot += time_elapsed

        for sub_time in self.sub_times.values():
            time_tot += sub_time.get_total_time()

        return time_tot

    def get_time_str(self, prefix: str = "", decplace: int = 2) -> str:
        """ Format every bucket and sub-timer into a single human-readable
        multi-line string.

        :param prefix: String prepended to each nested line (used internally
            for recursive indentation).
        :param decplace: Number of decimal places to render.
        :return: A multi-line string listing per-bucket times and a total.
        """
        time_str_l: List[str] = [f"{key}: {val:.{decplace}f}" for key, val in self.times.items()]
        sub_time_str_l: List[str] = [f"->{key}: {sub_time.get_total_time():.{decplace}f}"
                                     for key, sub_time in self.sub_times.items()]

        time_str: str = ", ".join(time_str_l + sub_time_str_l + [f"Tot: {self.get_total_time():.{decplace}f}"])

        prefix_new: str = f"\t{prefix}"
        for key, sub_time in self.sub_times.items():
            time_str = f"{time_str}\n{prefix_new}({key}): {sub_time.get_time_str(prefix=prefix_new)}"

        return time_str

    def __str__(self) -> str:
        return self.get_time_str()

    def __repr__(self) -> str:
        return self.__str__()
```
