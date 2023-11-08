import random

def shuffle(xs):
    goal = list(range(1, 10))
    if xs != goal:
        return xs
    else:
        return shuffle(random.sample(xs, len(xs)))

def prefixFlipAt(k, lst):
    return lst[:k][::-1] + lst[k:]

def prompt(r, ry):
    print(str(r) + ". " + ' '.join([str(x) for x in ry]) + " How many to flip? ")
    answ = int(input())
    if answ < 10 and answ > 0:
        return answ
    else:
        print("Error. The number should be between 0 and 10. Try again")
        return prompt(r, ry)

def playNRG(r, nrs):
    goal = list(range(1, 10))
    if nrs == goal:
        print("The answer is: " + ' '.join([str(x) for x in nrs]))
        print("It took you " + str(r) + " attempts to sort the numbers.")
        print("")
    else:
        answ = prompt(r, nrs)
        playNRG(r + 1, prefixFlipAt(answ, nrs))

goal = list(range(1, 10))
start = random.sample(goal, len(goal))

playNRG(1, start)