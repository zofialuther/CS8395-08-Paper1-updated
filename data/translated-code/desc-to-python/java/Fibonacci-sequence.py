class FibUtil:
    def fibStream(self):
        return LongStream.iterate((0, 1), lambda t: (t[1], t[0] + t[1])).map(lambda t: t[0])

    def fib(self, n):
        return self.fibStream().limit(n).reduce(lambda x, y: y)