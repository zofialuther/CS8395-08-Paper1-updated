from typing import List
from dataclasses import dataclass

def selSort(xs: List[int]) -> List[int]:
    if not xs:
        return []
    else:
        x = max(xs)
        xs.remove(x)
        return selSort(xs) + [x]