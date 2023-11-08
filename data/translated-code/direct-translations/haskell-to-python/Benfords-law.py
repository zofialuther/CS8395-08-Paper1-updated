import Data.Map as M
from math import log10

def fstdigit(num):
    return int(str(num)[0])

n = 1000

fibs = [1, 1]
for i in range(2, n):
    fibs.append(fibs[-1] + fibs[-2])

fibdata = list(map(fstdigit, fibs[:n]))

freqs = dict()
for d in fibdata:
    if d in freqs:
        freqs[d] += 1
    else:
        freqs[d] = 1

tab = [(d, freqs.get(d, 0) / n, log10(1 + 1 / d)) for d in range(1, 10)]

print(tab)