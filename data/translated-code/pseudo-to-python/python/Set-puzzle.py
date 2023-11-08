import random
import pprint
from itertools import product, combinations

N_DRAW = 9
N_GOAL = N_DRAW // 2

deck = list(product("red green purple".split(),
                    "one two three".split(),
                    "oval squiggle diamond".split(),
                    "solid open striped".split()))

sets = []
while len(sets) != N_GOAL:
    draw = random.sample(deck, N_DRAW)
    sets = []
    for cs in combinations(draw, 3):
        valid_set = True
        for t in zip(*cs):
            if len(set(t)) not in [1, 3]:
                valid_set = False
                break
        if valid_set:
            sets.append(cs)

print("Dealt %d cards:" % len(draw))
pprint.pprint(draw)
print("\nContaining %d sets:" % len(sets))
pprint.pprint(sets)