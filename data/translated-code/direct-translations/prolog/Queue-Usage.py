```python
def empty(U, V):
    return U == V

def push(Queue, Value):
    return Queue + [Value]

def pop(Queue):
    return Queue[0], Queue[1:]

def queue():
    # create an empty queue
    Q = []
    print('Create queue', Q)

    # add numbers 1 and 2
    print('Add numbers 1 and 2 : ', end='')
    Q = push(Q, 1)
    Q = push(Q, 2)

    # display queue
    print(Q)

    # pop element
    V, Q = pop(Q)
    print('Pop : Value', V, 'Queue :', Q)

    # test the queue
    print('Test of the queue : ', end='')
    if not Q:
        print('Queue empty')
    else:
        print('Queue not empty')

    # pop the elements
    print('Pop the queue : ', end='')
    V1, Q = pop(Q)
    print('Value', V1, 'Queue :', Q)

    print('Pop the queue : ', end='')
    _V, _Q = pop(Q)

queue()
```