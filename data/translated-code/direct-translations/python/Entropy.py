import math
from collections import Counter

def entropy(s):
    p, lns = Counter(s), float(len(s))
    return math.log2(lns) - sum(count * math.log2(count) for count in p.values()) / lns

print(entropy("1223334444"))