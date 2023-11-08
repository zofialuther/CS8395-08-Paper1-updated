from queue import PriorityQueue

TL0 = [(3, 'Clear drains'),
       (4, 'Feed cat')]

# create a priority queue from a list
pq = PriorityQueue()
for item in TL0:
    pq.put(item)

# now we add the other elements
pq.put((5, 'Make tea'))
pq.put((1, 'Solve RC tasks'))
pq.put((2, 'Tax return'))

# list the content of the queue
print("Content of the queue:")
while not pq.empty():
    print(pq.get())

# retrieve the minimum-priority pair
priority, key = pq.get()
print(f"Retrieve top of the queue: Priority {priority}, Element {key}")

# list the content of the queue
print("Content of the queue:")
while not pq.empty():
    print(pq.get())