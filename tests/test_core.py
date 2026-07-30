"""Unit tests for ItemManager (run with: pytest)."""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from app.core import ItemManager


def make_manager(tmp_path):
    """Create an ItemManager backed by a temporary file."""
    return ItemManager(str(tmp_path / "data" / "items.txt"))


def test_add_item(tmp_path):
    m = make_manager(tmp_path)
    m.add_item("apples")
    assert m.items == ["apples"]


def test_remove_item(tmp_path):
    m = make_manager(tmp_path)
    m.add_item("first")
    m.add_item("second")
    m.remove_item(0)
    assert m.items == ["second"]


def test_remove_invalid_index_is_safe(tmp_path):
    m = make_manager(tmp_path)
    m.add_item("only")
    m.remove_item(5)  # out of range must not crash or delete
    assert m.items == ["only"]


def test_items_persist_between_sessions(tmp_path):
    m1 = make_manager(tmp_path)
    m1.add_item("kept")
    m2 = make_manager(tmp_path)  # fresh instance, same file
    assert m2.items == ["kept"]
