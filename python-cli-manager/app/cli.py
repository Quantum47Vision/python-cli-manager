# app/cli.py
from app.core import ItemManager

# ANSI color codes for terminal output
class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"

def colored(text: str, color: str) -> str:
    """Wrap text in ANSI color codes."""
    return f"{color}{text}{Colors.END}"

def confirm(prompt: str) -> bool:
    """Ask the user for confirmation. Returns True if yes."""
    while True:
        response = input(colored(f"{prompt} (y/n): ", Colors.WARNING)).strip().lower()
        if response in ("y", "yes"):
            return True
        elif response in ("n", "no"):
            return False
        else:
            print(colored("Please enter 'y' or 'n'.", Colors.FAIL))

def run_cli():
    """Run the enhanced CLI with colors and confirmations."""
    manager = ItemManager("data/items.txt")
    print(colored("Welcome to the Python CLI App!\n", Colors.HEADER))

    while True:
        print(colored("\nOptions:", Colors.OKBLUE))
        print("  list   - Show all items")
        print("  add    - Add a new item")
        print("  remove - Remove an item by number")
        print("  quit   - Exit the program")

        choice = input(colored("\nEnter command: ", Colors.OKCYAN)).strip().lower()

        if choice == "list":
            manager.list_items()
        elif choice == "add":
            item = input(colored("Enter item name: ", Colors.OKCYAN)).strip()
            if item:
                manager.add_item(item)
            else:
                print(colored("Cannot add empty item.", Colors.FAIL))
        elif choice == "remove":
            if not manager.items:
                print(colored("No items to remove.", Colors.WARNING))
                continue
            try:
                index = int(input(colored("Enter item number to remove: ", Colors.OKCYAN))) - 1
                if 0 <= index < len(manager.items):
                    if confirm(f"Are you sure you want to remove '{manager.items[index]}'?"):
                        manager.remove_item(index)
                    else:
                        print(colored("Action cancelled.", Colors.WARNING))
                else:
                    print(colored("Invalid index.", Colors.FAIL))
            except ValueError:
                print(colored("Please enter a valid number.", Colors.FAIL))
        elif choice == "quit":
            print(colored("Goodbye!", Colors.OKGREEN))
            break
        else:
            print(colored("Unknown command. Please try again.", Colors.FAIL))
