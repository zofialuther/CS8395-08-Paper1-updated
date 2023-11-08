class Fifo:
    def __init__(self, input, output):
        self.input = input
        self.output = output

def emptyFifo():
    return Fifo([], [])

def push(fifo, item):
    return Fifo([item] + fifo.input, fifo.output)

def pop(fifo):
    if fifo.output:
        return fifo.output[0], Fifo(fifo.input, fifo.output[1:])
    elif fifo.input:
        return pop(Fifo([], fifo.input[::-1]))
    else:
        return None, Fifo([], [])

def isEmpty(fifo):
    return fifo.input == [] and fifo.output == []