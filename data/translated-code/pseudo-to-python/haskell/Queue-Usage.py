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

    def foldl(self, func, lst):
        return reduce(func, lst)

q = Fifo()
if q.isEmpty():
    print(True)
else:
    q.push(1)
    if not q.isEmpty():
        print(False)
    q.foldl(q.push, [2, 3, 4])
    v = q.pop()
    if v == 1:
        print(v)
    v = q.pop()
    if v == 2:
        print(v)
    v = q.pop()
    if v == 3:
        print(v)
    v = q.pop()
    if v == 4:
        print(v)
    v = q.pop()
    if v == None:
        print(None)