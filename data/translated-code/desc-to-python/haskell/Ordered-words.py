```python
with open('unixdict.txt', 'r') as file:
    words = file.read().split()

sorted_words = filter(lambda word: list(word) == sorted(word), words)
longest_length = len(max(sorted_words, key=len))
longest_sorted_words = filter(lambda word: len(word) == longest_length, sorted_words)
print(list(longest_sorted_words))
```