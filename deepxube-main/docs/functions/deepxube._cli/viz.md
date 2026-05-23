---
id: "func:deepxube._cli.viz"
kind: "function"
name: "viz"
qualified_name: "deepxube._cli.viz"
module: "deepxube._cli"
file: "deepxube/_cli.py"
line_start: 124
line_end: 207
class: null
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "args"
    annotation: "argparse.Namespace"
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: "func:deepxube.utils.command_line_utils.get_domain_from_arg"
    expr: "get_domain_from_arg"
    call_sites: [127]
  - target: null
    expr: "dict"
    call_sites: [132]
  - target: "func:pickle.load"
    expr: "pickle.load"
    call_sites: [134]
  - target: null
    expr: "open"
    call_sites: [134]
  - target: null
    expr: "domain.sample_problem_instances"
    call_sites: [138]
  - target: "func:matplotlib.pyplot.figure"
    expr: "plt.figure"
    call_sites: [142]
  - target: null
    expr: "isinstance"
    call_sites: [143, 190]
  - target: null
    expr: "domain.visualize_state_goal"
    call_sites: [144]
  - target: null
    expr: "print"
    call_sites: [145, 161, 164, 171, 180, 186, 191, 199, 203, 204]
  - target: null
    expr: "domain.is_solved"
    call_sites: [145, 171, 173, 180, 186, 204]
  - target: null
    expr: "len"
    call_sites: [152, 156, 195]
  - target: "func:matplotlib.pyplot.show"
    expr: "plt.show"
    call_sites: [153, 192, 207]
  - target: null
    expr: "input"
    call_sites: [155, 188, 194]
  - target: null
    expr: "act_str.upper"
    call_sites: [158, 174]
  - target: null
    expr: "domain.next_state"
    call_sites: [162, 201]
  - target: "func:deepxube._cli._viz_state_goal_update"
    expr: "_viz_state_goal_update"
    call_sites: [169, 178, 185, 205]
  - target: null
    expr: "int"
    call_sites: [182]
  - target: null
    expr: "domain.string_to_action_help"
    call_sites: [191]
  - target: null
    expr: "domain.string_to_action"
    call_sites: [197]
  - target: "func:typing.cast"
    expr: "cast"
    call_sites: [205]
raises: []
reads_attrs: []
writes_attrs: []
---

# `deepxube._cli.viz`

**File:** [deepxube/_cli.py:124](../../../../deepxube/_cli.py#L124)
**Visibility:** public
**Kind:** function

## Signature

```python
def viz(args: argparse.Namespace) -> None
```

## Docstring

Visualise a state/goal pair and optionally step through a solution path interactively. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `args` | `argparse.Namespace` | — |

## Returns

`None`

## Calls

- `get_domain_from_arg` → `func:deepxube.utils.command_line_utils.get_domain_from_arg` (lines: 127)
- `pickle.load` → `func:pickle.load` (lines: 134)
- `plt.figure` → `func:matplotlib.pyplot.figure` (lines: 142)
- `plt.show` → `func:matplotlib.pyplot.show` (lines: 153, 192, 207)
- `_viz_state_goal_update` → `func:deepxube._cli._viz_state_goal_update` (lines: 169, 178, 185, 205)
- `cast` → `func:typing.cast` (lines: 205)

### Unresolved
- `dict` (lines: 132)
- `open` (lines: 134)
- `domain.sample_problem_instances` (lines: 138)
- `isinstance` (lines: 143, 190)
- `domain.visualize_state_goal` (lines: 144)
- `print` (lines: 145, 161, 164, 171, 180, 186, 191, 199, 203, 204)
- `domain.is_solved` (lines: 145, 171, 173, 180, 186, 204)
- `len` (lines: 152, 156, 195)
- `input` (lines: 155, 188, 194)
- `act_str.upper` (lines: 158, 174)
- `domain.next_state` (lines: 162, 201)
- `int` (lines: 182)
- `domain.string_to_action_help` (lines: 191)
- `domain.string_to_action` (lines: 197)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Source

```python
def viz(args: argparse.Namespace) -> None:
    """ Visualise a state/goal pair and optionally step through a solution path interactively. """
    # domain
    domain, domain_name = get_domain_from_arg(args.domain)

    # state and goal
    state: State
    goal: Goal
    data: Dict = dict()
    if args.file is not None:
        data = pickle.load(open(args.file, "rb"))
        state = data['states'][args.idx]
        goal = data['goals'][args.idx]
    else:
        states, goals = domain.sample_problem_instances([args.steps])
        state = states[0]
        goal = goals[0]

    fig: Figure = plt.figure(figsize=(5, 5))
    assert isinstance(domain, StateGoalVizable)
    domain.visualize_state_goal(state, goal, fig)
    print(f"Goal Reached: {domain.is_solved([state], [goal])[0]}")

    if args.soln:
        solved: bool = data['solved'][args.idx]
        if solved:
            states_on_path: List[State] = data['states_on_path'][args.idx]
            state_idx: int = 0
            state_idx_max: int = len(states_on_path) - 1
            plt.show(block=False)
            while True:
                act_str = input(f"State idx {state_idx} of {state_idx_max} on solution path. Next state (n), Previous state (p), or state idx: ")
                if len(act_str) == 0:
                    break
                if act_str.upper() == "N":
                    if state_idx < state_idx_max:
                        action: Action = data['actions'][args.idx][state_idx]
                        print(f"Action: {action}")
                        state_next_l, tcs = domain.next_state([state], [action])
                        state_next: State = state_next_l[0]
                        print(f"Transition cost: {tcs[0]}")
                        state_idx += 1
                        assert state_next == states_on_path[state_idx]
                        state = state_next

                        _viz_state_goal_update(domain, state, goal, fig)

                        print(f"Goal Reached: {domain.is_solved([state], [goal])[0]}")
                        if state_idx == state_idx_max:
                            assert domain.is_solved([state], [goal])[0]
                elif act_str.upper() == "P":
                    if state_idx > 0:
                        state_idx -= 1
                        state = states_on_path[state_idx]
                        _viz_state_goal_update(domain, state, goal, fig)

                        print(f"Goal Reached: {domain.is_solved([state], [goal])[0]}")
                else:
                    state_idx = int(act_str)
                    assert state_idx >= 0
                    state = states_on_path[state_idx]
                    _viz_state_goal_update(domain, state, goal, fig)
                    print(f"Goal Reached: {domain.is_solved([state], [goal])[0]}")
        else:
            input("Not solved (press enter to quit): ")
    else:
        if isinstance(domain, StringToAct):
            print(domain.string_to_action_help())
            plt.show(block=False)
            while True:
                act_str = input("Write action (press enter to quit): ")
                if len(act_str) == 0:
                    break
                action_op: Optional[Action] = domain.string_to_action(act_str)
                if action_op is None:
                    print(f"No action {act_str}")
                else:
                    states_next, tcs = domain.next_state([state], [action_op])
                    state = states_next[0]
                    print(f"Transition cost: {tcs[0]}")
                    print(f"Goal Reached: {domain.is_solved([state], [goal])[0]}")
                    _viz_state_goal_update(cast(StateGoalVizable, domain), state, goal, fig)
        else:
            plt.show(block=True)
```
