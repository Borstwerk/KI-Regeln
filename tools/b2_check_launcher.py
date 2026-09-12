#!/usr/bin/env python3
"""The `check` command an agent may run, and the only thing `Bash(check)` can reach.

The adapter allows exactly one literal invocation. That allowance is worth nothing unless the
thing it invokes is trusted, so this module materialises a launcher the agent cannot edit,
outside the writable workspace, that takes no arguments and does exactly one thing: hand the
pinned workspace check to the execution boundary.

    Claude  ->  Bash(check)  ->  bin/check  (adapter-owned, read-only)
                                     |
                                     v
                             b2_boundary.run_in_view
                                     |
                                     v
                          python3 /workspace/checks/validate.py

The workspace path comes from the adapter, baked into the launcher at materialisation time.
Nothing about it is taken from agent input, so there is no argument to smuggle a path
through -- and any argument at all is refused.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import stat
import sys
from pathlib import Path

try:
    from .b2_boundary import BoundaryError, ViewSpec, run_in_view
except ImportError:  # direct script sibling import
    from b2_boundary import BoundaryError, ViewSpec, run_in_view

LAUNCHER_NAME = "check"
BIN_DIR = "bin"
# The only modules the launcher needs. Staged into a directory of its own so the view never
# carries the repository, and so an agent that reads `bin/check` learns two in-view paths and
# no host path. The earlier version embedded `Path(__file__).resolve().parent`, which handed
# out the absolute path of the evaluator's own tools directory.
TRUSTED_RUNTIME_FILES = ("b2_boundary.py", "b2_check_launcher.py")
CHECK_ENTRY = "checks/validate.py"
CHECK_TIMEOUT = 60
# Exit codes the launcher owns. 0 and 1 belong to the check itself.
EXIT_MISUSE = 64
EXIT_BOUNDARY = 65

TEMPLATE = '''#!/usr/bin/env python3
"""Adapter-owned check launcher. Not editable from the workspace, and takes no arguments."""
import sys

sys.path.insert(0, {tools!r})
from b2_check_launcher import launch  # noqa: E402

raise SystemExit(launch({workspace!r}, sys.argv[1:]))
'''


def launch(workspace: str, argv: list[str]) -> int:
    """Run the pinned workspace check inside the boundary. No arguments, no alternatives."""
    if argv:
        print(f"check takes no arguments; got {argv}", file=sys.stderr)
        return EXIT_MISUSE
    root = Path(workspace)
    if not (root / CHECK_ENTRY).is_file():
        print(f"the workspace has no {CHECK_ENTRY}", file=sys.stderr)
        return EXIT_MISUSE
    try:
        result = run_in_view(ViewSpec(
            workspace=root,
            argv=("/usr/bin/env", "python3", f"/workspace/{CHECK_ENTRY}"),
            timeout=CHECK_TIMEOUT,
        ))
    except BoundaryError as exc:
        # A boundary that did not come up is not a failing check. Saying so keeps an
        # instrumentation failure from reading as a red product.
        print(f"CHECK_BOUNDARY_ERROR: {exc}", file=sys.stderr)
        return EXIT_BOUNDARY
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    return result.returncode


def stage_trusted_runtime(destination: Path, source: Path | None = None) -> Path:
    """Copy exactly the modules the launcher imports, and nothing that sits beside them."""
    source = source or Path(__file__).resolve().parent
    destination.mkdir(parents=True, exist_ok=True)
    for name in TRUSTED_RUNTIME_FILES:
        shutil.copyfile(source / name, destination / name)
    staged = sorted(p.name for p in destination.rglob("*") if p.is_file())
    if staged != sorted(TRUSTED_RUNTIME_FILES):
        raise RuntimeError(f"the staged runtime carries unexpected files: {staged}")
    return destination


def materialize(task_root: Path, workspace: Path, tools_dir: Path | None = None,
                staging: Path | None = None) -> Path:
    """Write `bin/check` into the runner package, outside the writable workspace.

    `workspace` and `tools_dir` are embedded verbatim, so the caller decides whether the
    launcher names host paths or in-view ones. The confined adapter path passes `/workspace`
    and `/b2-runtime`; nothing about the evaluator's filesystem is written into the file.
    When `staging` is given, the trusted runtime is copied there first.
    """
    if staging is not None:
        stage_trusted_runtime(staging)
    tools = str(tools_dir) if tools_dir is not None else str(Path(__file__).resolve().parent)
    bin_dir = task_root / BIN_DIR
    bin_dir.mkdir(parents=True, exist_ok=True)
    launcher = bin_dir / LAUNCHER_NAME
    launcher.write_text(TEMPLATE.format(tools=tools, workspace=str(workspace)), encoding="utf-8")
    launcher.chmod(stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
    return launcher


def path_with_launcher(task_root: Path, base_path: str | None = None) -> str:
    """PATH for the child process, with the adapter's bin/ first."""
    base = base_path if base_path is not None else os.environ.get("PATH", "/usr/bin:/bin")
    return f"{(task_root / BIN_DIR).resolve()}:{base}"


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--materialize", nargs=2, metavar=("TASK_ROOT", "WORKSPACE"))
    args = parser.parse_args(argv)
    if not args.materialize:
        parser.error("--materialize TASK_ROOT WORKSPACE is required")
    launcher = materialize(Path(args.materialize[0]), Path(args.materialize[1]))
    print(json.dumps({"launcher": str(launcher), "path": path_with_launcher(Path(args.materialize[0]))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
