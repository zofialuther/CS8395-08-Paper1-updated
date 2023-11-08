```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise Exception("Queue is empty")
        else:
            value = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return value

    def is_empty(self):
        return self.front is None
```