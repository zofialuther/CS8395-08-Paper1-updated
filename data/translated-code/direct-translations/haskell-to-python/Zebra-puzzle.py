from itertools import permutations
from itertools import product

def same(lst1, item1, lst2, item2):
    return (item1, item2) in list(zip(lst1, lst2))

def leftOf(lst1, item1, lst2, item2):
    return same(lst1, item1, lst2[1:], item2)

def nextTo(lst1, item1, lst2, item2):
    return leftOf(lst1, item1, lst2, item2) or leftOf(lst2, item2, lst1, item1)

def middle(lst, item):
    return lst.index(item) == 2

def first(lst, item):
    return lst[0] == item

values = list(permutations([Nation for Nation in range(5)]))

colors = list(product(Color, repeat=5))
nations = list(product(Nation, repeat=5))
pets = list(product(Pet, repeat=5))
drinks = list(product(Drink, repeat=5))
smokes = list(product(Smoke, repeat=5))

answers = []

for color in colors:
    if leftOf(color, Green, color, White):
        for nation in nations:
            if first(nation, Norwegian) and same(nation, English, color, Red) and nextTo(nation, Norwegian, color, Blue):
                for drink in drinks:
                    if middle(drink, Milk) and same(nation, Dane, drink, Tea) and same(drink, Coffee, color, Green):
                        for pet in pets:
                            if same(nation, Swede, pet, Dog):
                                for smoke in smokes:
                                    if same(smoke, PallMall, pet, Birds) and same(color, Yellow, smoke, Dunhill) and nextTo(smoke, Blend, pet, Cats) and nextTo(pet, Horse, smoke, Dunhill) and same(nation, German, smoke, Prince) and same(smoke, BlueMaster, drink, Beer) and nextTo(drink, Water, smoke, Blend):
                                        answers.append(list(zip(nation, color, pet, drink, smoke)))

for answer in answers:
    for item in answer:
        print(item)
    print([nation for (nation, _, Zebra, _, _) in answer])
    print("")

print("No more solutions!")