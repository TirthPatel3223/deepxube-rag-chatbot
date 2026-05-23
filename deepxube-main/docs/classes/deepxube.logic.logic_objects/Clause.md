---
id: "class:deepxube.logic.logic_objects.Clause"
kind: "class"
name: "Clause"
qualified_name: "deepxube.logic.logic_objects.Clause"
module: "deepxube.logic.logic_objects"
file: "deepxube/logic/logic_objects.py"
line_start: 97
line_end: 290
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.logic.logic_objects.Clause.__init__"
  - "func:deepxube.logic.logic_objects.Clause.is_in_out_consistent_body"
  - "func:deepxube.logic.logic_objects.Clause.can_ground"
  - "func:deepxube.logic.logic_objects.Clause.to_code"
  - "func:deepxube.logic.logic_objects.Clause.get_lit_id_count_dict"
  - "func:deepxube.logic.logic_objects.Clause.theta_sub"
  - "func:deepxube.logic.logic_objects.Clause.__str__"
  - "func:deepxube.logic.logic_objects.Clause.__repr__"
  - "func:deepxube.logic.logic_objects.Clause.__hash__"
  - "func:deepxube.logic.logic_objects.Clause.__eq__"
attributes:
  - name: "self.all_vars"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.body"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.hash"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.head"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.logic.logic_objects.Clause`

**File:** [deepxube/logic/logic_objects.py:97](../../../deepxube/logic/logic_objects.py#L97)
**Abstract:** no

## Docstring

A definite clause (head :- body); supports theta-subsumption-based equality via a WL graph hash. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `is_in_out_consistent_body`
- `can_ground`
- `to_code`
- `get_lit_id_count_dict`
- `theta_sub`
- `__str__`
- `__repr__` *(trivial, skipped)* — *(no docstring)*
- `__hash__`
- `__eq__`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.all_vars` | — | __init__ |
| `self.body` | — | __init__ |
| `self.hash` | — | __init__ |
| `self.head` | — | __init__ |

## Source

```python
class Clause:
    """ A definite clause (head :- body); supports theta-subsumption-based equality via a WL graph hash. """

    def __init__(self, head: Literal, body: Tuple[Literal, ...]):
        """ Store head/body literals and collect the set of all variable names across the clause. """
        self.head: Literal = head
        self.body: Tuple[Literal, ...] = body

        # compute all the 'vars' in the program
        self.all_vars: Set[str] = set()
        self.all_vars.update(head.arguments)
        for literal in (self.head,) + self.body:
            self.all_vars.update(literal.arguments)

        self.hash: Optional[int] = None

    def is_in_out_consistent_body(self) -> bool:
        """ :return: True if every 'in' variable in the body is produced (as 'out') by some other body literal. """
        var_has_out: Set[str] = set()

        for body_lit in self.body:
            var_has_out.update(body_lit.outputs)

        for body_lit in self.body:
            for in_var in body_lit.inputs:
                if in_var not in var_has_out:
                    return False

        return True

    def can_ground(self) -> bool:
        """ :return: True if the body literals can be ordered so that all 'in' variables are bound before use. """
        grounded_variables = self.head.inputs
        body_literals = set(self.body)

        while len(body_literals) > 0:
            selected_literal = None
            for literal in body_literals:
                if literal.inputs.issubset(grounded_variables):
                    selected_literal = literal
                    break

            if selected_literal is None:
                return False

            grounded_variables = grounded_variables.union(selected_literal.outputs)
            body_literals = body_literals.difference({selected_literal})

        return True

    def to_code(self) -> str:
        """ :return: Clingo rule string ``'head :- body'``, or just ``'head'`` for facts. """
        if len(self.body) > 0:
            return (
                f'{self.head.to_code()}:- '
                f'{",".join([blit.to_code() for blit in self.body])}'
            )
        else:
            return self.head.to_code()

    def get_lit_id_count_dict(self) -> Dict[Tuple[str, int, bool], int]:
        """ :return: Dict mapping ``(predicate, arity, positive)`` to occurrence count across head + body. """
        lit_pred_dict: Dict[Tuple[str, int, bool], int] = dict()
        for lit in [self.head] + list(self.body):
            if lit is not None:
                lit_tup: Tuple[str, int, bool] = lit.get_pred_arity_pos_id()
                if lit_tup not in lit_pred_dict:
                    lit_pred_dict[lit_tup] = 0

                lit_pred_dict[lit_tup] += 1

        return lit_pred_dict

    def theta_sub(self, other: 'Clause', subs_prev: Optional[Dict[str, str]] = None,
                  negate_l: Optional[List[bool]] = None, subs_forbid: Optional[Dict[str, List[str]]] = None,
                  ignore_head: bool = False) -> Optional[Dict[str, str]]:
        """ :return: A variable-substitution dict if ``self`` theta-subsumes ``other``; ``None`` otherwise. """
        # Initialize
        if ignore_head:
            assert negate_l is None, "Negate not yet integrated with ignore_head"

        if subs_prev is None:
            subs_prev = dict()
        if subs_forbid is None:
            subs_forbid = dict()

        lits_self: List[Literal] = list(self.body)
        lits_other: List[Literal] = list(other.body)
        if not ignore_head:
            lits_self = [self.head] + lits_self
            lits_other = [other.head] + lits_other

        name_to_lit_other: Dict[str, List[Literal]] = dict()
        for lit in lits_other:
            if lit.predicate not in name_to_lit_other.keys():
                name_to_lit_other[lit.predicate] = []
            name_to_lit_other[lit.predicate].append(lit)

        negate_prev = negate_l
        if negate_l is None:
            negate_l = [False] * len(lits_self)

        # check all predicate names in self appears in other
        assert len(lits_self) == len(negate_l), f"{self}, {other}, {len(lits_self)}, {len(negate_l)}, {negate_prev}"
        for lit_self, negate in zip(lits_self, negate_l):
            if (not negate) and (lit_self.predicate not in name_to_lit_other.keys()):
                return None

        return theta_sub_lits(lits_self, name_to_lit_other, negate_l, subs_prev, subs_forbid)

    def __str__(self) -> str:
        """ :return: Human-readable 'head :- body' rule string. """
        if len(self.body) > 0:
            # return (
            #    f'{self.head.to_code()}:- '
            #    f'{",".join([blit.to_code() for blit in self.body if blit.predicate[:4] != "dif_"])}'
            # )
            return (
                f'{self.head.to_code()}:- '
                f'{",".join([blit.to_code() for blit in self.body])}'
            )
        else:
            return self.head.to_code()

        # return self.to_code()

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        """ :return: Structure hash computed by WL-style message-passing over the literal/variable graph. """
        if self.hash is not None:
            return self.hash

        # make lit nodes
        lit_nodes: List[LitNode] = []
        for lit in [self.head]:
            lit_nodes.append(LitNode(lit.predicate, False, lit.arguments))

        for lit in self.body:
            lit_nodes.append(LitNode(lit.predicate, True, lit.arguments))

        # make connections between variable nodes
        for lit1_idx, lit_node1 in enumerate(lit_nodes):
            for lit2_idx, lit_node2 in enumerate(lit_nodes):
                if lit1_idx == lit2_idx:
                    continue
                for var_idx1, var_name1 in enumerate(lit_node1.var_names):
                    for var_idx2, var_name2 in enumerate(lit_node2.var_names):
                        if var_name1 == var_name2:
                            lit_node1.var_nodes[var_idx1].add_neighbor(lit_node2.var_nodes[var_idx2])

        # get all variable nodes
        var_nodes: List[VarNode] = []
        for lit_node in lit_nodes:
            var_nodes.extend(lit_node.var_nodes)

        # init representation
        for lit_node in lit_nodes:
            lit_node.prop_up()

        # propagate
        self.hash = 0
        for _ in range(10):
            for lit_node in lit_nodes:
                lit_node.prop_down()

            prop_across(var_nodes)

            for lit_node in lit_nodes:
                lit_node.prop_up()

        self.hash = sum([lit_node.rep for lit_node in lit_nodes])

        return self.hash

    def __eq__(self, other: object) -> bool:
        """ :return: True when ``self`` and ``other`` mutually theta-subsume each other. """
        if not isinstance(other, Clause):
            return NotImplemented

        # assuming no repeats
        if (self.head is None) != (other.head is None):
            return False
        if self.head.predicate != other.head.predicate:
            return False

        if self.theta_sub(other) is None:
            return False

        if other.theta_sub(self) is None:
            return False

        return True
```
