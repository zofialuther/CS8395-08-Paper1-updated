from queue import PriorityQueue

class Task:
    def __init__(self, p, n):
        self.priority = p
        self.name = n

    def __str__(self):
        return str(self.priority) + ", " + self.name

    def __lt__(self, other):
        return self.priority < other.priority

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.put(Task(3, "Clear drains"))
    pq.put(Task(4, "Feed cat"))
    pq.put(Task(5, "Make tea"))
    pq.put(Task(1, "Solve RC tasks"))
    pq.put(Task(2, "Tax return"))

    while not pq.empty():
        print(pq.get())