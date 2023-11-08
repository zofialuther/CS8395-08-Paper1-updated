```python
# facts
prefere = {
    "abe": ["abi", "eve", "cath", "ivy", "jan", "dee", "fay", "bea", "hope", "gay"],
    "bob": ["cath", "hope", "abi", "dee", "eve", "fay", "bea", "jan", "ivy", "gay"],
    "col": ["hope", "eve", "abi", "dee", "bea", "fay", "ivy", "gay", "cath", "jan"],
    "dan": ["ivy", "fay", "dee", "gay", "hope", "eve", "jan", "bea", "cath", "abi"],
    "ed": ["jan", "dee", "bea", "cath", "fay", "eve", "abi", "ivy", "hope", "gay"],
    "fred": ["bea", "abi", "dee", "gay", "eve", "ivy", "cath", "jan", "hope", "fay"],
    "gav": ["gay", "eve", "ivy", "bea", "cath", "abi", "dee", "hope", "jan", "fay"],
    "hal": ["abi", "eve", "hope", "fay", "ivy", "cath", "jan", "bea", "gay", "dee"],
    "ian": ["hope", "cath", "dee", "gay", "bea", "abi", "fay", "ivy", "jan", "eve"],
    "jon": ["abi", "fay", "jan", "gay", "eve", "bea", "dee", "cath", "ivy", "hope"],
    "abi": ["bob", "fred", "jon", "gav", "ian", "abe", "dan", "ed", "col", "hal"],
    "bea": ["bob", "abe", "col", "fred", "gav", "dan", "ian", "ed", "jon", "hal"],
    "cath": ["fred", "bob", "ed", "gav", "hal", "col", "ian", "abe", "dan", "jon"],
    "dee": ["fred", "jon", "col", "abe", "ian", "hal", "gav", "dan", "bob", "ed"],
    "eve": ["jon", "hal", "fred", "dan", "abe", "gav", "col", "ed", "ian", "bob"],
    "fay": ["bob", "abe", "ed", "ian", "jon", "dan", "fred", "gav", "col", "hal"],
    "gay": ["jon", "gav", "hal", "fred", "bob", "abe", "col", "ed", "dan", "ian"],
    "hope": ["gav", "jon", "bob", "abe", "ian", "dan", "hal", "ed", "col", "fred"],
    "ivy": ["ian", "col", "hal", "gav", "fred", "bob", "abe", "ed", "jon", "dan"],
    "jan": ["ed", "hal", "gav", "abe", "bob", "jon", "col", "ian", "fred", "dan"]
}

man = ["abe", "bob", "col", "dan", "ed", "fred", "gav", "hal", "ian", "jon"]
woman = ["abi", "bea", "cath", "dee", "eve", "fay", "gay", "hope", "ivy", "jan"]

# rules
class Person:
    def __init__(self, name, preference):
        self.name = name
        self.preference = preference
        self.status = "free"

class Man(Person):
    def propose(self):
        if self.status == "free":
            preferred_woman = self.preference.pop(0)
            return preferred_woman
        return None

class Woman(Person):
    def dispose(self, contact):
        if self.status == "free":
            self.status = "maybe"
            self.elu = contact
        else:
            self.status = "no"

def stable_mariage():
    men = [Man(name, prefere[name]) for name in man]
    women = [Woman(name, prefere[name]) for name in woman]

    # ... (other code)

stable_mariage()
```