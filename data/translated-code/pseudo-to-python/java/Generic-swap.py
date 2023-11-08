class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    @staticmethod
    def swap(p):
        temp = p.first
        p.first = p.second
        p.second = temp