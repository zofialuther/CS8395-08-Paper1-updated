```python
from queue import PriorityQueue

def sort(n):
    piles = []
    for x in n:
        newPile = [x]
        i = 0
        for pile in piles:
            if newPile[0] < pile[0]:
                break
            i += 1
        if i < len(piles):
            piles[i].append(x)
        else:
            piles.append(newPile)
    
    heap = PriorityQueue()
    for c in range(len(n)):
        smallPile = heap.get()
        n[c] = smallPile.pop()
        if smallPile:
            heap.put(smallPile)

def main(args):
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    sort(a)
    print(a)
```