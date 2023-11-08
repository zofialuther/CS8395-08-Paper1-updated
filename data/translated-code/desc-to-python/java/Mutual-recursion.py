class MutualRecursion:
    femaleResults = {}
    maleResults = {}

    def f(self, n):
        if n in self.femaleResults:
            return self.femaleResults[n]
        if n == 0:
            result = 1
        else:
            result = n - self.m(self.f(n - 1))
        self.femaleResults[n] = result
        return result

    def m(self, n):
        if n in self.maleResults:
            return self.maleResults[n]
        if n == 0:
            result = 0
        else:
            result = n - self.f(self.m(n - 1))
        self.maleResults[n] = result
        return result

    def main(self):
        for i in range(1, 21):
            print(f"Female({i}): {self.f(i)}, Male({i}): {self.m(i)}")

recursion = MutualRecursion()
recursion.main()