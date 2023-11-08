import urllib
import concurrent.futures
import collections
import functools
import itertools

def try_with_resources(callable, function, default_supplier):
    def inner():
        try:
            with callable() as auto_closeable:
                return function(auto_closeable)()
        except Exception as throwable:
            return default_supplier()
    return inner

def function(supplier):
    return lambda i: supplier()

if __name__ == "__main__":
    anagrams = collections.defaultdict(list)
    with urllib.request.urlopen("http://wiki.puzzlers.org/pub/wordlists/unixdict.txt") as response:
        words = response.read().decode('utf-8').splitlines()

    count = try_with_resources(
        lambda: itertools.chain(words),
        lambda reader: functools.partial(
            max,
            (
                len(anagrams[key]) or 0
                for key in (
                    ''.join(sorted(word))
                    for word in reader
                )
                if (anagrams[key] := anagrams[key]).append(word)
            )
        ),
        lambda: 0
    )()

    for ana in anagrams.values():
        if len(ana) >= count:
            print(ana)