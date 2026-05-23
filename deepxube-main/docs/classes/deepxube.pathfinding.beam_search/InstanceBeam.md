---
id: "class:deepxube.pathfinding.beam_search.InstanceBeam"
kind: "class"
name: "InstanceBeam"
qualified_name: "deepxube.pathfinding.beam_search.InstanceBeam"
module: "deepxube.pathfinding.beam_search"
file: "deepxube/pathfinding/beam_search.py"
line_start: 21
line_end: 86
is_abstract: true
is_dataclass: false
decorators: []
generic_parameters: []
bases:
  - name: "Instance"
    resolved_id: null
  - name: "ABC"
    resolved_id: null
methods:
  - "func:deepxube.pathfinding.beam_search.InstanceBeam.__init__"
  - "func:deepxube.pathfinding.beam_search.InstanceBeam.set_beam_size"
  - "func:deepxube.pathfinding.beam_search.InstanceBeam.set_temp"
  - "func:deepxube.pathfinding.beam_search.InstanceBeam.set_eps"
  - "func:deepxube.pathfinding.beam_search.InstanceBeam.frontier_size"
  - "func:deepxube.pathfinding.beam_search.InstanceBeam.record_goal"
  - "func:deepxube.pathfinding.beam_search.InstanceBeam.select_idxs_from_logits"
  - "func:deepxube.pathfinding.beam_search.InstanceBeam.finished"
attributes:
  - name: "self.beam_size"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.eps"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.temp"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.pathfinding.beam_search.InstanceBeam`

**File:** [deepxube/pathfinding/beam_search.py:21](../../../deepxube/pathfinding/beam_search.py#L21)
**Abstract:** yes

## Docstring

Per-instance beam-search state: beam size, sampling temperature, exploration epsilon, plus best-so-far goal tracking. 

## Inheritance

**Direct bases:**
- `Instance`
- `ABC`

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `set_beam_size` *(trivial, skipped)*
- `set_temp` *(trivial, skipped)*
- `set_eps` *(trivial, skipped)*
- `frontier_size` *(trivial, skipped)*
- `record_goal`
- `select_idxs_from_logits`
- `finished`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.beam_size` | — | __init__ |
| `self.eps` | — | __init__ |
| `self.temp` | — | __init__ |

## Source

```python
class InstanceBeam(Instance, ABC):
    """ Per-instance beam-search state: beam size, sampling temperature, exploration epsilon, plus best-so-far goal tracking. """

    def __init__(self, root_node: Node, inst_info: Any):
        """ Initialise with default beam_size=1, temp=0, eps=0. """
        super().__init__(root_node, inst_info)
        self.beam_size: int = 1
        self.temp: float = 0.0
        self.eps: float = 0.0

    def set_beam_size(self, beam_size: int) -> None:
        """ Set the per-step beam size (>= 1). """
        assert beam_size >= 1
        self.beam_size = beam_size

    def set_temp(self, temp: float) -> None:
        """ Set Boltzmann sampling temperature (0 = pure argmax top-k). """
        assert temp >= 0.0
        self.temp = temp

    def set_eps(self, eps: float) -> None:
        """ Set the per-pick random-replacement probability (epsilon in [0, 1]). """
        assert (eps >= 0.0) and (eps <= 1.0)
        self.eps = eps

    def frontier_size(self) -> int:
        """ :return: Current beam-frontier size. """
        return len(self._nodes_curr)

    def record_goal(self, nodes: List[Node]) -> None:
        """ Record the best (lowest-cost) solved node seen so far. """
        for node in nodes:
            assert node.is_solved is not None
            if node.is_solved:
                if (self.goal_node is None) or (self.goal_node.path_cost > node.path_cost):
                    self.goal_node = node

    def select_idxs_from_logits(self, logits: List[float]) -> List[int]:
        """ Pick ``beam_size`` indices greedily, by Boltzmann sampling, or with epsilon random replacement. """
        num_logits: int = len(logits)
        next_idxs: List[int]
        if len(logits) <= self.beam_size:
            next_idxs = list(range(num_logits))
        else:
            # get next idxs
            if self.temp == 0:
                next_idxs = (np.argpartition(logits, -self.beam_size)[-self.beam_size:]).tolist()
            else:
                # select next according to boltzmann
                probs: List[float] = boltzmann(logits, self.temp)
                next_idxs = np.random.choice(num_logits, size=self.beam_size, replace=False, p=probs).tolist()

            # randomly select index
            if self.eps > 0:
                replace_rand_idxs: List[int] = np.where(np.random.random(len(next_idxs)) < self.eps)[0].tolist()
                num_replace: int = len(replace_rand_idxs)
                if num_replace > 0:
                    next_idxs_rand: List[int] = np.random.choice(num_logits, replace=False, size=num_replace).tolist()
                    for replace_idx, next_idx_rand in zip(replace_rand_idxs, next_idxs_rand):
                        next_idxs[replace_idx] = next_idx_rand
                    next_idxs = list(set(next_idxs))
        return next_idxs

    def finished(self) -> bool:
        """ :return: True once a solved goal has been recorded. """
        return self.has_soln()
```
