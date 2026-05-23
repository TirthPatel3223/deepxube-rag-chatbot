---
id: "class:deepxube.utils.data_utils.Logger"
kind: "class"
name: "Logger"
qualified_name: "deepxube.utils.data_utils.Logger"
module: "deepxube.utils.data_utils"
file: "deepxube/utils/data_utils.py"
line_start: 23
line_end: 58
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "object"
    resolved_id: null
methods:
  - "func:deepxube.utils.data_utils.Logger.__init__"
  - "func:deepxube.utils.data_utils.Logger.write"
  - "func:deepxube.utils.data_utils.Logger.flush"
attributes:
  - name: "self.echo"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.log"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.terminal"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.utils.data_utils.Logger`

**File:** [deepxube/utils/data_utils.py:23](../../../deepxube/utils/data_utils.py#L23)
**Abstract:** no

## Docstring

Stdout-compatible file logger that tees writes to both a file and
(optionally) the real terminal.

Instantiate and assign to ``sys.stdout`` to capture all prints to a log
file while still showing them on screen.

## Inheritance

**Direct bases:**
- `object`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*
- `write`
- `flush` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.echo` | — | __init__ |
| `self.log` | — | __init__ |
| `self.terminal` | — | __init__ |

## Source

```python
class Logger(object):
    """ Stdout-compatible file logger that tees writes to both a file and
    (optionally) the real terminal.

    Instantiate and assign to ``sys.stdout`` to capture all prints to a log
    file while still showing them on screen.
    """

    def __init__(self, filename: str, mode: str = "a", echo: bool = True):
        """ Open the log file and snapshot the current stdout.

        :param filename: Path to the log file.
        :param mode: ``open()`` mode; ``"a"`` appends, ``"w"`` overwrites.
        :param echo: If ``True`` (default) writes also go to the original
            stdout; if ``False`` they go only to the file.
        """
        self.terminal = sys.stdout
        self.log = open(filename, mode)
        self.echo: bool = echo

    def write(self, message: str) -> None:
        """ Write ``message`` to the log file (and to the terminal if
        ``echo`` is ``True``), flushing the file afterwards.

        :param message: String to write.
        """
        if self.echo:
            self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

    def flush(self) -> None:
        """ No-op; stdout file objects must define ``flush``, but this
        logger flushes on every ``write``.
        """
        pass
```
