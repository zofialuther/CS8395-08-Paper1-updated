```python
# Python code for the Weasel Program genetic algorithm
import random

# Parameters
target_phrase = "METHINKS IT IS LIKE A WEASEL"
gen_size = 100
mutation_rate = 0.05

# Initialize population
population = [''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ ", k=len(target_phrase))) for _ in range(gen_size)]

# Evolution loop
generation = 0
while True:
    fitness_scores = [(sum(c1 == c2 for c1, c2 in zip(phrase, target_phrase)), phrase) for phrase in population]
    best_fit = max(fitness_scores)
    print(f"Generation {generation}: {best_fit[1]} ({best_fit[0]}/{len(target_phrase)} matches)")
    if best_fit[1] == target_phrase:
        break
    new_population = []
    for _ in range(gen_size):
        parent = random.choice(population)
        child = ''.join(c if random.random() > mutation_rate else random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ ") for c in parent)
        new_population.append(child)
    population = new_population
    generation += 1
```