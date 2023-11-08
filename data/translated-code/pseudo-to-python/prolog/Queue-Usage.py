def empty(U, V):
    return U == V

def push(Queue, Value):
    Queue.append(Value)

def pop(Queue):
    return Queue.pop(0)

def queue():
    # create an empty queue
    Q = []
    print(f'Create queue {Q}\n')

    # add numbers 1 and 2
    print('Add numbers 1 and 2 : ', end='')
    push(Q, 1)
    push(Q, 2)

    # display queue
    print(f'{Q}\n')

    # pop element
    V = pop(Q)
    print(f'Pop : Value {V} Queue : {Q}\n')

    # test the queue
    print('Test of the queue : ', end='')
    if not Q:
        print('Queue empty')
    else:
        print('Queue not empty')
    print()

    # pop the elements
    print('Pop the queue : ', end='')
    V1 = pop(Q)
    print(f'Value {V1} Queue : {Q}\n')

    print('Pop the queue : ', end='')
    pop(Q)