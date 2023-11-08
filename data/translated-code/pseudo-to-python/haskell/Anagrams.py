```python
from itertools import groupby
from operator import itemgetter

def groupon(f, x, y):
    return f(x) == f(y)

def main():
    with open("./../Puzzels/Rosetta/unixdict.txt", "r") as file:
        words = file.read().splitlines()
        wix = [list(group) for key, group in groupby(sorted(zip(map(sorted, words), words), key=itemgetter(0)), key=lambda x: len(list(x[1])))]
        mxl = max(len(group) for group in wix)
        for group in wix:
            if len(group) == mxl:
                print(list(map(itemgetter(1), group)))

main()
```