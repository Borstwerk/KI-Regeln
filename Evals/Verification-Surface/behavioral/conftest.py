"""Keep the synthetic B2 workspaces out of this repository's own test run.

`workspace-base/checks/test_discount.py` and its per-case copies are *data*: they are the
measurement surface a synthetic agent workspace is graded on, deliberately identical in name
across the base and every seed so that a byte comparison is meaningful. They are not tests of
this repository, and collecting them would both fail on the duplicate basenames and write
`__pycache__` into the seeds — which then shows up as an undeclared change in the very diff
the grader measures.

Ignoring them relaxes no check. `tests/test_verification_surface_b2_implementation.py` is
what exercises this directory, and it reads these files as bytes or runs them inside the
execution boundary rather than importing them here.
"""

collect_ignore_glob = ["workspace-base/**", "cases/**", "oracle/**"]
