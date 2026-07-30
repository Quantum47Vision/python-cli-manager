# app/storage.py
import os

class StorageHandler:
    """Handles reading and writing items to a plain text file."""

    def __init__(self, file_path: str):
        """Initialize with a file path."""
        self.file_path = file_path
        # Ensure the folder exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    def load_items(self):
        """Load items from the file. Returns a list of strings."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            # Return empty list if file does not exist
            return []

    def save_items(self, items: list):
        """Save the list of items to the file."""
        with open(self.file_path, "w", encoding="utf-8") as f:
            for item in items:
                f.write(f"{item}\n")
