# DeepXube Documentation Extractor

Static AST-based extractor that produces RAG-ready per-function / per-class /
per-module Markdown docs, a merged `graph.json`, a CLI-flag dispatch catalog,
and gap reports.

## Quick start

From the `deepxube-main/` directory:

```bash
python docs/extractor/extract.py --scope docs/extractor/poc_scope.txt
```

Output lands in `deepxube-main/docs/`.

## What it does

For each `.py` file listed in the scope:

1. Parses with Python's `ast` module — **no code is executed**.
2. Builds a per-file import index (so `np.array(...)` resolves to `numpy.array`).
3. Extracts every class, method, module-level function, constant, TypeVar.
4. For every function: parameters with type hints, return annotation, docstring,
   decorators, call sites (best-effort static resolution), `raise` statements,
   `self.*` reads/writes, source code.
5. For every class: bases, generic parameters, whether abstract,
   `@factory.register_class(...)` decorators, methods, attributes.
6. Writes:
   - `docs/functions/<module>/<Class>/<func>.md` (one per non-trivial function)
   - `docs/classes/<module>/<Class>.md`
   - `docs/modules/<module>.md`
   - `docs/graph.json` (merged knowledge graph)
   - `docs/cli_flags.json` (factory keys + dispatch rules)
   - `docs/missing_docstrings.md`
   - `docs/skipped_trivial.md`
7. Generates a sample Mermaid diagram in `docs/samples/` (POC only).

## Triviality rule

A function is skipped (listed in `skipped_trivial.md`, not given its own `.md`)
iff **all three** of:

- ≤3 statements (after removing docstring)
- no control flow (`if`/`for`/`while`/`try`/`with`/`match`)
- no calls to any project function

`__repr__`/`__str__`/`__eq__`/`__hash__` at ≤3 lines also count as trivial.

## Extractor inputs

- `--scope FILE` — text file listing one `.py` path per line (relative to repo
  root). Blank lines and lines starting with `#` are ignored.
- `--repo-root DIR` (default: `.`) — root of `deepxube-main/`.
- `--docs-root DIR` (default: `docs`) — output directory relative to repo root.

## Scope progression

The full documentation is generated module-by-module. After the POC, the order is:

1. `updaters/` (POC — current)
2. `utils/`
3. `base/`
4. `factories/`
5. `heuristics/`, `nnet/`
6. `pathfinding/`
7. `logic/`
8. `trainers/`
9. `domains/`
10. Entry points (`_cli.py`, `_train_cli.py`, `_solve.py`, `__main__.py`)
11. `tests/`

Between each module batch, the scope file is updated and the extractor re-run
on the combined scope. The graph/report files overwrite previous outputs; the
per-function/class/module `.md` files are additive and only the ones in scope
get refreshed.

## Schema

See [`SCHEMA.md`](./SCHEMA.md) for the full specification of the output formats.

## What the extractor does NOT do

- **No code execution.** Pure static. Flag-conditional dispatch that happens at
  runtime is recorded as a dispatch rule (see `cli_flags.json`) rather than as
  a hardcoded edge.
- **No LLM calls.** Docstrings are preserved verbatim; missing ones are listed
  in `missing_docstrings.md` for you to fill by hand or via a separate LLM pass.
- **No embedding / no vector index.** The Markdown corpus is the embedding-ready
  input; embedding happens at RAG-deploy time.
- **No dynamic coverage tracing.** We can later add a `--coverage-json` flag
  that merges `coverage.py` data into the graph as edge annotations, but not
  in this POC.

## Known limitations (POC-level)

- `ref:<module>.<attr>` call targets that fall outside the current scope stay
  as unresolved calls until their module is added to scope.
- Base-class resolution only works for classes defined in the scope. External
  bases (`ABC`, `Generic`, `numpy.ndarray`) appear as `to: null` with a note.
- Overloaded functions inside a single class body: last definition wins.
