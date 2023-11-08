import random

target = "METHINKS IT IS LIKE A WEASEL"
possibilities = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
C = 100
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
        if rand.random() <= rate:
            retVal += possibilities[rand.randint(0, len(possibilities) - 1)]
        else:
            retVal += parent[i]
    return retVal

def main():
    global parent
    parent = mutate(target, 1)
    iter = 0
    while target != parent:
        rate = newMutateRate()
        iter += 1
        if iter % 100 == 0:
            print(str(iter) + ": " + parent + ", fitness: " + str(fitness(parent)) + ", rate: " + str(rate))
        bestSpawn = None
        bestFit = 0
        for i in range(C):
            spawn = mutate(parent, rate)
            fit = fitness(spawn)
            if fit > bestFit:
                bestSpawn = spawn
                bestFit = fit
        parent = bestSpawn if bestFit > fitness(parent) else parent
    print(parent + ", " + str(iter))

main()