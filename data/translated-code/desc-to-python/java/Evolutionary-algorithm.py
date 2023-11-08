```python
import random
import string

target_phrase = "METHINKS IT IS LIKE A WEASEL"
mutation_rate = 0.05

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + " ") for _ in range(length))

def calculate_fitness(mutated_string):
    return sum(1 for i in range(len(target_phrase)) if target_phrase[i] == mutated_string[i])

def mutate_string(current_string):
    return ''.join([random.choice(string.ascii_uppercase + " ") if random.random() < mutation_rate else current_string[i] for i in range(len(current_string)])

best_string = generate_random_string(len(target_phrase))
best_fitness = calculate_fitness(best_string)

iteration = 0
while best_fitness < len(target_phrase):
    iteration += 1
    mutated_string = mutate_string(best_string)
    mutated_fitness = calculate_fitness(mutated_string)
    
    if mutated_fitness > best_fitness:
        best_string = mutated_string
        best_fitness = mutated_fitness
    
    if iteration % 100 == 0:
        print(f"Iteration: {iteration}, Best String: {best_string}, Fitness: {best_fitness}")

    mutation_rate *= 0.99  # decrease mutation rate as fitness improves
```