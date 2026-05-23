---
id: "func:deepxube.logic.asp.Solver.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.logic.asp.Solver.__init__"
module: "deepxube.logic.asp"
file: "deepxube/logic/asp.py"
line_start: 95
line_end: 139
class: "Solver"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "ground_atoms"
    annotation: "List[Atom]"
    default: null
  - name: "bk"
    annotation: "List[str]"
    default: null
returns: null
docstring_source: "present"
callees:
  - target: null
    expr: "dict"
    call_sites: [98]
  - target: null
    expr: "len"
    call_sites: [107, 109, 130, 135]
  - target: "func:deepxube.logic.logic_utils.atom_to_str"
    expr: "atom_to_str"
    call_sites: [108]
  - target: null
    expr: "'; '.join"
    call_sites: [109]
  - target: null
    expr: "enumerate"
    call_sites: [110]
  - target: null
    expr: "grnd_atom_counts.append"
    call_sites: [111, 112]
  - target: null
    expr: "int.from_bytes"
    call_sites: [120]
  - target: "func:os.urandom"
    expr: "os.urandom"
    call_sites: [120]
  - target: "func:clingo.Control"
    expr: "clingo.Control"
    call_sites: [124, 125]
  - target: "func:deepxube.logic.asp.parse_clingo_line"
    expr: "parse_clingo_line"
    call_sites: [129, 134]
  - target: null
    expr: "self.ctl_rand.add"
    call_sites: [132]
  - target: null
    expr: "self.ctl_min.add"
    call_sites: [133, 136]
  - target: null
    expr: "self.ctl_rand.ground"
    call_sites: [138]
  - target: null
    expr: "self.ctl_min.ground"
    call_sites: [139]
raises: []
reads_attrs:
  - "self.bk"
  - "self.ctl_min"
  - "self.ctl_rand"
  - "self.goals_added"
  - "self.ground_atoms"
  - "self.models_banned"
writes_attrs:
  - "self.bk"
  - "self.ctl_min"
  - "self.ctl_rand"
  - "self.goals_added"
  - "self.ground_atoms"
  - "self.models_banned"
---

# `deepxube.logic.asp.Solver.__init__`

**File:** [deepxube/logic/asp.py:95](../../../../deepxube/logic/asp.py#L95)
**Class:** `Solver`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self, ground_atoms: List[Atom], bk: List[str])
```

## Docstring

Ground the background knowledge and atom bookkeeping into randomized and minimizing Clingo controls. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `ground_atoms` | `List[Atom]` | — |
| `bk` | `List[str]` | — |

## Returns

*(Not annotated.)*

## Calls

- `atom_to_str` → `func:deepxube.logic.logic_utils.atom_to_str` (lines: 108)
- `os.urandom` → `func:os.urandom` (lines: 120)
- `clingo.Control` → `func:clingo.Control` (lines: 124, 125)
- `parse_clingo_line` → `func:deepxube.logic.asp.parse_clingo_line` (lines: 129, 134)

### Unresolved
- `dict` (lines: 98)
- `len` (lines: 107, 109, 130, 135)
- `'; '.join` (lines: 109)
- `enumerate` (lines: 110)
- `grnd_atom_counts.append` (lines: 111, 112)
- `int.from_bytes` (lines: 120)
- `self.ctl_rand.add` (lines: 132)
- `self.ctl_min.add` (lines: 133, 136)
- `self.ctl_rand.ground` (lines: 138)
- `self.ctl_min.ground` (lines: 139)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self.bk`
- `self.ctl_min`
- `self.ctl_rand`
- `self.goals_added`
- `self.ground_atoms`
- `self.models_banned`

**Reads:**
- `self.bk`
- `self.ctl_min`
- `self.ctl_rand`
- `self.goals_added`
- `self.ground_atoms`
- `self.models_banned`

## Source

```python
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
```
