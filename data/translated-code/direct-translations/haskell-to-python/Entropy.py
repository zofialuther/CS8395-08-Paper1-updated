from collections import Counter
import math

def entropy(data):
    frequency = Counter(data)
    total = len(data)
    probabilities = [count / total for count in frequency.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return entropy

result = entropy("1223334444")
print(result)