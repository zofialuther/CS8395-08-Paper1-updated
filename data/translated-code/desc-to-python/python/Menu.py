```python
def _menu(items):
    for i, item in enumerate(items):
        print(f"{i+1}. {item}")

def _ok(choice, items):
    return choice.isdigit() and 1 <= int(choice) <= len(items)

def selector(items):
    _menu(items)
    choice = input("Select an item: ")
    while not _ok(choice, items):
        print("Invalid selection. Please try again.")
        choice = input("Select an item: ")
    return items[int(choice)-1]

story_items = ["Straw House", "Stick House", "Brick House"]
chosen_item = selector(story_items)
print(f"You chose the {chosen_item}.")
```