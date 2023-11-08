```python
import random
import string

target_sequence = "METHINKS IT IS LIKE A WEASEL"
mutation_rate = 0.05
population_size = 100
alphabet = string.ascii_uppercase + " "

def generate_random_sequence(length):
    return ''.join(random.choice(alphabet) for _ in range(length))

def calculate_fitness(sequence):
    return sum(1 for i in range(len(target_sequence)) if sequence[i] == target_sequence[i])

def mutate_sequence(sequence, mutation_rate):
    return ''.join(c if random.random() > mutation_rate else random.choice(alphabet) for c in sequence)

current_sequence = generate_random_sequence(len(target_sequence))
iterations = 0

while current_sequence != target_sequence:
    iterations += 1
    current_fitness = calculate_fitness(current_sequence)
    print(f"Iteration: {iterations}, Current Sequence: {current_sequence}, Fitness: {current_fitness}")

    new_population = [mutate_sequence(current_sequence, mutation_rate) for _ in range(population_size)]
    current_sequence = max(new_population, key=calculate_fitness)

    if iterations % 100 == 0:
        print(f"Iteration: {iterations}, Current Sequence: {current_sequence}, Fitness: {current_fitness}")

    mutation_rate *= 0.95

print(f"Final Sequence: {current_sequence}, Target Sequence: {target_sequence}")
```