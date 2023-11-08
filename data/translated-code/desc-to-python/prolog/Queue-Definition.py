```python
class Queue:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def empty(self):
        return self.front == None

    def push(self, value):
        new_back = [value, None]
        if self.front == None:
            self.front = new_back
        else:
            self.back[1] = new_back
        self.back = new_back

    def pop(self):
        if self.front == None:
            return None
        else:
            popped = self.front[0]
            self.front = self.front[1]
            return popped

    def append_dl(self, other_queue):
        if self.front == None:
            self.front = other_queue.front
            self.back = other_queue.back
        else:
            self.back[1] = other_queue.front
            self.back = other_queue.back
```