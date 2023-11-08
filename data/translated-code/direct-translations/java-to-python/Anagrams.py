from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import functools
import collections
import array
import re

def tryWithResources(callable, function, defaultSupplier):
    def wrapper():
        try:
            with callable() as autoCloseable:
                return function(autoCloseable)
        except Exception as e:
            return defaultSupplier()
    return wrapper

def function(supplier):
    return lambda i: supplier()

if __name__ == "__main__":
    anagrams = collections.defaultdict(list)
    
    def process_word(word):
        chars = array.array('u', word)
        chars.fromunicode(sorted(chars))
        key = str(chars)
        anagrams[key].append(word)
        return len(anagrams[key])
    
    with urlopen("http://wiki.puzzlers.org/pub/wordlists/unixdict.txt") as response:
        count = tryWithResources(
            lambda: response,
            lambda reader: max(ThreadPoolExecutor().map(process_word, reader.read().decode('utf-8').splitlines())),
            lambda: 0
        )()
    
    for ana in filter(lambda ana: len(ana[1]) >= count, anagrams.items()):
        print(ana[1])