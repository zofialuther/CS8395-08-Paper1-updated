from typing import List
from functools import cmp_to_key

def sorted(xs: List[int]) -> List[int]:
    def pad(x: str) -> str:
        return ''.join([x] * ((maxLen // len(x)) + 1))
    
    maxLen = max(map(len, map(str, xs)))
    return sorted(xs, key=cmp_to_key(lambda a, b: 1 if pad(a) < pad(b) else -1))

def maxcat(arrays: List[List[int]]) -> List[int]:
    return [int(''.join(map(str, sorted(array)))) for array in arrays]

print(maxcat([[1,34,3,98,9,76,45,4], [54,546,548,60]]))