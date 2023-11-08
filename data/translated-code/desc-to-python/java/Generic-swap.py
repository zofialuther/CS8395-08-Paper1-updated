class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def swap(pair):
    pair.first, pair.second = pair.second, pair.first