```python
import random

target = "METHINKS IT IS LIKE A WEASEL"
possibilities = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
C = 100  # number of spawn per generation
minMutateRate = 0.09
perfectFitness = len(target)
parent = ""
rand = random.Random()

def fitness(trial):
    retVal = 0
    for i in range(len(trial)):
        if trial[i] == target[i]:
            retVal += 1
    return retVal

def newMutateRate():
    return ((perfectFitness - fitness(parent)) / perfectFitness * (1 - minMutateRate))

def mutate(parent, rate):
    retVal = ""
    for i in range(len(parent)):
        retVal += possibilities[rand.randint(0, len(possibilities)-1)] if rand.random() <= rate else parent[i]
    return retVal

parent = mutate(target, 1)
iter = 0
while target != parent:
    rate = newMutateRate()
    iter += 1
    if iter % 100 == 0:
        print(f"{iter}: {parent}, fitness: {fitness(parent)}, rate: {rate}")
    bestSpawn = None
    bestFit = 0
    for i in range(C):
        spawn = mutate(parent, rate)
        fit = fitness(spawn)
        if fit > bestFit:
            bestSpawn = spawn
            bestFit = fit
    parent = bestSpawn if bestFit > fitness(parent) else parent

print(f"{parent}, {iter}")
```