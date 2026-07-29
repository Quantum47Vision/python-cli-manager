# app/core.py
from app.storage import StorageHandler

class ItemManager:
    """Manages a collection of items in the application."""

    def __init__(self, storage_file: str):
        """Initialize with a storage handler and load existing items."""
        self.storage = StorageHandler(storage_file)
        self.items = self.storage.load_items()

    def list_items(self):
        """Print all items with their index."""
        if not self.items:
            print("No items found.")
            return
        print("\nCurrent Items:")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item}")

    def add_item(self, item: str):
        """Add a new item to the collection and persist."""
        self.items.append(item)
        self.storage.save_items(self.items)
        print(f"Added item: {item}")

    def remove_item(self, index: int):
        """Remove an item by its index (0-based)."""
        if 0 <= index < len(self.items):
            removed = self.items.pop(index)
            self.storage.save_items(self.items)
            print(f"Removed item: {removed}")
        else:
            print("Invalid index. No item removed.")
