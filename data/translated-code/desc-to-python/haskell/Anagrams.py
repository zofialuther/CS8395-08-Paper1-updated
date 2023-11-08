```python
from collections import defaultdict

def group_anagrams(file_name):
    anagrams = defaultdict(list)

    with open(file_name, 'r') as file:
        words = file.read().splitlines()

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    max_group = max(anagrams.values(), key=len)
    print(max_group)

group_anagrams('file_name.txt')
```