---
id: "class:deepxube.pathfinding.graph_search.GraphSearchParser"
kind: "class"
name: "GraphSearchParser"
qualified_name: "deepxube.pathfinding.graph_search.GraphSearchParser"
module: "deepxube.pathfinding.graph_search"
file: "deepxube/pathfinding/graph_search.py"
line_start: 287
line_end: 316
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Parser"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.graph_search.GraphSearchParser.parse"
  - "func:deepxube.pathfinding.graph_search.GraphSearchParser.help"
  - "func:deepxube.pathfinding.graph_search.GraphSearchParser._alg_name"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.graph_search.GraphSearchParser`

**File:** [deepxube/pathfinding/graph_search.py:287](../../../deepxube/pathfinding/graph_search.py#L287)
**Abstract:** yes

## Docstring

Abstract CLI parser for all graph-search variants; parses ``<n>B_<f>W_<f>E`` arg strings. 

## Inheritance

**Direct bases:**
- `Parser`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `parse`
- `help`
- `_alg_name` *(trivial, skipped)*

## Source

```python
class GraphSearchParser(Parser, ABC):
    """ Abstract CLI parser for all graph-search variants; parses ``<n>B_<f>W_<f>E`` arg strings. """

    def parse(self, args_str: str) -> Dict[str, Any]:
        """ Parse an underscore-separated arg string into ``batch_size``, ``weight``, and/or ``eps`` kwargs. """
        args_str_l: List[str] = args_str.split("_")
        kwargs: Dict[str, Any] = dict()
        for args_str_i in args_str_l:
            batch_size_re = re.search(r"^(\S+)B$", args_str_i)
            weight_re = re.search(r"^(\S+)W", args_str_i)
            eps_re = re.search(r"^(\S+)E", args_str_i)
            if batch_size_re is not None:
                kwargs["batch_size"] = int(batch_size_re.group(1))
            elif weight_re is not None:
                kwargs["weight"] = float(weight_re.group(1))
            elif eps_re is not None:
                kwargs["eps"] = float(eps_re.group(1))
            else:
                raise ValueError(f"Unexpected argument {args_str_i!r}")
        return kwargs

    def help(self) -> str:
        """ :return: CLI usage string describing ``B``/``W``/``E`` suffixes with an example. """
        return ("<int>B (batch size), <float>W (weight), <float>E (epsilon for chance to randomly pop node).\n"
                f"E.g. {self._alg_name()}.10B_0.5W_0.1E")

    @abstractmethod
    def _alg_name(self) -> str:
        """ :return: The algorithm key (e.g. ``graph_v``) used in CLI help examples. """
        pass
```
