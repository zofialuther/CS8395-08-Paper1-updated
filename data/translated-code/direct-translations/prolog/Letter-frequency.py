```python
from collections import Counter

def frequency(file):
    with open(file, 'r') as f:
        data = f.read().replace('\n', '')
    
    # count frequency of each character
    freq = Counter(data)
    
    # sort and print the frequency
    for char, count in sorted(freq.items()):
        print(f"Number of {char.upper()} : {count}")

# Example usage
frequency('file.txt')
```