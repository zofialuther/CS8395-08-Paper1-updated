class Queue:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def empty_queue(self):
        return Queue([], [])

    def push(self, element):
        new_back = self.back + [element]
        return Queue(self.front, new_back)

    def pop(self):
        if self.front:
            return self.front[0], Queue(self.front[1:], self.back)
        elif self.back:
            return self.back[0], Queue(self.back[1:], [])
        else:
            return None

# Demonstration
q = Queue([], [])
q = q.push(1)
q = q.push(2)
element, q = q.pop()
print(element)  # should print 1
print(q.empty_queue())  # should print False
element, q = q.pop()
print(element)  # should print 2
print(q.empty_queue())  # should print True