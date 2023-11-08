from queue import Queue

my_queue = Queue()
my_queue.put("foo")
my_queue.put("bar")
my_queue.put("baz")

print(my_queue.get())
print(my_queue.get())
print(my_queue.get())