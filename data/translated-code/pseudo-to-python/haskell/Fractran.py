from typing import List
from typing import Optional
from dataclasses import dataclass

def findIndex(lst: List[int], value: int) -> Optional[int]:
    index = lst.index(value) if value in lst else None
    return index