from random import shuffle

def best_shuffle():
    for word in ["abracadabra", "eesaw", "elk", "grrrrrr", "up", "a"]:
        best_shuffle(word)

def best_shuffle(Str):
    score = len(Str)
    min_val = calcule_min(Str, len(Str))
    
    while True:
        Shuffled = list(Str)
        shuffle(Shuffled)
        
        V = sum(comp(Str[i], Shuffled[i]) for i in range(len(Str)))
        
        if V < score:
            score = V
        elif V == min_val:
            print(f"String: {Str}, Current Score: {score}, Previous Score: {min_val}")
            break

def comp(a, b):
    return 1 if a == b else 0

def calcule_min(string, length):
    sorted_str = ''.join(sorted(string))
    packed = packList(sorted_str)
    min_val = len(packed[0][1])
    return min_val

def packList(lst):
    if len(lst) == 1:
        return [[lst[0], 1]]
    
    result = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            result.append([lst[i], 1])
        else:
            result[-1][1] += 1
    return result

def run(var, lst):
    if len(lst) == 0:
        return [[var, 1]]
    elif lst[-1][0] == var:
        lst[-1][1] += 1
    else:
        lst.append([var, 1])
    return lst
```