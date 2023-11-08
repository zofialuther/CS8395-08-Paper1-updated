```python
def rosetta_menu(items, selected_item):
    if not items:
        return
    while True:
        display_menu(items)
        choice = int(input("Select a menu item by number: "))
        if 1 <= choice <= len(items):
            selected_item = items[choice - 1]
            break

def display_menu(items):
    print()
    for index, item in enumerate(items, start=1):
        print(f"{index}) {item}")

def get_choice():
    return int(input("Select a menu item by number: "))
```