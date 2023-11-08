class PriorityQ:
  def __init__(self, k, v):
    self.k = k
    self.v = v
    self.left = None
    self.right = None

def emptyPQ():
  return PriorityQ(None, None)

def isEmptyPQ(pq):
  return pq.k is None and pq.v is None

def sizePQ(pq):
  if pq.k is None and pq.v is None:
    return 0
  else:
    n = sizePQ(pq.right)
    return 2 * n + rest(n, pq.left, pq.right)

def rest(n, p, q):
  if n == 0 and p.k is None:
    return 1
  elif n == 0:
    return 2
  elif p.left is not None:
    return rest(n - 1, p.left, q.left)
  else:
    return rest(n - 1, p.right, q.right)

def peekMinPQ(pq):
  if pq.k is None and pq.v is None:
    return None
  else:
    return [pq.k, pq.v]

def pushPQ(wk, wv, pq):
  if pq.k is None and pq.v is None:
    pq.k = wk
    pq.v = wv
  elif wk <= pq.k:
    tempK = pq.k
    tempV = pq.v
    pq.k = wk
    pq.v = wv
    pushPQ(tempK, tempV, pq.right)
  else:
    pushPQ(wk, wv, pq.right)
  return pq

def replaceMinPQ(wk, wv, pq):
  if pq.k is None and pq.v is None:
    return emptyPQ()
  else:
    return siftdown(wk, wv, pq.left, pq.right)

def deleteMinPQ(pq):
  if pq.k is None and pq.v is None:
    return emptyPQ()
  elif pq.left is None:
    return pq.right
  else:
    tempK = pq.k
    tempV = pq.v
    npl = leftrem(pq.left)
    return siftdown(tempK, tempV, pq.right, npl)

def adjustPQ(f, pq):
  if pq.k is None and pq.v is None:
    return emptyPQ()
  else:
    return adjust(pq)

def fromListPQ(list):
  if len(list) == 0:
    return emptyPQ()
  else:
    pq = build(len(list), list)
    return pq

def mergePQ(pq1, pq2):
  if pq1.k is None and pq1.v is None:
    return pq2
  elif pq2.k is None and pq2.v is None:
    return pq1
  else:
    return fromListPQ(zipper(pq1, pq2, []))

def popMinPQ(pq):
  kv = peekMinPQ(pq)
  if kv is None:
    return None
  else:
    return [kv, deleteMinPQ(pq)]

def toListPQ(pq):
  if pq.k is None and pq.v is None:
    return []
  else:
    return [[pq.k, pq.v], *toListPQ(deleteMinPQ(pq))]

def sortPQ(list):
  pq = fromListPQ(list)
  return toListPQ(pq)