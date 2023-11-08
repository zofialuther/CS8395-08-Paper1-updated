```python
import queue

class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
        return

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"Task: {self.name}, Priority: {self.priority}"

tasks = queue.PriorityQueue()

tasks.put(Task(5, 'Task1'))
tasks.put(Task(1, 'Task2'))
tasks.put(Task(3, 'Task3'))

while not tasks.empty():
    print(tasks.get())
```