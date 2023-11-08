```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self):
        if self.head is None:
            return None
        else:
            removed = self.head.data
            self.head = self.head.next
            return removed

    def print_contents(self):
        current = self.head
        contents = []
        while current:
            contents.append(current.data)
            current = current.next
        print(contents)

queue = LinkedList()
print(queue.is_empty())
queue.add(1)
queue.add(2)
queue.add(3)
queue.print_contents()
print(queue.remove())
queue.print_contents()
print(queue.is_empty())
```