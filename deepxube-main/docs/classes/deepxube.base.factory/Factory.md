---
id: "class:deepxube.base.factory.Factory"
kind: "class"
name: "Factory"
qualified_name: "deepxube.base.factory.Factory"
module: "deepxube.base.factory"
file: "deepxube/base/factory.py"
line_start: 55
line_end: 179
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters:
  - "T"
bases:
  - name: "Generic[T]"
    resolved_id: null
methods:
  - "func:deepxube.base.factory.Factory.__init__"
  - "func:deepxube.base.factory.Factory.register_class"
  - "func:deepxube.base.factory.Factory.register_parser"
  - "func:deepxube.base.factory.Factory.get_parser"
  - "func:deepxube.base.factory.Factory.get_kwargs"
  - "func:deepxube.base.factory.Factory.get_type"
  - "func:deepxube.base.factory.Factory.build_class"
  - "func:deepxube.base.factory.Factory.get_all_class_names"
attributes:
  - name: "self._class_registry"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._class_type_str"
    annotation: null
    default: null
    from: "__init__"
  - name: "self._parser_registry"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.factory.Factory`

**File:** [deepxube/base/factory.py:55](../../../deepxube/base/factory.py#L55)
**Abstract:** no
**Generic parameters:** `T`

## Docstring

Registry of named classes (and optional parsers) for a single family.

One ``Factory`` instance is created per family (domain, heuristic,
pathfinding, updater, etc.). Classes register themselves with the factory
via the ``@factory.register_class("name")`` decorator, typically at module
import time. Optional ``@factory.register_parser("name")`` decorators hook
up a ``Parser`` for the class so CLI argument strings can be resolved into
constructor kwargs.

## Inheritance

**Direct bases:**
- `Generic[T]`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__` *(trivial, skipped)*
- `register_class`
- `register_parser`
- `get_parser`
- `get_kwargs`
- `get_type`
- `build_class`
- `get_all_class_names` *(trivial, skipped)*

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self._class_registry` | — | __init__ |
| `self._class_type_str` | — | __init__ |
| `self._parser_registry` | — | __init__ |

## Source

```python
class Factory(Generic[T]):
    """ Registry of named classes (and optional parsers) for a single family.

    One ``Factory`` instance is created per family (domain, heuristic,
    pathfinding, updater, etc.). Classes register themselves with the factory
    via the ``@factory.register_class("name")`` decorator, typically at module
    import time. Optional ``@factory.register_parser("name")`` decorators hook
    up a ``Parser`` for the class so CLI argument strings can be resolved into
    constructor kwargs.
    """

    def __init__(self, class_type_str: str):
        """ Create a new factory for a given class family.

        :param class_type_str: Short human-readable label for the registered
            class family (e.g. ``"Domain"``, ``"Update"``). Used in error
            messages to identify which registry failed lookup.
        """
        self._class_registry: Dict[str, Type[T]] = dict()
        self._parser_registry: Dict[str, Type[Parser]] = dict()
        self._class_type_str: str = class_type_str

    def register_class(self, name: str) -> Callable[[Type[T]], Type[T]]:
        """ Return a decorator that registers a class under ``name``.

        :param name: Unique string key under which to register the class.
            Registering the same name twice raises ``ValueError``.
        :return: A decorator that records the class in this factory's class
            registry and returns the class unchanged.
        """
        def deco(cls: Type[T]) -> Type[T]:
            if name in self._class_registry.keys():
                raise ValueError(f"{self._class_type_str.capitalize()} {name!r} already registered")
            self._class_registry[name] = cls
            return cls
        return deco

    def register_parser(self, name: str) -> Callable[[Type[Parser]], Type[Parser]]:
        """ Return a decorator that registers a ``Parser`` subclass under ``name``.

        The ``name`` must match the name used when registering the corresponding
        class, so ``get_kwargs`` can find both in tandem.

        :param name: Unique string key matching a registered class.
            Registering the same name twice raises ``ValueError``.
        :return: A decorator that records the parser in this factory's parser
            registry and returns the parser class unchanged.
        """
        def deco(cls: Type[Parser]) -> Type[Parser]:
            if name in self._parser_registry.keys():
                raise ValueError(f"{self._class_type_str.capitalize()} parser {name!r} already registered")
            self._parser_registry[name] = cls
            return cls
        return deco

    def get_parser(self, name: str) -> Optional[Parser]:
        """ Return a fresh instance of the ``Parser`` registered under ``name``.

        :param name: The registered class name.
        :return: A new ``Parser`` instance, or ``None`` if no parser is
            registered for that name.
        """
        cls_parser: Optional[Type[Parser]] = self._parser_registry.get(name)
        if cls_parser is not None:
            return cls_parser()
        else:
            return None

    def get_kwargs(self, name: str, args_str: Optional[str]) -> Dict[str, Any]:
        """ Resolve a CLI argument suffix into constructor keyword arguments.

        Asserts that the class ``name`` is registered, then routes ``args_str``
        through the corresponding parser if one exists. If no parser is
        registered for ``name``, ``args_str`` must be ``None``.

        :param name: The registered class name.
        :param args_str: The dotted argument suffix following ``name``
            (e.g. ``"7"`` in ``grid.7``), or ``None`` if the argument had no
            suffix.
        :return: A dictionary of keyword arguments for the class constructor.
            Empty if no parser exists or ``args_str`` is ``None``.
        """
        self.get_type(name)
        kwargs: Dict[str, Any] = dict()
        parser: Optional[Parser] = self.get_parser(name)
        if (parser is not None) and (args_str is not None):
            try:
                kwargs = parser.parse(args_str)
            except Exception as e:
                logging.exception(f"Error occurred: {e}")
                raise ValueError(f"Error parsing {args_str} for {self._class_type_str} {name!r}.\nParser help:\n{parser.help()}")
        else:
            assert args_str is None, f"No parser for {self._class_type_str} {name}, however, args given are {args_str}"
        return kwargs

    def get_type(self, name: str) -> Type[T]:
        """ Return the class registered under ``name``.

        :param name: The registered class name.
        :return: The concrete class type.
        :raises ValueError: If no class is registered under ``name``; the error
            message lists the available names.
        """
        try:
            return self._class_registry[name]
        except KeyError:
            raise ValueError(f"Unknown {self._class_type_str} {name!r}. Available: {sorted(self._class_registry)}")

    def build_class(self, name: str, kwargs: Dict[str, Any]) -> T:
        """ Look up the class registered under ``name`` and instantiate it.

        :param name: The registered class name.
        :param kwargs: Keyword arguments to pass to the class constructor,
            typically produced by ``get_kwargs``.
        :return: A newly-constructed instance of the registered class.
        """
        cls: Type[T] = self.get_type(name)
        return cls(**kwargs)

    def get_all_class_names(self) -> List[str]:
        """ Return the list of all class names registered with this factory.

        :return: A list of every registered class name, in insertion order.
        """
        return list(self._class_registry.keys())
```
