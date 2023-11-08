```python
from math import log2
from collections import Counter

def shannon_entropy(string):
    freq = Counter(string)
    total = len(string)
    entropy = -sum(frequency / total * log2(frequency / total) for frequency in freq.values())
    return entropy

# Example query
H = shannon_entropy("1223334444")
print(H)  # Output: 1.8464393446710154
```