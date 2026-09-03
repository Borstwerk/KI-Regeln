"""Keep the guarded artifacts out of this repository's own test run.

`canonical/guarded/test_discount.py` and its per-control copies are *data*: they are the
measurement surface the engine grades, deliberately identical in name across the canonical
tree and every workspace so that a byte comparison is meaningful. They are not tests of
this repository, and pytest's rootdir collection would otherwise both try to import them
and fail on the duplicate basenames.

Ignoring them here does not relax any check. `tests/test_verification_surface.py` is what
actually exercises this directory, and it reads these files as bytes rather than importing
them.
"""

collect_ignore_glob = ["**/guarded/*.py"]
