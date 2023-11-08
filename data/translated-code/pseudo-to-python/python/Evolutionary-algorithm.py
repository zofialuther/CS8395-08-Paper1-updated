```python
from string import ascii_uppercase, ascii_lowercase, digits, punctuation, whitespace
from random import choice, random

target = list("METHINKS IT IS LIKE A WEASEL")
charset = ascii_uppercase + ascii_lowercase + digits + punctuation + whitespace
parent = [choice(charset) for _ in range(len(target))]
minmutaterate = 0.09
C = range(100)

perfectfitness = float(len(target))

def fitness(trial):
    return sum(1 for a, b in zip(trial, target) if a == b)

def mutaterate():
    return 1 - ((perfectfitness - fitness(parent)) / perfectfitness) * (1 - minmutaterate)

def mutate(parent, rate):
    return [p if random() > rate else choice(charset) for p in parent]

def que():
    print(f"Iteration: {iterations}, Fitness: {fitness(parent)/perfectfitness*100}%, Parent: {''.join(parent)}")

def mate(a, b):
    if random() < 0.7:
        return a, b
    else:
        i = choice(range(len(a)))
        return a[:i] + b[i:], b[:i] + a[i:]

iterations = 0
center = len(C) // 2
while parent != target:
    rate = mutaterate()
    iterations += 1
    if iterations % 100 == 0:
        que()
    copies = [mutate(parent, rate) for _ in C]
    parent1 = max(copies[:center], key=fitness)
    parent2 = max(copies[center:], key=fitness)
    parent = max(mate(parent1, parent2), key=fitness)

que()
```