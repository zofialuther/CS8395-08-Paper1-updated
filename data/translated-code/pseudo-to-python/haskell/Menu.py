```python
import re

def select(menu):
    if not menu:
        return ""
    else:
        print(showMenu(menu))
        choice = input("Choose an item: ")
        result = choose(menu, choice)
        if result:
            return result
        else:
            return select(menu)

def showMenu(menu):
    return "\n".join([str(n) + ") " + item for n, item in enumerate(menu, start=1)])

def choose(menu, choice):
    try:
        n = int(choice)
        if n > 0:
            return menu[n-1]
    except ValueError:
        return None

def maybeRead(s):
    try:
        return int(s)
    except ValueError:
        return None
```