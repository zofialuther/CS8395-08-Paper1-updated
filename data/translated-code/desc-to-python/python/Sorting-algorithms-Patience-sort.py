```python
import heapq
from bisect import bisect_left

class Pile(list):
    def __lt__(self, other):
        return self[-1] < other[-1]
    
    def __eq__(self, other):
        return self[-1] == other[-1]

def patience_sort(nums):
    piles = []
    for num in nums:
        new_pile = Pile([num])
        i = bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].append(num)
        else:
            piles.append(new_pile)
    
    for i in range(len(nums)):
        small_pile = piles[0]
        yield small_pile.pop()
        if small_pile:
            heapq.heapreplace(piles, small_pile)
        else:
            heapq.heappop(piles)

input_list = [5, 3, 8, 4, 2, 9, 1, 6, 7]
sorted_result = list(patience_sort(input_list))
print(sorted_result)
```