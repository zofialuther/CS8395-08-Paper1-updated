# Python code
# Priority queue in Python using heapq

import heapq

class PriorityQueue:
    def __init__(self):
        self.tasks = []
        self.counter = 0

    def add_task(self, priority, task):
        heapq.heappush(self.tasks, (-priority, self.counter, task))
        self.counter += 1

    def get_highest_priority_task(self):
        return heapq.heappop(self.tasks)

    def display_queue_content(self):
        print("Priority Queue Content:")
        for task in self.tasks:
            print(task[2])

# Create a priority queue
priority_queue = PriorityQueue()

# Add tasks to the queue
priority_queue.add_task(3, "Task 1")
priority_queue.add_task(1, "Task 2")
priority_queue.add_task(2, "Task 3")

# Display the content of the queue
priority_queue.display_queue_content()

# Retrieve the task with the highest priority
highest_priority_task = priority_queue.get_highest_priority_task()
print("Task with highest priority:", highest_priority_task[2])

# Show the updated content of the queue
priority_queue.display_queue_content()