```python
import sys

def select(menu):
    if not menu:
        return ""
    else:
        print(showMenu(menu))
        choice = input("Choose an item: ")
        chosen_item = choose(menu, choice)
        if chosen_item:
            return chosen_item
        else:
            return select(menu)

def showMenu(menu):
    return '\n'.join([str(n) + ") " + item for n, item in enumerate(menu, 1)])

def choose(menu, choice):
    try:
        n = int(choice)
        if n > 0:
            return menu[n-1]
        else:
            return None
    except ValueError:
        return None

def maybeRead(choice):
    try:
        return int(choice)
    except ValueError:
        return None

if __name__ == "__main__":
    menu = ["apple", "banana", "orange"]
    print(select(menu))
```