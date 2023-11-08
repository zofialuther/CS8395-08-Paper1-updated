class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    class Node:
        def __init__(self, value, next_node):
            self.value = value
            self.next = next_node

    def enqueue(self, value):
        new_node = self.Node(value, None)
        if self.empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.empty():
            raise ValueError("No more elements.")
        ret_val = self.head.value
        self.head = self.head.next
        return ret_val

    def empty(self):
        return self.head is None