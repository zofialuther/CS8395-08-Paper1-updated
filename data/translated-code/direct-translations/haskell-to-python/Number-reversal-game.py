import random

def knuthShuffle(arr):
    random.shuffle(arr)
    return arr

def prefixFlipAt(k, arr):
    return arr[:k][::-1] + arr[k:]

def prompt(r, ry):
    answ = int(input(str(r) + ". " + " ".join(map(str, ry)) + " How many to flip? "))
    if 0 < answ < 10:
        return answ
    else:
        print("Error. The number should be between 0 and 10. Try again")
        return prompt(r, ry)

def playNRG(r, nrs):
    goal = [1,2,3,4,5,6,7,8,9]
    if nrs == goal:
        print("The answer is: " + " ".join(map(str, nrs)))
        print("It took you " + str(r) + " attempts to sort the numbers.\n")
    else:
        answ = prompt(r, nrs)
        playNRG(r + 1, prefixFlipAt(answ, nrs))

start = knuthShuffle([1,2,3,4,5,6,7,8,9])
playNRG(1, start)