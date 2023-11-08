import requests
from collections import defaultdict

url = 'https://example.com/words.txt'
response = requests.get(url)
words = response.text.split()

groups = defaultdict(list)
for word in words:
    groups[''.join(sorted(word))].append(word)

max_anagrams = max(groups.values(), key=len)
print(max_anagrams)

max_anagram_count = len(max_anagrams)
print(max_anagram_count)