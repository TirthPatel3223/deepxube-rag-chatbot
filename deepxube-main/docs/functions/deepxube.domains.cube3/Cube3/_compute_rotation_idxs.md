---
id: "func:deepxube.domains.cube3.Cube3._compute_rotation_idxs"
kind: "method"
name: "_compute_rotation_idxs"
qualified_name: "deepxube.domains.cube3.Cube3._compute_rotation_idxs"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 635
line_end: 709
class: "Cube3"
visibility: "private"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
  - name: "cube_len"
    annotation: "int"
    default: null
  - name: "moves"
    annotation: "List[str]"
    default: null
returns: "Tuple[Dict[str, NDArray[np.int_]], Dict[str, NDArray[np.int_]]]"
docstring_source: "present"
callees:
  - target: null
    expr: "dict"
    call_sites: [638, 639]
  - target: null
    expr: "int"
    call_sites: [643, 689, 690, 697, 698, 704, 705]
  - target: "func:numpy.array"
    expr: "np.array"
    call_sites: [645, 646, 677, 684, 685, 686, 687, 699, 700, 701, 702]
  - target: "func:numpy.zeros"
    expr: "np.zeros"
    call_sites: [648]
  - target: "func:numpy.copy"
    expr: "np.copy"
    call_sites: [649]
  - target: null
    expr: "range"
    call_sites: [653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 675, 676, 683, 696]
  - target: "func:numpy.arange"
    expr: "np.arange"
    call_sites: [671, 673, 679, 681]
  - target: null
    expr: "len"
    call_sites: [671, 673, 679, 681, 696]
  - target: null
    expr: "np.array([cubes_idxs[cubes_to[i]][0]]).flatten"
    call_sites: [684]
  - target: null
    expr: "np.array([cubes_idxs[cubes_to[i]][1]]).flatten"
    call_sites: [685]
  - target: null
    expr: "np.array([cubes_idxs[cubes_from[i]][0]]).flatten"
    call_sites: [686]
  - target: null
    expr: "np.array([cubes_idxs[cubes_from[i]][1]]).flatten"
    call_sites: [687]
  - target: null
    expr: "zip"
    call_sites: [688, 703]
  - target: "func:numpy.ravel_multi_index"
    expr: "np.ravel_multi_index"
    call_sites: [689, 690, 704, 705]
  - target: "func:numpy.concatenate"
    expr: "np.concatenate"
    call_sites: [691, 692, 706, 707]
  - target: null
    expr: "np.array([face_idxs[face_to][0]]).flatten"
    call_sites: [699]
  - target: null
    expr: "np.array([face_idxs[face_to][1]]).flatten"
    call_sites: [700]
  - target: null
    expr: "np.array([face_idxs[face_from][0]]).flatten"
    call_sites: [701]
  - target: null
    expr: "np.array([face_idxs[face_from][1]]).flatten"
    call_sites: [702]
raises: []
reads_attrs:
  - "self.adj_faces"
writes_attrs: []
---

# `deepxube.domains.cube3.Cube3._compute_rotation_idxs`

**File:** [deepxube/domains/cube3.py:635](../../../../deepxube/domains/cube3.py#L635)
**Class:** `Cube3`
**Visibility:** private
**Kind:** method

## Signature

```python
def _compute_rotation_idxs(self, cube_len: int, moves: List[str]) -> Tuple[Dict[str, NDArray[np.int_]], Dict[str, NDArray[np.int_]]]
```

## Docstring

:return: ``(rotate_idxs_new, rotate_idxs_old)`` flat-index permutation tables for every move string. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |
| `cube_len` | `int` | — |
| `moves` | `List[str]` | — |

## Returns

`Tuple[Dict[str, NDArray[np.int_]], Dict[str, NDArray[np.int_]]]`

## Calls

- `np.array` → `func:numpy.array` (lines: 645, 646, 677, 684, 685, 686, 687, 699, 700, 701, 702)
- `np.zeros` → `func:numpy.zeros` (lines: 648)
- `np.copy` → `func:numpy.copy` (lines: 649)
- `np.arange` → `func:numpy.arange` (lines: 671, 673, 679, 681)
- `np.ravel_multi_index` → `func:numpy.ravel_multi_index` (lines: 689, 690, 704, 705)
- `np.concatenate` → `func:numpy.concatenate` (lines: 691, 692, 706, 707)

### Unresolved
- `dict` (lines: 638, 639)
- `int` (lines: 643, 689, 690, 697, 698, 704, 705)
- `range` (lines: 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 675, 676, 683, 696)
- `len` (lines: 671, 673, 679, 681, 696)
- `np.array([cubes_idxs[cubes_to[i]][0]]).flatten` (lines: 684)
- `np.array([cubes_idxs[cubes_to[i]][1]]).flatten` (lines: 685)
- `np.array([cubes_idxs[cubes_from[i]][0]]).flatten` (lines: 686)
- `np.array([cubes_idxs[cubes_from[i]][1]]).flatten` (lines: 687)
- `zip` (lines: 688, 703)
- `np.array([face_idxs[face_to][0]]).flatten` (lines: 699)
- `np.array([face_idxs[face_to][1]]).flatten` (lines: 700)
- `np.array([face_idxs[face_from][0]]).flatten` (lines: 701)
- `np.array([face_idxs[face_from][1]]).flatten` (lines: 702)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Reads:**
- `self.adj_faces`

## Source

```python
    def _compute_rotation_idxs(self, cube_len: int,
                               moves: List[str]) -> Tuple[Dict[str, NDArray[np.int_]], Dict[str, NDArray[np.int_]]]:
        """ :return: ``(rotate_idxs_new, rotate_idxs_old)`` flat-index permutation tables for every move string. """
        rotate_idxs_new: Dict[str, NDArray[np.int_]] = dict()
        rotate_idxs_old: Dict[str, NDArray[np.int_]] = dict()

        for move in moves:
            f: str = move[0]
            sign: int = int(move[1:])

            rotate_idxs_new[move] = np.array([], dtype=int)
            rotate_idxs_old[move] = np.array([], dtype=int)

            colors: NDArray = np.zeros((6, cube_len, cube_len), dtype=np.int64)
            colors_new = np.copy(colors)

            # WHITE:0, YELLOW:1, BLUE:2, GREEN:3, ORANGE: 4, RED: 5

            adj_idxs = {0: {2: [range(0, cube_len), cube_len - 1], 3: [range(0, cube_len), cube_len - 1],
                            4: [range(0, cube_len), cube_len - 1], 5: [range(0, cube_len), cube_len - 1]},
                        1: {2: [range(0, cube_len), 0], 3: [range(0, cube_len), 0], 4: [range(0, cube_len), 0],
                            5: [range(0, cube_len), 0]},
                        2: {0: [0, range(0, cube_len)], 1: [0, range(0, cube_len)],
                            4: [cube_len - 1, range(cube_len - 1, -1, -1)], 5: [0, range(0, cube_len)]},
                        3: {0: [cube_len - 1, range(0, cube_len)], 1: [cube_len - 1, range(0, cube_len)],
                            4: [0, range(cube_len - 1, -1, -1)], 5: [cube_len - 1, range(0, cube_len)]},
                        4: {0: [range(0, cube_len), cube_len - 1], 1: [range(cube_len - 1, -1, -1), 0],
                            2: [0, range(0, cube_len)], 3: [cube_len - 1, range(cube_len - 1, -1, -1)]},
                        5: {0: [range(0, cube_len), 0], 1: [range(cube_len - 1, -1, -1), cube_len - 1],
                            2: [cube_len - 1, range(0, cube_len)], 3: [0, range(cube_len - 1, -1, -1)]}
                        }
            face_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'B': 4, 'F': 5}
            face = face_dict[f]

            faces_to = self.adj_faces[face]
            if sign == 1:
                faces_from = faces_to[(np.arange(0, len(faces_to)) + 1) % len(faces_to)]
            else:
                faces_from = faces_to[(np.arange(len(faces_to) - 1, len(faces_to) - 1 + len(faces_to))) % len(faces_to)]

            cubes_idxs = [[0, range(0, cube_len)], [range(0, cube_len), cube_len - 1],
                          [cube_len - 1, range(cube_len - 1, -1, -1)], [range(cube_len - 1, -1, -1), 0]]
            cubes_to = np.array([0, 1, 2, 3])
            if sign == 1:
                cubes_from = cubes_to[(np.arange(len(cubes_to) - 1, len(cubes_to) - 1 + len(cubes_to))) % len(cubes_to)]
            else:
                cubes_from = cubes_to[(np.arange(0, len(cubes_to)) + 1) % len(cubes_to)]

            for i in range(4):
                idxs_new = [[idx1, idx2] for idx1 in np.array([cubes_idxs[cubes_to[i]][0]]).flatten() for idx2 in
                            np.array([cubes_idxs[cubes_to[i]][1]]).flatten()]
                idxs_old = [[idx1, idx2] for idx1 in np.array([cubes_idxs[cubes_from[i]][0]]).flatten() for idx2 in
                            np.array([cubes_idxs[cubes_from[i]][1]]).flatten()]
                for idxNew, idxOld in zip(idxs_new, idxs_old):
                    flat_idx_new: int = int(np.ravel_multi_index((face, idxNew[0], idxNew[1]), colors_new.shape))
                    flat_idx_old: int = int(np.ravel_multi_index((face, idxOld[0], idxOld[1]), colors.shape))
                    rotate_idxs_new[move] = np.concatenate((rotate_idxs_new[move], [flat_idx_new]))
                    rotate_idxs_old[move] = np.concatenate((rotate_idxs_old[move], [flat_idx_old]))

            # Rotate adjacent faces
            face_idxs = adj_idxs[face]
            for i in range(0, len(faces_to)):
                face_to: int = int(faces_to[i])
                face_from: int = int(faces_from[i])
                idxs_new = [[idx1, idx2] for idx1 in np.array([face_idxs[face_to][0]]).flatten() for idx2 in
                            np.array([face_idxs[face_to][1]]).flatten()]
                idxs_old = [[idx1, idx2] for idx1 in np.array([face_idxs[face_from][0]]).flatten() for idx2 in
                            np.array([face_idxs[face_from][1]]).flatten()]
                for idxNew, idxOld in zip(idxs_new, idxs_old):
                    flat_idx_new = int(np.ravel_multi_index((face_to, idxNew[0], idxNew[1]), colors_new.shape))
                    flat_idx_old = int(np.ravel_multi_index((face_from, idxOld[0], idxOld[1]), colors.shape))
                    rotate_idxs_new[move] = np.concatenate((rotate_idxs_new[move], [flat_idx_new]))
                    rotate_idxs_old[move] = np.concatenate((rotate_idxs_old[move], [flat_idx_old]))

        return rotate_idxs_new, rotate_idxs_old
```
