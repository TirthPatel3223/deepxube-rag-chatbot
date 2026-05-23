---
id: "class:deepxube.pathfinding.beam_search.BeamSearchParser"
kind: "class"
name: "BeamSearchParser"
qualified_name: "deepxube.pathfinding.beam_search.BeamSearchParser"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 300
line_end: 329
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
  - "func:deepxube.pathfinding.beam_search.BeamSearchParser.parse"
  - "func:deepxube.pathfinding.beam_search.BeamSearchParser.help"
  - "func:deepxube.pathfinding.beam_search.BeamSearchParser._alg_name"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.BeamSearchParser`

**File:** [deepxube/pathfinding/beam_search.py:300](../../../deepxube/pathfinding/beam_search.py#L300)
**Abstract:** yes

## Docstring

Abstract CLI parser for all beam-search variants; parses ``<n>B_<f>T_<f>E`` arg strings. 

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
class BeamSearchParser(Parser, ABC):
    """ Abstract CLI parser for all beam-search variants; parses ``<n>B_<f>T_<f>E`` arg strings. """

    def parse(self, args_str: str) -> Dict[str, Any]:
        """ Parse an underscore-separated arg string into ``beam_size``, ``temp``, and/or ``eps`` kwargs. """
        args_str_l: List[str] = args_str.split("_")
        kwargs: Dict[str, Any] = dict()
        for args_str_i in args_str_l:
            beam_re = re.search(r"^(\S+)B$", args_str_i)
            temp_re = re.search(r"^(\S+)T", args_str_i)
            eps_re = re.search(r"^(\S+)E", args_str_i)
            if beam_re is not None:
                kwargs["beam_size"] = int(beam_re.group(1))
            elif temp_re is not None:
                kwargs["temp"] = float(temp_re.group(1))
            elif eps_re is not None:
                kwargs["eps"] = float(eps_re.group(1))
            else:
                raise ValueError(f"Unexpected argument {args_str_i!r}")
        return kwargs

    def help(self) -> str:
        """ :return: CLI usage string describing ``B``/``T``/``E`` suffixes with an example. """
        return ("<int>B (beam size), <float>T (temperature for Boltzmann distribution), <float>E (epsilon for chance to randomly select node).\n"
                f"E.g. {self._alg_name()}.10B_1.0T_0.1E")

    @abstractmethod
    def _alg_name(self) -> str:
        """ :return: The algorithm key (e.g. ``beam_v``) used in CLI help examples. """
        pass
```
