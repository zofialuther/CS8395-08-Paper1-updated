```python
class RosettaSelect:
    def __init__(self):
        pass
    
    def select(self, items):
        user_choice = self.showMenu(items)
        return self.choose(user_choice, items)

    def showMenu(self, items):
        for i in range(len(items)):
            print(f"{i+1}. {items[i]}")
        return int(input("Choose an item: "))

    def choose(self, user_choice, items):
        if user_choice > 0 and user_choice <= len(items):
            return items[user_choice - 1]
        else:
            return None

    def maybeRead(self, user_input):
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input")
            return None
```