class Exp:
    def pow(self, base, exponent):
        if exponent < 0:
            return 1 / self.pow(base, -exponent)
        ans = 1
        for _ in range(exponent):
            ans *= base
        return ans

    def main(self):
        exp = Exp()
        print(exp.pow(2, 3))  # Output: 8
        print(exp.pow(3, 4))  # Output: 81
        print(exp.pow(5, -2))  # Output: 0.04