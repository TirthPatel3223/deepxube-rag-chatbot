---
id: "func:deepxube.domains.sokoban.Sokoban.__init__"
kind: "method"
name: "__init__"
qualified_name: "deepxube.domains.sokoban.Sokoban.__init__"
module: "deepxube.domains.sokoban"
file: "deepxube/domains/sokoban.py"
line_start: 138
line_end: 173
class: "Sokoban"
visibility: "dunder"
is_abstract: false
is_generator: false
is_async: false
decorators: []
parameters:
  - name: "self"
    annotation: null
    default: null
returns: "None"
docstring_source: "present"
callees:
  - target: null
    expr: "super().__init__"
    call_sites: [140]
  - target: null
    expr: "super"
    call_sites: [140]
  - target: "func:deepxube.domains.sokoban.SkAction"
    expr: "SkAction"
    call_sites: [149]
  - target: null
    expr: "range"
    call_sites: [149]
  - target: "func:deepxube.domains.sokoban.get_data_dir"
    expr: "get_data_dir"
    call_sites: [152]
  - target: null
    expr: "os.path.exists"
    call_sites: [154, 162]
  - target: null
    expr: "input"
    call_sites: [157]
  - target: null
    expr: "user_in.upper"
    call_sites: [159, 172]
  - target: null
    expr: "print"
    call_sites: [161, 168, 170]
  - target: "func:os.makedirs"
    expr: "os.makedirs"
    call_sites: [163]
  - target: "func:wget.download"
    expr: "wget.download"
    call_sites: [166]
  - target: "func:tarfile.open"
    expr: "tarfile.open"
    call_sites: [167]
  - target: null
    expr: "tar_gz_file.extractall"
    call_sites: [169]
  - target: "func:os.remove"
    expr: "os.remove"
    call_sites: [171]
raises: []
reads_attrs:
  - "self._surfaces"
  - "self.actions"
  - "self.dim"
  - "self.num_actions"
  - "self.num_boxes"
  - "self.states_train"
writes_attrs:
  - "self._surfaces"
  - "self.actions"
  - "self.dim"
  - "self.num_actions"
  - "self.num_boxes"
  - "self.states_train"
---

# `deepxube.domains.sokoban.Sokoban.__init__`

**File:** [deepxube/domains/sokoban.py:138](../../../../deepxube/domains/sokoban.py#L138)
**Class:** `Sokoban`
**Visibility:** dunder
**Kind:** method

## Signature

```python
def __init__(self) -> None
```

## Docstring

Initialise grid dimensions and prompt the user to download training data if absent. 

## Parameters

| Name | Type | Default |
|------|------|---------|
| `self` | — | — |

## Returns

`None`

## Calls

- `SkAction` → `func:deepxube.domains.sokoban.SkAction` (lines: 149)
- `get_data_dir` → `func:deepxube.domains.sokoban.get_data_dir` (lines: 152)
- `os.makedirs` → `func:os.makedirs` (lines: 163)
- `wget.download` → `func:wget.download` (lines: 166)
- `tarfile.open` → `func:tarfile.open` (lines: 167)
- `os.remove` → `func:os.remove` (lines: 171)

### Unresolved
- `super().__init__` (lines: 140)
- `super` (lines: 140)
- `range` (lines: 149)
- `os.path.exists` (lines: 154, 162)
- `input` (lines: 157)
- `user_in.upper` (lines: 159, 172)
- `print` (lines: 161, 168, 170)
- `tar_gz_file.extractall` (lines: 169)

## Called by

*(See `graph.json` for reverse edges; placeholder filled by graph post-pass.)*

## Attribute access

**Writes:**
- `self._surfaces`
- `self.actions`
- `self.dim`
- `self.num_actions`
- `self.num_boxes`
- `self.states_train`

**Reads:**
- `self._surfaces`
- `self.actions`
- `self.dim`
- `self.num_actions`
- `self.num_boxes`
- `self.states_train`

## Source

```python
    def __init__(self) -> None:
        """ Initialise grid dimensions and prompt the user to download training data if absent. """
        super().__init__()

        self.dim: int = 10
        self.num_boxes: int = 4

        self.num_actions: int = 4

        self.states_train: Optional[List[SkState]] = None
        self._surfaces: Optional[Dict[str, NDArray]] = None
        self.actions: List[SkAction] = [SkAction(x) for x in range(self.num_actions)]

        # check if data needs to be downloaded
        data_dir = get_data_dir()
        data_download_link: str = "https://github.com/forestagostinelli/DeepXubeData/raw/main/sokoban.tar.gz"
        if not os.path.exists(f"{data_dir}/sokoban/"):
            valid_user_in: bool = False
            while not valid_user_in:
                user_in: str = input(f"Sokoban data needs to be downloaded from {data_download_link}. "
                                     f"Download data (about 16MB)? (y/n):")
                if user_in.upper() == "Y":
                    valid_user_in = True
                    print("Downloading compressed data")
                    if not os.path.exists(data_dir):
                        os.makedirs(data_dir)

                    tar_gz_file_name = f"{data_dir}/sokoban.tar.gz"
                    wget.download(data_download_link, tar_gz_file_name, bar=None)
                    tar_gz_file = tarfile.open(tar_gz_file_name)
                    print("Uncompressing data")
                    tar_gz_file.extractall(data_dir)
                    print("Deleting compressed data")
                    os.remove(tar_gz_file_name)
                elif user_in.upper() == "N":
                    valid_user_in = True
```
