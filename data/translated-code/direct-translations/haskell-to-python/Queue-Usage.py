```python
# fifo.py
class Fifo:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return None

q = Fifo()
print(q.isEmpty())  # True
q.push(1)
print(q.isEmpty())  # False
for i in range(2, 5):
    q.push(i)
print(q.pop())  # 1
print(q.pop())  # 2
print(q.pop())  # 3
print(q.pop())  # 4
print(q.pop())  # None
```
To run the code, save it in a file named "fifo.py" and run the command `python fifo.py` in your terminal.