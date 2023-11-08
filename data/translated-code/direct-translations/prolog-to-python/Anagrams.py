import urllib.request
from urllib.request import urlopen
from operator import itemgetter
from itertools import groupby

def anagrams():
    url = 'http://wiki.puzzlers.org/pub/wordlists/unixdict.txt'
    response = urlopen(url)
    words = response.read().decode('utf-8').split()

    # Sort the words
    words.sort()

    # Group words by sorted letters
    anagram_groups = []
    for key, group in groupby(words, key=lambda x: ''.join(sorted(x))):
        anagrams = list(group)
        if len(anagrams) > 1:
            anagram_groups.append(anagrams)

    # Sort the anagram groups by size
    anagram_groups.sort(key=len, reverse=True)

    # Print the first 6 groups
    for group in anagram_groups[:6]:
        print(group)

anagrams()