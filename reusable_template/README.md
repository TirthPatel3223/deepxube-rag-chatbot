# Generic Python Codebase Documentation Extractor

A static AST-based extractor that produces:

- **One Markdown file per non-trivial function, class, and module** — with YAML
  frontmatter for RAG ingestion and Markdown body for human reading.
- **`graph.json`** — a merged knowledge graph (nodes + typed edges: `calls`,
  `inherits`, `registers`, `raises`, `reads_attr`, `writes_attr`).
- **`cli_flags.json`** — catalog of factory-registered dispatch keys.
- **`missing_docstrings.md`** — gap report so the human reviewer can fill
  docstrings after the fact.
- **`skipped_trivial.md`** — log of functions skipped by the triviality rule.
- **Per-factory Mermaid diagrams** — one readable inheritance diagram per
  factory registry.

## How this originated

This extractor was built for Tirth's DeepXube RAG documentation project
(Prof. Agostinelli, U. South Carolina) in April 2026. The original lives in
`deepxube-main/docs/extractor/`. The output was designed as the corpus for a
RAG-based chatbot that answers questions about the codebase, with particular
support for **subgraph isolation by CLI-flag combination** (since DeepXube
dispatches through factory registries by flag-driven string keys).

**The code is unchanged except for three generalizations:**

1. All factory-decorator patterns are now configurable (was hardcoded to
   `@factory.register_class("key")`).
2. All factory-instance annotation prefixes are configurable (was hardcoded
   to `Factory[...]`).
3. Scope resolution supports an explicit list, a scope file, or
   auto-discovery under a root — whichever suits the target project.

## Quick start on a new project

1. Copy this `reusable_template/` folder into the target project (or run it
   from anywhere — paths in the config are relative to the config's own
   directory).
2. Copy `config.example.json` to `config.json` and edit:
   - `repo_root` — where the target project lives.
   - `docs_root` — where output should land.
   - Choose **one** of `scope_file`, `scope`, or `auto_discover`.
   - Adjust `factory_registration_patterns` if the project uses a different
     decorator name for registrations (e.g. `@registry.add("key")` →
     `{"method_name": "add", "kind_label": "add"}`).
   - Adjust `factory_instance_annotation_prefixes` if the factory class has
     a different name (e.g. `Registry[...]`).
3. Run:
   ```bash
   python extract.py --config config.json
   ```

That's it. Everything else — per-function Markdown, graph.json, Mermaid, gap
reports — is generated without further configuration.

## Output schema

See [`SCHEMA.md`](./SCHEMA.md) for the full specification of every output file,
including node/edge id scheme, YAML frontmatter fields, and stability policy.

The schema is **v1.0** and frozen. Additive fields bump the minor version;
breaking changes bump the major version and require re-extraction.

## What the extractor does

For each Python file in scope, it parses with `ast` (no execution). It records
for every function: parameters with type hints, return annotation, docstring
(verbatim if present), decorators, source code, call sites (best-effort static
resolution using the per-file import index), `raise` statements, and `self.*`
attribute reads/writes. For every class: bases, generic parameters, abstract
status, factory-registration decorators, methods, attributes (including those
assigned in `__init__`). For every module: imports, classes, functions,
module-level constants, TypeVars.

Calls to builtins are filtered out. Method calls on `self` are resolved to
the class's own method (even through inheritance — the post-pass links to the
base class when the subclass doesn't override). Calls to imported names
resolve through the import index. Calls to local variables' methods
(`queue.put(...)`, `list.append(...)`) remain **unresolved** and are listed
in `graph.json["unresolved_calls"]` — this is the static-analysis ceiling.

## Triviality rule

A function is skipped (listed in `skipped_trivial.md`, not given its own
`.md`) iff **all three** of:

- ≤3 statements (after docstring removal)
- no control flow (`if` / `for` / `while` / `try` / `with` / `match`)
- no calls to project functions

`__repr__` / `__str__` / `__eq__` / `__hash__` at ≤3 lines are also skipped
under a separate dunder rule. `__init__.py` files should typically be
excluded from scope entirely, since they are almost always re-export-only.

## What the extractor does NOT do

- **No code execution.** Pure static. Flag-conditional dispatch that happens
  at runtime is recorded as a dispatch rule (see `cli_flags.json`) rather
  than as a hardcoded graph edge.
- **No LLM calls.** Docstrings are preserved verbatim; missing ones are
  listed in `missing_docstrings.md` for you to fill by hand or via a
  separate LLM pass.
- **No embedding / no vector index.** The Markdown corpus is the
  embedding-ready input; embedding happens at RAG-deploy time.
- **No dynamic coverage tracing.** You can later add a `--coverage-json`
  flag that merges `coverage.py` data into the graph as edge annotations,
  but this is out of the base tool.

## Known limitations

- Call targets that fall outside the current scope stay as unresolved calls
  until their module is added to scope. Widen the scope or accept the gap.
- Base-class resolution only works for classes defined in scope. External
  bases (`ABC`, `Generic`, `nn.Module`) appear as `to: null` with a note.
- Overloaded functions inside a class body: last definition wins.
- Dynamic class creation (`type(...)`), monkey-patched attributes, and
  `exec`-based plumbing are invisible to static analysis.

## Scaling from POC to full codebase

The standard workflow:

1. Pick a small, self-contained module for the POC (DeepXube started with
   `updaters/` — ~4 files, ~40 classes including bases).
2. Run, review output, freeze the schema.
3. Expand scope module-by-module, re-running the extractor on the cumulative
   scope each time. Markdown files are idempotent — re-running on an
   unchanged file produces identical output.
4. At the end, run once on the full codebase. The unresolved-call count will
   drop significantly as cross-module references become resolvable.

## For future Claude or another agent

If you are an AI assistant asked to adapt this extractor to a new codebase,
follow this checklist:

- [ ] Read the target project's `README.md` and understand its top-level layout.
- [ ] Identify factory/registry patterns. Look for decorator calls that
      take a string key argument: `@factory.register("name")`,
      `@registry.add("x")`, etc. Update `factory_registration_patterns`.
- [ ] Identify the factory class itself. It will typically be instantiated
      at module scope with a type annotation like `Factory[Foo]` or
      `Registry[Bar]`. Update `factory_instance_annotation_prefixes`.
- [ ] Decide the scope. For small projects use `auto_discover`. For larger
      ones use `scope_file` and grow it module by module.
- [ ] Run the extractor and inspect `docs/graph.json`, specifically the
      `unresolved_calls` and `factories[*].registered_keys` fields. These
      are the two signals that tell you if your config is catching what
      it should.
- [ ] If you're documenting for a RAG system, emit embeddings at deploy
      time using the per-function `.md` frontmatter as metadata and the
      body as the text. One file = one chunk by design.

## License

Same license as the target project. This template itself is derivative of
the DeepXube documentation tooling.
