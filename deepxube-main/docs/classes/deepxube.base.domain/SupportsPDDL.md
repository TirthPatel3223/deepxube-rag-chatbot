---
id: "class:deepxube.base.domain.SupportsPDDL"
kind: "class"
name: "SupportsPDDL"
qualified_name: "deepxube.base.domain.SupportsPDDL"
module: "deepxube.base.domain"
file: "deepxube/base/domain.py"
line_start: 612
line_end: 628
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Domain[S, A, G]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.domain.SupportsPDDL.get_pddl_domain"
  - "func:deepxube.base.domain.SupportsPDDL.prob_inst_to_pddl_inst"
  - "func:deepxube.base.domain.SupportsPDDL.pddl_action_to_action"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.domain.SupportsPDDL`

**File:** [deepxube/base/domain.py:612](../../../deepxube/base/domain.py#L612)
**Abstract:** yes

## Docstring

Mixin for domains that can describe themselves and their problem instances in PDDL. 

## Inheritance

**Direct bases:**
- `Domain[S, A, G]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `get_pddl_domain` *(trivial, skipped)*
- `prob_inst_to_pddl_inst` *(trivial, skipped)*
- `pddl_action_to_action` *(trivial, skipped)*

## Source

```python
class SupportsPDDL(Domain[S, A, G], ABC):
    """ Mixin for domains that can describe themselves and their problem instances in PDDL. """

    @abstractmethod
    def get_pddl_domain(self) -> List[str]:
        """ :return: PDDL domain text, line by line. """
        pass

    @abstractmethod
    def prob_inst_to_pddl_inst(self, state: S, goal: G) -> List[str]:
        """ :return: PDDL problem-instance text for the (state, goal) pair, line by line. """
        pass

    @abstractmethod
    def pddl_action_to_action(self, pddl_action: str) -> A:
        """ :return: ``A`` corresponding to the PDDL ground-action string. """
        pass
```
