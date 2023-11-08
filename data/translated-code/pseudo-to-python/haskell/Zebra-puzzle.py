```python
from itertools import permutations
from itertools import product

values = list(permutations([1, 2, 3, 4, 5]))

class Nation:
    English, Swede, Dane, Norwegian, German = range(1, 6)

class Color:
    Red, Green, White, Yellow, Blue = range(1, 6)

class Pet:
    Dog, Birds, Cats, Horse, Zebra = range(1, 6)

class Drink:
    Tea, Coffee, Milk, Beer, Water = range(1, 6)

class Smoke:
    PallMall, Dunhill, Blend, BlueMaster, Prince = range(1, 6)

answers = []
for color in values:
    if (color[1] == 3) and (color[0] < color[4]) and (color[4] == 3):
        for nation in values:
            if (nation[0] == 4):
                if (nation[0] == 1) and (color[1] == 1):
                    if abs(nation.index(4) - color.index(5)) == 1:
                        for drink in values:
                            if drink[2] == 3:
                                if (nation.index(3) == drink.index(1)):
                                    if (drink.index(2) == color.index(2)):
                                        for pet in values:
                                            if (nation.index(2) == pet.index(1)):
                                                for smoke in values:
                                                    if (smoke.index(1) == pet.index(2)):
                                                        if (color.index(4) == smoke.index(2)):
                                                            if abs(smoke.index(3) - pet.index(3)) == 1:
                                                                if abs(pet.index(3) - smoke.index(2)) == 1:
                                                                    if (nation.index(5) == smoke.index(5)):
                                                                        if (drink.index(5) == smoke.index(3)):
                                                                            answers.append(list(zip(nation, color, pet, drink, smoke)))

for answer in answers:
    for answ in answer:
        print(answ)
    print([nation for (nation, _, Zebra, _, _) in answer])
    print("")
print("No more solutions!")
```