"""Day 3 — wire the stages into one end-to-end run.

This is the entry point for ``uv run de-pipeline``. By the end of the week it
should run the whole pipeline — fetch from S3 -> load into DuckDB -> run the
transforms — printing a short summary so a human can see what happened.
"""

from __future__ import annotations

# The stages you'll orchestrate. Each exposes the functions you wrote this week.
from de_pipeline import fetch, load, transform  # noqa: F401


def main() -> None:
    """Run the full pipeline end to end: fetch the source files, open a DuckDB
    connection, load the raw tables, run the transforms, and print a summary."""
    fetched = fetch.fetch_all()
    print("fetched:", {name: str(path) for name, path in fetched.items()})

    con = load.connect()
    loaded = load.load_all(con)
    print("loaded:", loaded)

    transformed = transform.run_transforms(con)
    print("transformed:", transformed)


if __name__ == "__main__":
    main()
