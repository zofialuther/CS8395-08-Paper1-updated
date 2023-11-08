from collections import deque

queue = deque()
print(queue)  # empty test - true
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # [1, 2, 3]
print(queue.popleft())  # 1
print(queue)  # [2, 3]
print(queue)  # false