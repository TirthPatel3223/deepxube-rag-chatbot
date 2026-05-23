---
id: "func:deepxube.factories.utils.import_modules.import_local_modules"
kind: "function"
name: "import_local_modules"
qualified_name: "deepxube.factories.utils.import_modules.import_local_modules"
module: "deepxube.factories.utils.import_modules"
file: "deepxube/factories/utils/import_modules.py"
line_start: 12
line_end: 35
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "root_dir"
    annotation: "str"
    default: null
  - name: "base_package"
    annotation: "str"
    default: "''"
returns: "None"
docstring_source: "present"
callees:
  - target: "func:os.walk"
    expr: "os.walk"
    call_sites: [26]
  - target: null
    expr: "file.endswith"
    call_sites: [28]
  - target: null
    expr: "file.startswith"
    call_sites: [28]
  - target: null
    expr: "os.path.join(root, file).replace('.py', '').replace"
    call_sites: [29]
  - target: null
    expr: "os.path.join(root, file).replace"
    call_sites: [29]
  - target: null
    expr: "os.path.join"
    call_sites: [29]
  - target: "func:importlib.import_module"
    expr: "import_module"
    call_sites: [33]
  - target: null
    expr: "print"
    call_sites: [35]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube.factories.utils.import_modules.import_local_modules`

**File:** [deepxube/factories/utils/import_modules.py:12](../../../../deepxube/factories/utils/import_modules.py#L12)
**Visibility:** public
**Kind:** function

## Signature

```python
def import_local_modules(root_dir: str, base_package: str = '') -> None
```

## Docstring

Recursively import every non-dunder ``.py`` file under ``root_dir``.

Designed to trigger factory-registration decorators in user-supplied
modules. Import errors are caught and logged to stdout rather than raised
so that one broken module does not prevent the rest from loading.

:param root_dir: Directory to walk. Every ``.py`` file whose name does
    not start with ``__`` is imported.
:param base_package: Optional dotted prefix prepended to each discovered
    module name (e.g. ``"mypkg"`` yields ``"mypkg.foo.bar"``). Empty by
    default, in which case the module path is derived directly from the
    file path.

## Parameters

| Name | Type | Default |
|------|------|---------|
| `root_dir` | `str` | — |
| `base_package` | `str` | `''` |

## Returns

`None`

## Calls

- `os.walk` → `func:os.walk` (lines: 26)
- `import_module` → `func:importlib.import_module` (lines: 33)

### Unresolved
- `file.endswith` (lines: 28)
- `file.startswith` (lines: 28)
- `os.path.join(root, file).replace('.py', '').replace` (lines: 29)
- `os.path.join(root, file).replace` (lines: 29)
- `os.path.join` (lines: 29)
- `print` (lines: 35)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def import_local_modules(root_dir: str, base_package: str = "") -> None:
    """ Recursively import every non-dunder ``.py`` file under ``root_dir``.

    Designed to trigger factory-registration decorators in user-supplied
    modules. Import errors are caught and logged to stdout rather than raised
    so that one broken module does not prevent the rest from loading.

    :param root_dir: Directory to walk. Every ``.py`` file whose name does
        not start with ``__`` is imported.
    :param base_package: Optional dotted prefix prepended to each discovered
        module name (e.g. ``"mypkg"`` yields ``"mypkg.foo.bar"``). Empty by
        default, in which case the module path is derived directly from the
        file path.
    """
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                module_name = os.path.join(root, file).replace('.py', '').replace('/', '.')
                if base_package:
                    module_name = base_package + '.' + module_name
                try:
                    import_module(module_name)
                except Exception as e:
                    print(f"Failed to import {module_name}: {e}")
```
