```python
import queue

class Hamming:
    def hammingNumber(self, n):
        pq = queue.PriorityQueue()
        pq.put(1)
        count = 0
        prev = 0
        while count < n:
            curr = pq.get()
            if curr != prev:
                count += 1
                prev = curr
                pq.put(curr*2)
                pq.put(curr*3)
                pq.put(curr*5)
        return prev

if __name__ == "__main__":
    h = Hamming()
    for i in range(1, 20):
        print(h.hammingNumber(i))
```