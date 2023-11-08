```python
def commaQuibble(s):
    return ', '.join(s[:-1]) + ' and ' + s[-1]

sequences = [[], ['apple'], ['apple', 'banana'], ['apple', 'banana', 'cherry', 'date']]

for sequence in sequences:
    print(sequence, commaQuibble(sequence))
```