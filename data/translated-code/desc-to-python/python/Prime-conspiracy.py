```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    num = 2
    while len(primes) < limit:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def count_digit_transitions(primes):
    transitions = {}
    for i in range(len(primes) - 1):
        curr_digit = str(primes[i])[-1]
        next_digit = str(primes[i + 1])[-1]
        transition = (curr_digit, next_digit)
        transitions[transition] = transitions.get(transition, 0) + 1
    return transitions

limit = 100
primes = generate_primes(limit)
digit_transitions = count_digit_transitions(primes)
print(digit_transitions)
```