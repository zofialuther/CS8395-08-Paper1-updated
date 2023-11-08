```python
from random import randint, choice

class Person:

    def __init__(self, name, preference):
        self.name = name
        self.preference = preference
        self.status = "free"
        self.elu = None
        self.contact = []

class Man(Person):

    def propose(self):
        if self.status == "free":
            preference = self.preference
            pref = preference[0]
            self.preference = preference[1:]
            return pref
        else:
            return None

    def refuse(self):
        self.status = "free"

    def accept(self):
        self.status = "maybe"

class Woman(Person):

    def dispose(self):
        contact = self.contact
        elu = self.elu
        if elu:
            contact.append(elu)
        contact.sort(key=lambda x: x[0])
        choice = contact[0][1]
        choice.accept()
        self.status = "maybe"
        self.elu = choice
        for c in contact:
            c[1].refuse()
        self.contact = []

def get_two_random_couples(Len):
    C1 = randint(0, Len - 1)
    while True:
        C2 = randint(0, Len - 1)
        if C2 != C1:
            return C1, C2

def create_couple(woman, lst_couple):
    lst_couple.append((woman.elu.name, woman.name))

def round(lst_man, lst_woman):
    for man in lst_man:
        man.propose()
    for woman in lst_woman:
        woman.dispose()
        if not all(woman.status == "maybe" for woman in lst_woman):
            round(lst_man, lst_woman)
        else:
            return

def stability(lst_couple):
    couples = list(map(lambda x: (x[0].name, x[1].name), lst_couple))
    unstable_couples = []
    for i, c1 in enumerate(couples):
        for j, c2 in enumerate(couples[i+1:], i+1):
            if is_unstable(c1, c2):
                unstable_couples.append((c1, c2))
    if not unstable_couples:
        print("Couples are stable")
    else:
        print("Unstable couples are:")
        for couple in unstable_couples:
            print(couple[0], "and", couple[1])

def is_unstable(couple1, couple2):
    PX1 = couple1[0].preference
    PX2 = couple2[0].preference
    PY1 = couple1[1].preference
    PY2 = couple2[1].preference

    IY12 = PX1.index(couple2[1].name)
    IY11 = PX1.index(couple1[1].name)
    IX21 = PY2.index(couple1[0].name)
    IX22 = PY2.index(couple2[0].name)

    IY21 = PX2.index(couple1[1].name)
    IY22 = PX2.index(couple2[1].name)
    IX11 = PY1.index(couple1[0].name)
    IX12 = PY1.index(couple2[0].name)

    return (IY12 < IY11 and IX21 < IX22) or (IY21 < IY22 and IX12 < IX11)

# facts
prefere = {
    "abe": ["abi", "eve", "cath", "ivy", "jan", "dee", "fay", "bea", "hope", "gay"],
    "bob": ["cath", "hope", "abi", "dee", "eve", "fay", "bea", "jan", "ivy", "gay"],
    # ... and so on for all other persons
}

man_names = ["abe", "bob", "col", "dan", "ed", "fred", "gav", "hal", "ian", "jon"]
woman_names = ["abi", "bea", "cath", "dee", "eve", "fay", "gay", "hope", "ivy", "jan"]

men = [Man(name, prefere[name]) for name in man_names]
women = [Woman(name, prefere[name]) for name in woman_names]

lst_man = men
lst_woman = women

for man in lst_man:
    man.contact = lst_woman
for woman in lst_woman:
    woman.contact = lst_man

round(lst_man, lst_woman)
stability(list(zip(lst_man, lst_woman)))
```