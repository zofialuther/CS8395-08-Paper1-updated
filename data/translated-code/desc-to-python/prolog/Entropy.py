```python
# shannon_entropy.py

import math

def shannon_entropy(input_string):
    probabilities = [float(input_string.count(c)) / len(input_string) for c in dict.fromkeys(list(input_string))]
    shannon_entropy = -sum(p * math.log(p) / math.log(2.0) for p in probabilities)
    return shannon_entropy

def calculate_relative_frequencies(input_string):
    frequencies = {c: input_string.count(c) / len(input_string) for c in dict.fromkeys(list(input_string))}
    return frequencies

def run_length_encoding(input_string):
    # implementation for run-length encoding

def calculate_logarithm(number):
    return math.log(number)

def sum_numbers(numbers):
    return sum(numbers)

# Example usage
input_string1 = "hello world"
input_string2 = "abracadabra"
entropy1 = shannon_entropy(input_string1)
entropy2 = shannon_entropy(input_string2)
print("Shannon Entropy of input_string1:", entropy1)
print("Shannon Entropy of input_string2:", entropy2)

frequencies1 = calculate_relative_frequencies(input_string1)
frequencies2 = calculate_relative_frequencies(input_string2)
print("Relative frequencies of input_string1:", frequencies1)
print("Relative frequencies of input_string2:", frequencies2)
```