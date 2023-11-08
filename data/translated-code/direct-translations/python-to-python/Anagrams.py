import urllib.request
from collections import defaultdict
words = urllib.request.urlopen('http://wiki.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
print(len(words))
anagram = defaultdict(list) # map sorted chars to anagrams
for word in words:
    anagram[tuple(sorted(word))].append( word )

count = max(len(ana) for ana in anagram.values())
for ana in anagram.values():
    if len(ana) >= count:
        print(ana)

print(count)