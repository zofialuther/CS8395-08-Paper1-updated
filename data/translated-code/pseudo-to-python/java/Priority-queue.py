class Task:
    def compareTo(self, other):
        if self.priority < other.priority:
            return -1
        elif self.priority > other.priority:
            return 1
        else:
            return 0

    def main(self, args):
        pq = []
        pq.append(Task(3, "Clear drains"))
        pq.append(Task(4, "Feed cat"))
        pq.append(Task(5, "Make tea"))
        pq.append(Task(1, "Solve RC tasks"))
        pq.append(Task(2, "Tax return"))

        while len(pq) > 0:
            print(pq.pop(0))