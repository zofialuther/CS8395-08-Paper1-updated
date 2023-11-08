class Fifo:
    def __init__(self, input_list, output_list):
        self.input = input_list
        self.output = output_list

    @staticmethod
    def emptyFifo():
        return Fifo([], [])

    def push(self, item):
        self.input.append(item)

    def pop(self):
        if len(self.output) == 0 and len(self.input) > 0:
            self.output = self.input[::-1]
            self.input = []
        if len(self.output) > 0:
            return self.output.pop(0)
        else:
            return None

    def isEmpty(self):
        return len(self.input) == 0 and len(self.output) == 0
