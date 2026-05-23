---
id: "class:deepxube.logic.asp.Solver"
kind: "class"
name: "Solver"
qualified_name: "deepxube.logic.asp.Solver"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 91
line_end: 286
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.logic.asp.Solver.__init__"
  - "func:deepxube.logic.asp.Solver.get_num_ground_rules"
  - "func:deepxube.logic.asp.Solver.get_models"
  - "func:deepxube.logic.asp.Solver.check_model"
  - "func:deepxube.logic.asp.Solver.sample_minimal_model"
  - "func:deepxube.logic.asp.Solver.sample_minimal_model_old"
  - "func:deepxube.logic.asp.Solver._add_goal"
  - "func:deepxube.logic.asp.Solver._make_assumptions"
attributes:
  - name: "self.bk"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.ctl_min"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.ctl_rand"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.goals_added"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.ground_atoms"
    annotation: null
    default: null
    from: "__init__"
  - name: "self.models_banned"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.logic.asp.Solver`

**File:** [deepxube/logic/asp.py:91](../../../deepxube/logic/asp.py#L91)
**Abstract:** no

## Docstring

Clingo-based ASP solver supporting randomized and minimal model sampling over a fixed background knowledge base
and a set of choosable ground atoms. 

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `__init__`
- `get_num_ground_rules` *(trivial, skipped)* — *(no docstring)*
- `get_models`
- `check_model`
- `sample_minimal_model`
- `sample_minimal_model_old`
- `_add_goal`
- `_make_assumptions`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.bk` | — | __init__ |
| `self.ctl_min` | — | __init__ |
| `self.ctl_rand` | — | __init__ |
| `self.goals_added` | — | __init__ |
| `self.ground_atoms` | — | __init__ |
| `self.models_banned` | — | __init__ |

## Source

```python
class Solver:
    """ Clingo-based ASP solver supporting randomized and minimal model sampling over a fixed background knowledge base
    and a set of choosable ground atoms. """

    def __init__(self, ground_atoms: List[Atom], bk: List[str]):
        """ Ground the background knowledge and atom bookkeeping into randomized and minimizing Clingo controls. """
        self.bk: List[str] = bk
        self.goals_added: Dict[frozenset[Clause], str] = dict()
        self.models_banned: List[Model] = []

        self.ground_atoms: List[Atom] = ground_atoms
        grnd_atom_counts: List[str] = []
        model_grnd_atoms_str: str = ""
        count_model_grnd_atoms_str: str = ""
        count_model_grnd_atoms_gt_str: str = ""
        minimize_grnd_atoms_str: str = ""
        if len(self.ground_atoms) > 0:
            grnd_atoms_str_l: List[str] = [atom_to_str(atom) for atom in self.ground_atoms]
            model_grnd_atoms_str = f"0 {{ {'; '.join(grnd_atoms_str_l)} }} {len(self.ground_atoms)}"
            for grnd_atom_idx, grnd_atom_str in enumerate(grnd_atoms_str_l):
                grnd_atom_counts.append(f"grnd_atom_count_num({grnd_atom_idx})")
                grnd_atom_counts.append(f"grnd_atom_present({grnd_atom_idx}) :- {grnd_atom_str}")

            count_model_grnd_atoms_str = "count_model_grnd_atoms(N) :- N = #count{ V: grnd_atom_present(V) }"
            count_model_grnd_atoms_gt_str = ("count_model_grnd_atoms_gt(N) :- grnd_atom_count_num(N), "
                                             "count_model_grnd_atoms(M), M > N")
            minimize_grnd_atoms_str = "#minimize {N: count_model_grnd_atoms(N)}"

        # clingo control
        seed = int.from_bytes(os.urandom(4), 'big')
        arguments_rand = ["--models=1", "--opt-mode=ignore", "--heuristic=Domain", "--dom-mod=5,16", "--rand-prob=1",
                          f"--seed={seed}", "--stats=2"]
        arguments_min = ["--models=1", "--opt-mode=optN", "--heuristic=Domain", "--dom-mod=5,16"]
        self.ctl_rand: Control = clingo.Control(arguments=arguments_rand)
        self.ctl_min: Control = clingo.Control(arguments=arguments_min)

        for add_line in bk + grnd_atom_counts + [model_grnd_atoms_str, count_model_grnd_atoms_str,
                                                 count_model_grnd_atoms_gt_str]:
            add_line = parse_clingo_line(add_line)
            if len(add_line) == 0:
                continue
            self.ctl_rand.add('base', [], f"{add_line}\n")
            self.ctl_min.add('base', [], f"{add_line}\n")
        add_line = parse_clingo_line(minimize_grnd_atoms_str)
        if len(add_line) > 0:
            self.ctl_min.add('base', [], f"{add_line}\n")

        self.ctl_rand.ground([("base", [])])
        self.ctl_min.ground([("base", [])])

    def get_num_ground_rules(self) -> int:
        # FIXME this behavior changes if looking at statistics before solve, not sure why
        self.ctl_rand.solve()
        num_grnd_rules: int = self.ctl_rand.statistics["problem"]["lp"]["rules"]

        return num_grnd_rules

    def get_models(self, spec: Spec, on_model: Callable[[Any], Model], num_models: int, minimal: bool) -> List[Model]:
        """

        :param spec: Specification
        :param on_model: Callable that processes models
        :param num_models: number of models to sample
        :param minimal: if true, only samples minimal models
        :return:
        """
        assumptions: List[Tuple[Symbol, bool]] = self._make_assumptions(spec)

        # get models
        models: List[Model] = []
        for model_itr in range(num_models):
            models_i: List[Model] = []
            self.ctl_rand.solve(assumptions=assumptions, on_model=lambda x: models_i.append(on_model(x)))
            if len(models_i) == 0:
                break
            model_i: Model = random.choice(models_i)

            if minimal:
                model_i = self.sample_minimal_model(spec, model_i, on_model)
                # assert model_i == self.sample_minimal_model_old(spec, model_i)

            models.append(model_i)

            if model_itr < (num_models - 1):
                assumptions_i: List[Tuple[Symbol, bool]] = self._make_assumptions(Spec(models_banned=[model_i]))
                assumptions.extend(assumptions_i)

        return models

    def check_model(self, spec: Spec, model: Model, timeout: Optional[float] = None) -> bool:
        """

        :param spec: Specification
        :param model: Model to check
        :param timeout: Timeout only for solving, not for grounding
        :return:
        """
        atoms_false: List[Atom] = [atom for atom in self.ground_atoms if atom not in model]
        spec_check: Spec = Spec(atoms_true=list(model), atoms_false=atoms_false)

        assumptions: List[Tuple[Symbol, bool]] = self._make_assumptions(spec)
        assumptions += self._make_assumptions(spec_check)
        models_ret: List[None] = []

        solve_handle: SolveHandle = self.ctl_rand.solve(assumptions=assumptions,
                                                        on_model=lambda x: models_ret.append(None), async_=True)
        solve_handle.wait(timeout=timeout)
        solve_handle.cancel()

        return len(models_ret) > 0

    def sample_minimal_model(self, spec: Spec, model: Model, on_model: Callable[[ModelCl], Model]) -> Model:
        """ :return: A randomly chosen stable model that is minimal w.r.t. the atoms not in ``model``. """
        models_min: List[Model] = []
        atoms_false: List[Atom] = [atom for atom in self.ground_atoms if atom not in model]
        spec_min: Spec = Spec(atoms_false=atoms_false)
        assumptions: List[Tuple[Symbol, bool]] = self._make_assumptions(spec.add(spec_min))
        self.ctl_min.solve(assumptions=assumptions, on_model=lambda x: models_min.append(on_model(x)))

        return random.choice(models_min)

    def sample_minimal_model_old(self, spec: Spec, model: Model) -> Model:
        """ Greedy recursive minimisation: remove atoms one at a time while the spec is still satisfiable;
        :return: the minimal model found. """
        atoms_l = list(model)
        random.shuffle(atoms_l)
        atoms_true: Set[Atom] = set(atoms_l)
        for atom in atoms_l:
            atoms_true.remove(atom)
            model_new: Model = frozenset(atoms_true)
            if self.check_model(spec, model_new):
                return self.sample_minimal_model_old(spec, model_new)

            atoms_true.add(atom)
        return frozenset(atoms_true)

    def _add_goal(self, goal: List[Clause]) -> str:
        """ Adds all goal clauses with same head

        :param goal:
        :return:
        """
        assert all([x.head.predicate == "goal" for x in goal]), "head should be goal"
        assert all([len(x.head.arguments) == 0 for x in goal]), "head should not have any arguments"

        goal_clauses_set: frozenset[Clause] = frozenset(goal)
        goal_new_head_pred_get: Optional[str] = self.goals_added.get(goal_clauses_set)
        if goal_new_head_pred_get is None:
            goal_num: int = len(self.goals_added)
            goal_new_head_pred: str = f"goal{goal_num}"

            prg_blk: str = goal_new_head_pred
            for goal_clause in goal:
                goal_clause_new_head: Clause = copy_clause_with_new_head(goal_clause, goal_new_head_pred)
                self.ctl_rand.add(prg_blk, [], f"{goal_clause_new_head.to_code()}.\n")
                self.ctl_min.add(prg_blk, [], f"{goal_clause_new_head.to_code()}.\n")
            self.ctl_rand.ground([(prg_blk, [])])
            self.ctl_min.ground([(prg_blk, [])])

            self.goals_added[goal_clauses_set] = goal_new_head_pred

            return goal_new_head_pred
        else:
            return goal_new_head_pred_get

    def _make_assumptions(self, spec: Spec) -> List[Tuple[Symbol, bool]]:
        """ :return: Clingo ``(Symbol, bool)`` assumption pairs derived from all constraints in ``spec``. """
        atoms_true: List[Atom] = []
        atoms_false: List[Atom] = []
        if len(spec.goal_true) > 0:
            atoms_true.append((self._add_goal(spec.goal_true),))
        if len(spec.goal_false) > 0:
            atoms_false.append((self._add_goal(spec.goal_false),))

        atoms_true += spec.atoms_true
        atoms_false += spec.atoms_false
        for model_banned in spec.models_banned:
            blits: List[Literal] = [Literal(atom[0], atom[1:], tuple(["in"] * len(atom[1:]))) for atom in
                                    model_banned]
            clause_banned: Clause = Clause(Literal("goal", tuple(), tuple()), tuple(blits))
            atoms_false.append((self._add_goal([clause_banned]),))

        assumed_true: List[str] = []
        assumed_false: List[str] = []
        for atom in atoms_true:
            assumed_true.append(atom_to_str(atom))
        for atom in atoms_false:
            assumed_false.append(atom_to_str(atom))

        assumptions: List[Tuple[Symbol, bool]] = []
        for lit in assumed_true:
            assumptions.append((parse_term(lit), True))
        for lit in assumed_false:
            assumptions.append((parse_term(lit), False))

        return assumptions
```
