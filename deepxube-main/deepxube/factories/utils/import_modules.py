""" Helper to import every Python module under a directory tree so that
side-effect registrations (``@factory.register_class``) fire.

Used by the CLI at startup to pick up user-defined ``domains/``,
``heuristics/``, and nnet inputs without requiring an explicit import list.
"""

from importlib import import_module
import os


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
