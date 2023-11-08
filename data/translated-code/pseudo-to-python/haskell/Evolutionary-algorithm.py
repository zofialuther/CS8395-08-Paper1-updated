import random
import string

target = "METHINKS IT IS LIKE A WEASEL"
mutateRate = 0.1
popSize = 100
printEvery = 10

alphabet = list(string.ascii_uppercase + " ")

def randomChar():
    return random.choice(alphabet)

def createChar(c):
    return randomChar()

def fitness(str):
    return sum(1 for a, b in zip(target, str) if a == b)

def mutateChar(c):
    if random.random() < mutateRate:
        return randomChar()
    else:
        return c

def mutateArr(arr):
    return [mutateChar(c) for c in arr]

def converge(n, parent):
    if n % printEvery == 0:
        print(fmtd)
    if target == parent:
        print("\nFinal: " + fmtd)
    else:
        mutated = [mutateArr(parent) for _ in range(popSize-1)]
        mutated.append(parent)
        newParents = max(mutated, key=fitness)
        converge(n+1, newParents)
    fmtd = parent + ": " + str(fitness(parent)) + " (" + str(n) + ")"

def origin():
    return [createChar(c) for c in target]

main = converge(0, origin())