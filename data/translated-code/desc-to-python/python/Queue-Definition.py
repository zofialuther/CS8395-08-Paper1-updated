class FIFO:
    def __init__(self):
        self.contents = []

    def is_empty(self):
        return len(self.contents) == 0

    def pop(self):
        if not self.is_empty():
            return self.contents.pop(0)
        else:
            return None

    def retrieve_attribute(self, index):
        if index < len(self.contents):
            return self.contents[index]
        else:
            return None

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.contents):
            result = self.contents[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration