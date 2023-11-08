from queue import Queue

# create a queue
q = Queue()

# add elements to the queue
q.put("foo")
q.put("bar")
q.put("baz")

# retrieve and print elements from the queue
print(q.get())
print(q.get())
print(q.get())