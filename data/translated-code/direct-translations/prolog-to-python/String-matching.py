```python
from typing import List

def starts_with(FIRSTz: List[int], SECONDz: List[int]) -> bool:
    return SECONDz == FIRSTz[:len(SECONDz)]

def contains(FIRSTz: List[int], SECONDz: List[int]) -> bool:
    return any(starts_with(FIRSTz[i:], SECONDz) for i in range(len(FIRSTz)))

def ends_with(FIRSTz: List[int], SECONDz: List[int]) -> bool:
    return SECONDz == FIRSTz[-len(SECONDz):]
```