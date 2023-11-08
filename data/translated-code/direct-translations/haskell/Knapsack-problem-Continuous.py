from operator import itemgetter
from functools import cmp_to_key
from itertools import accumulate
from bisect import bisect

items = [
    ("beef", (36, 3.8)),
    ("pork", (43, 5.4)),
    ("ham", (90, 3.6)),
    ("greaves", (45, 2.4)),
    ("flitch", (30, 4.0)),
    ("brawn", (56, 2.5)),
    ("welt", (67, 3.7)),
    ("salami", (95, 3.0)),
    ("sausage", (98, 5.9))
]

def solution(k, items):
    items = sorted(items, key=lambda x: x[1][0]/x[1][1], reverse=True)
    for name, (value, weight) in items:
        if k >= weight:
            print(f"Take all the {name}")
            k -= weight
        else:
            print(f"Take {k:.2f} kg of the {name}")
            k = 0
            break

solution(15, items)
