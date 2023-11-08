from collections import deque

# Create an empty FIFO queue
fifo_queue = deque()

# Check if the queue is empty
print(fifo_queue)  # Output: True

# Push values 1, 2, 3, and 4 into the queue
fifo_queue.append(1)
fifo_queue.append(2)
fifo_queue.append(3)
fifo_queue.append(4)

# Check if the queue is empty
print(fifo_queue)  # Output: False

# Pop values from the queue
print(fifo_queue.popleft())  # Output: 1
print(fifo_queue.popleft())  # Output: 2
print(fifo_queue.popleft())  # Output: 3
print(fifo_queue.popleft())  # Output: 4

# Attempt to pop from the now empty queue
print(fifo_queue.popleft())  # Output: IndexError: deque is empty