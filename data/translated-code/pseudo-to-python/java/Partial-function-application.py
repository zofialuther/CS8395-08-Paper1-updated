def fs(f, s):
    r = [0] * len(s)
    for i in range(len(s)):
        r[i] = f(s[i])
    return r

class IntegerFunction:
    def call(self, arg):
        pass

class SequenceFunction:
    def call(self, arg):
        pass

def fs(f):
    class NewSequenceFunction(SequenceFunction):
        def call(self, s):
            return fs(f, s)
    return NewSequenceFunction()

class PartialApplication:
    @staticmethod
    def f1(i):
        return i * 2

    @staticmethod
    def f2(i):
        return i ** 2

fsf1 = fs(PartialApplication.f1)
fsf2 = fs(PartialApplication.f2)

def main(args):
    sequences = [[0, 1, 2, 3], [2, 4, 6, 8]]
    for array in sequences:
        print(array, fsf1.call(array), fsf2.call(array))