```python
def isOrdered(word):
    return list(word) == sorted(word)

with open('unixdict.txt', 'r') as file:
    words = file.read().split()

ordered_words = [word for word in words if isOrdered(word)]
longest_ordered_word = max(ordered_words, key=len)
print(longest_ordered_word)
```