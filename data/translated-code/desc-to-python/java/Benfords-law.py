```python
import math

def first_digit(num):
    while num >= 10:
        num //= 10
    return num

def benfords_law_freq(digit):
    return math.log10(1 + 1/digit)

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def count_first_digit_freq(sequence):
    freq_count = {str(i): 0 for i in range(1, 10)}
    for num in sequence:
        first_dig = int(str(num)[0])
        freq_count[str(first_dig)] += 1
    return freq_count

def compare_to_benfords_law(freq_count, n):
    expected_freq = {str(i): benfords_law_freq(i) * n for i in range(1, 10)}
    for digit in freq_count:
        observed = freq_count[digit] / n
        expected = expected_freq[digit]
        print(f"Observed frequency of {digit}: {observed:.4f}, Expected frequency: {expected:.4f}")

n = 100
fib_sequence = fibonacci(n)
freq_count = count_first_digit_freq(fib_sequence)
compare_to_benfords_law(freq_count, n)
```