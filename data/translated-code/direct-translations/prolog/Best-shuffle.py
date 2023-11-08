```python
from random import shuffle

score = {}

def best_shuffle():
    for s in ["abracadabra", "eesaw", "elk", "grrrrrr", "up", "a"]:
        best_shuffle_helper(s)

def best_shuffle_helper(s):
    score.clear()
    score[s] = len(s)
    min_val = calcule_min(s, len(s))
    while True:
        shuffled = list(s)
        shuffle(shuffled)
        result = [1 if s[i] == shuffled[i] else 0 for i in range(len(s))]
        value = sum(result)
        if s in score:
            if value < score[s]:
                score[shuffled] = value
        else:
            score[s] = value
        if value == min_val:
            del(score[s])
            print(f'{s} : {shuffled} ({value})')
            break

def calcule_min(s, length):
    sorted_str = sorted(s)
    packed = pack_list(sorted_str)
    packed.sort()
    n, _ = packed[-1]
    if n * 2 > length:
        return 2 * n - length
    else:
        return 0

def pack_list(lst):
    packed = []
    while lst:
        x = lst[0]
        if len(lst) == 1:
            packed.append([1, x])
            return packed
        else:
            count = 1
            for i in range(1, len(lst)):
                if lst[i] == x:
                    count += 1
                else:
                    packed.append([count, x])
                    lst = lst[i:]
                    break
            else:
                packed.append([count, x])
                return packed

best_shuffle()
```