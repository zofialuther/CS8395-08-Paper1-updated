class Fifo:
    def __init__(self):
        self.input_list = []
        self.output_list = []
    
    def emptyFifo(self):
        self.input_list = []
        self.output_list = []
    
    def push(self, item):
        self.input_list.append(item)
    
    def pop(self):
        if not self.output_list:
            while self.input_list:
                self.output_list.append(self.input_list.pop())
        return self.output_list.pop()
    
    def isEmpty(self):
        return not (self.input_list or self.output_list)