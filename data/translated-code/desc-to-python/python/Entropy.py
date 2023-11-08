import math
from collections import Counter

def entropy(s):
    prob = [float(s.count(c))/len(s) for c in dict.fromkeys(list(s))]
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
    print(entropy)

entropy("1223334444")