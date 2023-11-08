import heapq

def list_to_heap(lst, heap):
    for item in lst:
        heapq.heappush(heap, item)

def add_to_heap(heap, priority, element, new_heap):
    heapq.heappush(heap, (priority, element))
    new_heap = heap

def heap_to_list(heap, lst):
    lst = [item[1] for item in heap]

def get_from_heap(heap, priority, key, new_heap):
    (priority, key) = heapq.heappop(heap)
    new_heap = heap

TL0 = [(3, 'Clear drains'), (4, 'Feed cat')]
Heap0 = []
list_to_heap(TL0, Heap0)

Heap1 = []
add_to_heap(Heap0, 5, 'Make tea', Heap1)

Heap2 = []
add_to_heap(Heap1, 1, 'Solve RC tasks', Heap2)

Heap3 = []
add_to_heap(Heap2, 2, 'Tax return', Heap3)

TL1 = []
heap_to_list(Heap3, TL1)
print('Content of the queue')
for item in TL1:
    print(item)

Priority = 0
Key = ''
Heap4 = []
get_from_heap(Heap3, Priority, Key, Heap4)
print('Retrieve top of the queue : Priority', Priority, 'Element', Key)

TL2 = []
heap_to_list(Heap4, TL2)
print('Content of the queue')
for item in TL2:
    print(item)