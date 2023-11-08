from typing import List
import heapq

def patience_sort(nums: List[int]) -> List[int]:
    piles = []
    for num in nums:
        new_pile = [num]
        i = bisect.bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].append(num)
        else:
            piles.append(new_pile)
    for i in range(len(nums)):
        smallest_pile = min(piles, key=lambda x: x[-1])
        nums[i] = smallest_pile.pop()
        if not smallest_pile:
            piles.remove(smallest_pile)
    return nums

print(patience_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))