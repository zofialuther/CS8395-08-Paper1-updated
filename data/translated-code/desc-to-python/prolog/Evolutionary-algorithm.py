```python
import random
import string

def generate_random_text(length):
    return ''.join(random.choice(string.ascii_letters + ' ') for _ in range(length))

def calculate_score(target, text):
    return sum(1 for i in range(len(target)) if target[i] != text[i])

def mutate_text(text, mutation_rate):
    return ''.join(c if random.random() > mutation_rate else random.choice(string.ascii_letters + ' ') for c in text)

def weasel(target, initial_text, mutation_rate):
    best_text = initial_text
    best_score = calculate_score(target, initial_text)
    
    while best_score > 0:
        mutated_text = mutate_text(best_text, mutation_rate)
        score = calculate_score(target, mutated_text)
        
        if score < best_score:
            best_text = mutated_text
            best_score = score
    
    return best_text
```