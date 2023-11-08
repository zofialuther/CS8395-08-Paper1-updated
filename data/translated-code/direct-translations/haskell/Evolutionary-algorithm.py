```python
import random
import string

target = "METHINKS IT IS LIKE A WEASEL"
mutateRate = 0.1
popSize = 100
printEvery = 10

alphabet = list(string.ascii_uppercase + ' ')

randomChar = lambda: random.choice(alphabet)

origin = [randomChar() for _ in range(len(target))]

def fitness(word):
    return sum(1 for a, b in zip(word, target) if a == b)

def mutate(word):
    return [randomChar() if random.random() < mutateRate else c for c in word]

def converge(n, parent):
    fmtd = parent + ": " + str(fitness(parent)) + " (" + str(n) + ")"
    if n % printEvery == 0:
        print(fmtd)
    if parent == target:
        print("\nFinal: " + fmtd)
    else:
        mutated = [mutate(parent) for _ in range(popSize-1)]
        next_parents = mutated + [parent]
        fitness_scores = [(word, fitness(word)) for word in next_parents]
        next_parent = max(fitness_scores, key=lambda x: x[1])[0]
        converge(n+1, next_parent)

converge(0, origin)
```