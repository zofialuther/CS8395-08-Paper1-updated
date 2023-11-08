import queue

# Create a new priority queue
pq = queue.PriorityQueue()

# Put an item into the queue
pq.put((1, 'data1'))

# Remove and return an item from the queue
item = pq.get()

# Check if the queue is empty
is_empty = pq.empty()

# Check if the queue is full
is_full = pq.full()

# Get the size of the queue
size = pq.qsize()

# Indicate that a formerly enqueued task is complete
pq.task_done()