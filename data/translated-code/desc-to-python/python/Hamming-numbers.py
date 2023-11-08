```python
import heapq
from itertools import tee

def hamming_numbers():
    def gen_hamming_numbers():
        h = [1]
        for i in h:
            yield i
            h.append(2*i)
            h.append(3*i)
            h.append(5*i)
        h = h[1:]
    
    a, b, c = tee(gen_hamming_numbers(), 3)
    
    for i in heapq.merge(a, b, c):
        yield i
```