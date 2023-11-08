# Create a new LinkedList
queue = []

# Check if the queue is empty and print the result
print(len(queue) == 0)  # True

# Add new integers to the queue
queue.append(1)
queue.append(2)
queue.append(3)

# Print the contents of the queue
print(queue)  # [1, 2, 3]

# Remove the first element from the queue and print it
print(queue.pop(0))  # 1

# Print the contents of the queue after removal
print(queue)  # [2, 3]

# Check if the queue is empty and print the result
print(len(queue) == 0)  # False