```python
import urllib
from collections import defaultdict

words = urllib.urlopen("http://wiki.puzzlers.org/pub/wordlists/unixdict.txt").read().split()
word_length = len(words)
anagram = defaultdict(list)

for word in words:
    sorted_word = ''.join(sorted(word))
    anagram[sorted_word].append(word)

count = max(len(anagram_list) for anagram_list in anagram.values())

for anagram_list in anagram.values():
    if len(anagram_list) >= count:
        print(anagram_list)

count = count
```