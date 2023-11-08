class BalancedTernary:
    def __init__(self, a):
        self.a = a

    def zeroTrim(self, a):
        if len(a) == 0:
            return [0]
        else:
            s = []
            for num in a:
                if num == 0:
                    s.append(num)
                else:
                    s += [num]
            return s

    def btList(self):
        return self.a

    def __eq__(self, other):
        return self.btList() == other.btList()

    def btNormalize(self):
        def _carry(c, a):
            if len(a) == 0:
                if c == 0:
                    return []
                else:
                    return [c]
            else:
                cc, r = f((a[0]+c) // 3, (a[0]+c) % 3)
                return [r] + _carry(cc, a[1:])

        def f(x, y):
            if y == 2:
                return (x + 1, -1)
            elif y == -2:
                return (x - 1, 1)
            else:
                return (x, y)

        return BalancedTernary(_carry(0, self.a))

    def listBt(self):
        return BalancedTernary(self.zeroTrim(self.a))

    def __str__(self):
        return ''.join(list(map(lambda d: '-' if d == -1 else '0' if d == 0 else '+', self.a)))

    def strBt(self, s):
        return BalancedTernary(self.zeroTrim(list(map(lambda c: -1 if c == '-' else 0 if c == '0' else 1, s[::-1]))))

    def intBt(self, a):
        return BalancedTernary(list(map(int, str(a))))

    def btInt(self):
        return sum([self.a[i] * (3 ** i) for i in range(len(self.a))])

    def listAdd(self, a, b):
        return [a[i] + b[i] for i in range(max(len(a), len(b)))]

    def __neg__(self):
        return BalancedTernary(list(map(lambda x: -x, self.a)))

    def __add__(self, other):
        return self.btNormalize(self.listAdd(self.a, other.a))

    def __mul__(self, other):
        def mul_(as, b):
            if len(b) == 0:
                return []
            else:
                return self.listAdd(list(map(lambda a: a * b[0], as)) + [0], mul_(as, b[1:]))

        return self.btNormalize(mul_(self.a, other.a))

    def __sub__(self, other):
        return self.btNormalize(self.listAdd(self.a, list(map(lambda x: -x, other.a))))

    def __abs__(self):
        if self.a == [0]:
            return BalancedTernary([0])
        elif self.a[-1] == -1:
            return -self
        else:
            return self

    def __fromInteger__(self, x):
        def f(x):
            if x == 0:
                return []
            else:
                return [x % 3] + f(x // 3)

        return self.btNormalize(f(x))


a = BalancedTernary([1, 0, -1, 1, 1, 0, 1])
b = BalancedTernary([-1, 1, 0, 0, 1, 1])
c = BalancedTernary([1, -1, 1, 0, 1, -1])
r = a * (b - c)
print([a.btInt(), b.btInt(), c.btInt()])
print(r)
print(r.btInt())