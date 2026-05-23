---
id: "func:deepxube.domains.sokoban.Sokoban.to_img"
kind: "method"
name: "to_img"
qualified_name: "deepxube.domains.sokoban.Sokoban.to_img"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 279
line_end: 313
class: "Sokoban"
visibility: "public"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "state"
    annotation: "SkState"
    default: null
  - name: "goal"
    annotation: "SkGoal"
    default: null
returns: "NDArray"
docstring_source: "present"
callees:
  - target: "func:deepxube.domains.sokoban._get_surfaces"
    expr: "_get_surfaces"
    call_sites: [282]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [284]
  - target: null
    expr: "range"
    call_sites: [285, 288]
raises: []
reads_attrs:
  - "self._surfaces"
  - "self.dim"
writes_attrs:
  - "self._surfaces"
---

# `deepxube.domains.sokoban.Sokoban.to_img`

**File:** [deepxube/domains/sokoban.py:279](../../../../deepxube/domains/sokoban.py#L279)
**Class:** `Sokoban`
**Visibility:** public
**Kind:** method

## Signature

```python
def to_img(self, state: SkState, goal: SkGoal) -> NDArray
```

## Docstring

:return: Shape ``(dim*16, dim*16, 3)`` RGB array compositing surface tiles for each cell. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `state` | `SkState` | — |
| `goal` | `SkGoal` | — |

## Returns

`NDArray`

## Calls

- `_get_surfaces` → `func:deepxube.domains.sokoban._get_surfaces` (lines: 282)
- `np.zeros` → `func:numpy.zeros` (lines: 284)

### Unresolved
- `range` (lines: 285, 288)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self._surfaces`

**Reads:**
- `self._surfaces`
- `self.dim`

## Source

```python
    def to_img(self, state: SkState, goal: SkGoal) -> NDArray:
        """ :return: Shape ``(dim*16, dim*16, 3)`` RGB array compositing surface tiles for each cell. """
        if self._surfaces is None:
            self._surfaces = _get_surfaces()

        room_rgb: NDArray[np.uint8] = np.zeros(shape=(self.dim * 16, self.dim * 16, 3), dtype=np.uint8)
        for i in range(self.dim):
            x_i = i * 16

            for j in range(self.dim):
                y_j = j * 16

                surface_str: str
                if state.walls[i, j]:
                    surface_str = "wall"
                elif (state.agent[0] == i) and (state.agent[1] == j):
                    if goal.boxes[i, j]:
                        surface_str = "player_on_target"
                    else:
                        surface_str = "player"
                elif state.boxes[i, j]:
                    if goal.boxes[i, j]:
                        surface_str = "box_on_target"
                    else:
                        surface_str = "box"
                elif goal.boxes[i, j]:
                    surface_str = "box_target"
                else:
                    surface_str = "floor"
                room_rgb[x_i:(x_i + 16), y_j:(y_j + 16), :] = self._surfaces[surface_str]

        # img = Image.fromarray(room_rgb, 'RGB')
        # img = img.resize((self.img_dim, self.img_dim))

        return room_rgb
```
