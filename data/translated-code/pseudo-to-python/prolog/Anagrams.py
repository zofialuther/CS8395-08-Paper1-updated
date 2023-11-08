```python
import urllib.request

def anagrams():
    url = 'http://wiki.puzzlers.org/pub/wordlists/unixdict.txt'
    response = urllib.request.urlopen(url)
    data = response.read()
    Out = data.splitlines()
    response.close()
    MOut = sorted(Out)
    GPL = {}
    for word in MOut:
        key = ''.join(sorted(word))
        if key in GPL:
            GPL[key].append(word)
        else:
            GPL[key] = [word]
    GPLSort = sorted(GPL.items(), key=lambda x: len(x[1]), reverse=True)
    T1, T2, T3, T4, T5, T6 = GPLSort[:6]
    L = [str(pair[1]) for pair in [T1, T2, T3, T4, T5, T6]]
    for item in L:
        print(item)

def read_file():
    L1 = []
    while True:
        line = input().strip()
        if not line:
            break
        L1.append(line)
    return L1

def my_compare(KeyValues):
    KeyValues.sort(key=lambda x: (len(x[1]), x[0]))

```