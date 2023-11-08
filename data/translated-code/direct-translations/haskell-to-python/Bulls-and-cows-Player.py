```python
import itertools
import random

def combinationsOf(k, lst):
    if k == 0:
        return [[]]
    if not lst:
        return []
    return list(map(lambda x: [lst[0]] + x, combinationsOf(k-1, lst[1:])) + combinationsOf(k, lst[1:]))

def player():
    ps = list(itertools.permutations(['1','2','3','4','5','6','7','8','9'], 4))
    play(ps)

def play(ps):
    if not ps:
        print("Unable to find a solution")
    else:
        i = random.randint(0, len(ps) - 1)
        p = ''.join(ps[i])
        print("My guess is " + p)
        print("How many bulls and cows?")
        input_bc = takeInput()
        ps = [x for x in ps if sum(input_bc) == sum(1 for i, j in zip(x, p) if i == j) and input_bc[0] == sum(1 for i in x if i in p)]
        if len(ps) == 1:
            print("The answer is " + ''.join(ps[0]))
        else:
            play(ps)

def takeInput():
    inp = input()
    ui = list(map(int, [x for x in inp if x in '1234']))
    if sum(ui) > 4 or len(ui) != 2:
        print("Wrong input. Try again")
        return takeInput()
    else:
        return ui
```