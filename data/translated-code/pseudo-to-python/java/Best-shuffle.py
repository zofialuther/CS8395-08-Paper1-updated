```python
import random

def main():
    words = ["abracadabra", "seesaw", "grrrrrr", "pop", "up", "a"]
    for w in words:
        print(bestShuffle(w))

def bestShuffle(s1):
    s2 = list(s1)
    shuffle(s2)
    for i in range(len(s2)):
        if s2[i] != s1[i]:
            continue
        for j in range(len(s2)):
            if s2[i] != s2[j] and s2[i] != s1[j] and s2[j] != s1[i]:
                tmp = s2[i]
                s2[i] = s2[j]
                s2[j] = tmp
                break
    return s1 + " " + "".join(s2) + " (" + str(count(s1, s2)) + ")"

def shuffle(text):
    for i in range(len(text) - 1, 0, -1):
        r = random.randint(0, i)
        tmp = text[i]
        text[i] = text[r]
        text[r] = tmp

def count(s1, s2):
    count = 0
    for i in range(len(s2)):
        if s1[i] == s2[i]:
            count += 1
    return count
```