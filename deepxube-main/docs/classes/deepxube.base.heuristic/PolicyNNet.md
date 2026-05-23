---
id: "class:deepxube.base.heuristic.PolicyNNet"
kind: "class"
name: "PolicyNNet"
qualified_name: "deepxube.base.heuristic.PolicyNNet"
module: "deepxube.base.heuristic"
file: "deepxube/base/heuristic.py"
line_start: 100
line_end: 120
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "DeepXubeNNet[PNNetIn]"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.base.heuristic.PolicyNNet.forward"
  - "func:deepxube.base.heuristic.PolicyNNet.train_fprop"
attributes: []
factory_registrations: []
docstring_source: "present"
---

# `deepxube.base.heuristic.PolicyNNet`

**File:** [deepxube/base/heuristic.py:100](../../../deepxube/base/heuristic.py#L100)
**Abstract:** yes

## Docstring

Policy network base. ``forward`` produces sampled actions plus their density;
``train_fprop`` produces the loss given (state, goal, action) triples. 

## Inheritance

**Direct bases:**
- `DeepXubeNNet[PNNetIn]`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `forward` *(trivial, skipped)*
- `train_fprop` *(trivial, skipped)*

## Source

```python
class PolicyNNet(DeepXubeNNet[PNNetIn], ABC):
    """ Policy network base. ``forward`` produces sampled actions plus their density;
    ``train_fprop`` produces the loss given (state, goal, action) triples. """

    @abstractmethod
    def forward(self, states_goals: List[Tensor]) -> List[Tensor]:
        """ Condition on states and goals to sample actions

        :param states_goals:
        :return: List of tensors representing actions with the last Tensor representing the probability density of actions
        """
        pass

    @abstractmethod
    def train_fprop(self, states_goals_actions: List[Tensor]) -> Tuple[Tensor, str]:
        """

        :param states_goals_actions:
        :return: loss, info to print
        """
        pass
```
