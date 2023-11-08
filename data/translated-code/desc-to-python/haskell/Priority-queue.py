class PriorityQ:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek_min(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def push(self, value):
        self.queue.append(value)
        self.adjust_up(len(self.queue) - 1)

    def replace_min(self, value):
        if self.is_empty():
            return
        self.queue[0] = value
        self.adjust_down(0)

    def delete_min(self):
        if self.is_empty():
            return
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self.adjust_down(0)

    def adjust_all(self):
        n = len(self.queue)
        for i in range(n//2 - 1, -1, -1):
            self.adjust_down(i)

    @classmethod
    def from_list(cls, lst):
        pq = cls()
        pq.queue = lst
        pq.adjust_all()
        return pq

    def merge(self, other):
        self.queue.extend(other.queue)
        self.adjust_all()

    def pop_min(self):
        min_val = self.peek_min()
        self.delete_min()
        return min_val

    def to_sorted_list(self):
        sorted_lst = []
        while not self.is_empty():
            sorted_lst.append(self.pop_min())
        return sorted_lst