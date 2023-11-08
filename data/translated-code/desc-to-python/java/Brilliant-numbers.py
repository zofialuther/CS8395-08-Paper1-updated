```python
# Python code
# BrilliantNumbers.py

class PrimeGenerator:
    def __init__(self, limit):
        # implementation of prime number generation

def calculate_brilliant_numbers(limit):
    prime_gen = PrimeGenerator(limit)
    prime_numbers = prime_gen.generate_primes()
    
    brilliant_numbers = []
    for i in range(len(prime_numbers)):
        for j in range(i, len(prime_numbers)):
            brilliant_numbers.append(prime_numbers[i] * prime_numbers[j])
    
    brilliant_numbers.sort()
    
    print("First 100 brilliant numbers:")
    print(brilliant_numbers[:100])
    
    for power in range(1, 6):
        for num in brilliant_numbers:
            if num >= 10 ** power:
                print(f"The first brilliant number greater than or equal to 10^{power} is: {num}")
                break

calculate_brilliant_numbers(1000)
```