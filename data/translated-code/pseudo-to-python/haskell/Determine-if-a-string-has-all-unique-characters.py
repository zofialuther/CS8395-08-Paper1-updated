```python
from typing import List, Tuple, Optional
import string
import operator as op
import Data.Map as M
import Safe as S
import Data.Ord

duplicatedCharIndices :: str -> Optional[Tuple[str, List[int]]]
def duplicatedCharIndices(xs: str) -> Optional[Tuple[str, List[int]]]:
    def go(k: str, xs: List[int], mb: Optional[Tuple[str, List[int]]]) -> Optional[Tuple[str, List[int]]]:
        if len(xs) == 1:
            return mb
        elif mb is None:
            return (k, xs)
        else:
            c, ys = mb
            if xs[0] < ys[0]:
                return (k, xs)
            else:
                return (c, ys)

    char_indices = M.foldrWithKey(go, None, foldl(lambda a, ic: M.insert(ic[1], a.get(ic[1], []) + [ic[0]], a), M.empty(), zip(range(len(xs)), xs)))
    
    if char_indices is None:
        return None
    else:
        return char_indices[0], char_indices[1]

def fTable(s: str, xShow: Callable[[a], str], fxShow: Callable[[b], str], f: Callable[[a], b], xs: List[a]) -> str:
    def rjust(n: int, c: str) -> str:
        return lambda s: s.rjust(n, c)
    
    w = max([len(xShow(x)) for x in xs])
    return '\n'.join([s] + [rjust(w, ' ')(xShow(x)) + ' -> ' + fxShow(f(x)) for x in xs])
```