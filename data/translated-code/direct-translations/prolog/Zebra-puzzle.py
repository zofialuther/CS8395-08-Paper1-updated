from itertools import permutations
import numpy as np

def zebra():
    Nation = ['Englishman', 'Spaniard', 'Japanese', 'Ukrainian', 'Norwegian']
    Color = ['Red', 'Green', 'White', 'Yellow', 'Blue']
    Smoke = ['Oldgold', 'Kools', 'Chesterfield', 'Luckystrike', 'Parliament']
    Pet = ['Dog', 'Snails', 'Fox', 'Horse', 'Zebra']
    Drink = ['Tea', 'Coffee', 'Milk', 'Orangejuice', 'Water']

    # create permutations for all categories
    for perm in permutations([1, 2, 3, 4, 5]):
        # assign values to each category
        nation_values = {Nation[i]: perm[i] for i in range(5)}
        color_values = {Color[i]: perm[i] for i in range(5)}
        smoke_values = {Smoke[i]: perm[i] for i in range(5)}
        pet_values = {Pet[i]: perm[i] for i in range(5)}
        drink_values = {Drink[i]: perm[i] for i in range(5)}

        # apply the constraints
        if (nation_values['Englishman'] == color_values['Red'] and
                nation_values['Spaniard'] == pet_values['Dog'] and
                color_values['Green'] == drink_values['Coffee'] and
                nation_values['Ukrainian'] == drink_values['Tea'] and
                color_values['Green'] == color_values['White'] - 1 and
                smoke_values['Oldgold'] == pet_values['Snails'] and
                color_values['Yellow'] == smoke_values['Kools'] and
                drink_values['Milk'] == 3 and
                nation_values['Norwegian'] == 1 and
                (smoke_values['Chesterfield'] == pet_values['Fox'] - 1 or
                 smoke_values['Chesterfield'] == pet_values['Fox'] + 1) and
                (smoke_values['Kools'] == pet_values['Horse'] - 1 or
                 smoke_values['Kools'] == pet_values['Horse'] + 1) and
                smoke_values['Luckystrike'] == drink_values['Orangejuice'] and
                nation_values['Japanese'] == smoke_values['Parliament'] and
                (nation_values['Norwegian'] == color_values['Blue'] - 1 or
                 nation_values['Norwegian'] == color_values['Blue'] + 1)):

            # print the solution
            for k, v in sorted(nation_values.items(), key=lambda item: item[1]):
                print(k, '-', v)
            for k, v in sorted(color_values.items(), key=lambda item: item[1]):
                print(k, '-', v)
            for k, v in sorted(smoke_values.items(), key=lambda item: item[1]):
                print(k, '-', v)
            for k, v in sorted(pet_values.items(), key=lambda item: item[1]):
                print(k, '-', v)
            for k, v in sorted(drink_values.items(), key=lambda item: item[1]):
                print(k, '-', v)

zebra()