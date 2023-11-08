```python
from dataclasses import dataclass
from typing import Optional, List, Tuple

@dataclass
class PriorityQ:
    k: Optional[int]
    v: Optional[int]
    left: Optional['PriorityQ']
    right: Optional['PriorityQ']

emptyPQ = PriorityQ(None, None, None, None)

def isEmptyPQ(pq: PriorityQ) -> bool:
    return pq.k is None

def sizePQ(pq: PriorityQ) -> int:
    if pq.k is None:
        return 0
    else:
        n = sizePQ(pq.right)
        return 2 * n + rest(n, pq.left, pq.right)

def rest(n: int, p: PriorityQ, q: PriorityQ) -> int:
    if n == 0 and q.k is None:
        return 1
    elif n == 0:
        return 2
    else:
        d = (n - 1) >> 1
        r = (n - 1) & 1
        if r == 0:
            return rest(d, p.left, q.left)
        else:
            return rest(d, p.right, q.right)

def peekMinPQ(pq: PriorityQ) -> Optional[Tuple[int, int]]:
    if pq.k is None:
        return None
    else:
        return (pq.k, pq.v)

def pushPQ(wk: int, wv: int, pq: PriorityQ) -> PriorityQ:
    if pq.k is None:
        return PriorityQ(wk, wv, emptyPQ, emptyPQ)
    elif wk <= pq.k:
        return PriorityQ(wk, wv, pushPQ(pq.k, pq.v, pq.right), pq.left)
    else:
        return PriorityQ(pq.k, pq.v, pushPQ(wk, wv, pq.right), pq.left)

def siftdown(wk: int, wv: int, pl: PriorityQ, pr: PriorityQ) -> PriorityQ:
    if pl.k is None:
        return PriorityQ(wk, wv, emptyPQ, emptyPQ)
    elif pr.k is None:
        if wk <= pl.k:
            return PriorityQ(wk, wv, pl, emptyPQ)
        else:
            return PriorityQ(pl.k, pl.v, PriorityQ(wk, wv, emptyPQ, emptyPQ), emptyPQ)
    else:
        if wk <= pl.k and wk <= pr.k:
            return PriorityQ(wk, wv, pl, pr)
        elif pl.k <= pr.k:
            return PriorityQ(pl.k, pl.v, siftdown(wk, wv, pl.left, pl.right), pr)
        else:
            return PriorityQ(pr.k, pr.v, pl, siftdown(wk, wv, pr.left, pr.right))

def replaceMinPQ(wk: int, wv: int, pq: PriorityQ) -> PriorityQ:
    if pq.k is None:
        return emptyPQ
    else:
        return siftdown(wk, wv, pq.left, pq.right)

def deleteMinPQ(pq: PriorityQ) -> PriorityQ:
    if pq.k is None:
        return emptyPQ
    elif pq.right.k is None:
        return pq.left
    else:
        k, v, npl = leftrem(pq.left)
        return siftdown(k, v, pq.right, npl)

def leftrem(pq: PriorityQ) -> Tuple[int, int, PriorityQ]:
    if pq.right.k is None:
        return (pq.k, pq.v, emptyPQ)
    else:
        k, v, npl = leftrem(pq.left)
        return (k, v, PriorityQ(pq.k, pq.v, pq.right, npl))

def adjustPQ(f: callable, pq: PriorityQ) -> PriorityQ:
    if pq.k is None:
        return emptyPQ
    else:
        k, v = f(pq.k, pq.v)
        return siftdown(k, v, adjustPQ(f, pq.left), adjustPQ(f, pq.right))

def fromListPQ(lst: List[Tuple[int, int]]) -> PriorityQ:
    if not lst:
        return emptyPQ
    else:
        pq, _ = build(len(lst), lst)
        return pq

def build(lvl: int, xs: List[Tuple[int, int]]) -> Tuple[PriorityQ, List[Tuple[int, int]]]:
    if lvl == 0:
        return emptyPQ, xs
    else:
        pl, xrl = build(lvl >> 1, xs)
        pr, xrr = build((lvl - 1) >> 1, xrl)
        return siftdown(xs[0][0], xs[0][1], pl, pr), xrr

def mergePQ(pq1: PriorityQ, pq2: PriorityQ) -> PriorityQ:
    if pq1.k is None:
        return pq2
    elif pq2.k is None:
        return pq1
    else:
        return fromListPQ(zipper(pq1, []) + zipper(pq2, []))

def zipper(pq: PriorityQ, appndlst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if pq.k is not None and pq.left.k is None:
        return [(pq.k, pq.v)] + appndlst
    elif pq.k is not None and pq.right.k is None:
        return [(pq.k, pq.v)] + zipper(pq.left, appndlst)
    else:
        return [(pq.k, pq.v)] + zipper(pq.left, zipper(pq.right, appndlst))

def popMinPQ(pq: PriorityQ) -> Optional[Tuple[Tuple[int, int], PriorityQ]]:
    kv = peekMinPQ(pq)
    if kv is None:
        return None
    else:
        return (kv, deleteMinPQ(pq))

def toListPQ(pq: PriorityQ) -> List[Tuple[int, int]]:
    if pq.k is None:
        return []
    else:
        return [(pq.k, pq.v)] + toListPQ(deleteMinPQ(pq))

def sortPQ(ls: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return toListPQ(fromListPQ(ls))
```