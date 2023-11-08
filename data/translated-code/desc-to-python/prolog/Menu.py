```python
def rosetta_menu(items, selected_item):
    if not items:
        return ""
    
    print("Menu:")
    for i, item in enumerate(items):
        print(f"{i+1}. {item}")
    
    while True:
        try:
            choice = int(input("Select an item by entering its number: "))
            if 1 <= choice <= len(items):
                return items[choice-1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
```