from typing import List

def exchange(lst: List[int], I: int, J: int) -> List[int]:
    temp = lst[I]
    lst[I] = lst[J]
    lst[J] = temp
    return lst

def selection_sort(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst = exchange(lst, i, min_idx)
    return lst