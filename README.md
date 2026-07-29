# Python CLI Manager

A small command-line item manager written as a clean-code exercise: strict
separation between the interface, the business logic, and the storage layer.

## Why it exists

Small on purpose. The point is structure, not features — the storage backend
can be swapped for SQLite without touching the CLI, and the logic is fully
testable without the interface.

## Structure

```
main.py            entry point
app/cli.py         terminal interface (colors, confirmations)
app/core.py        ItemManager — the business logic
app/storage.py     file persistence
tests/test_core.py pytest unit tests
```

## Run

```
python main.py
```

## Test

```
pip install pytest
pytest
```

Items are stored in `data/items.txt`, created automatically on first run.
