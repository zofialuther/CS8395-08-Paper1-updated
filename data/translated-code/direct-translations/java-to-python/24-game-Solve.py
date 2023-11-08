```python
import random

class Game24Player:
    def __init__(self):
        self.patterns = ["nnonnoo", "nnonono", "nnnoono", "nnnonoo", "nnnnooo"]
        self.ops = "+-*/^"
        self.solution = ""
        self.digits = []

    def main(self):
        self.play()

    def play(self):
        self.digits = self.get_solvable_digits()

        while True:
            print("Make 24 using these digits:", self.digits)
            print("(Enter 'q' to quit, 's' for a solution)")
            line = input("> ")

            if line.lower() == "q":
                print("\nThanks for playing")
                return

            if line.lower() == "s":
                print(self.solution)
                self.digits = self.get_solvable_digits()
                continue

            entry = [char for char in line if char in "*/-+()1234567890"]

            try:
                self.validate(entry)

                if self.evaluate(self.infix_to_postfix(entry)):
                    print("\nCorrect! Want to try another?")
                    self.digits = self.get_solvable_digits()
                else:
                    print("\nNot correct.")

            except Exception as e:
                print("\n{} Try again.".format(e))

    def validate(self, input):
        total1 = 0
        parens = 0
        ops_count = 0

        for c in input:
            if c.isdigit():
                total1 += 1 << (int(c) * 4)
            elif c == '(':
                parens += 1
            elif c == ')':
                parens -= 1
            elif c in self.ops:
                ops_count += 1
            if parens < 0:
                raise Exception("Parentheses mismatch.")

        if parens != 0:
            raise Exception("Parentheses mismatch.")

        if ops_count != 3:
            raise Exception("Wrong number of operators.")

        total2 = sum(1 << d * 4 for d in self.digits)

        if total1 != total2:
            raise Exception("Not the same digits.")

    def evaluate(self, line):
        s = []
        try:
            for c in line:
                if c.isdigit():
                    s.append(float(c))
                else:
                    s.append(self.apply_operator(s.pop(), s.pop(), c))
        except IndexError:
            raise Exception("Invalid entry.")
        return abs(24 - s[-1]) < 0.001

    def apply_operator(self, a, b, c):
        if c == '+':
            return a + b
        elif c == '-':
            return b - a
        elif c == '*':
            return a * b
        elif c == '/':
            return b / a
        else:
            return float("nan")

    def random_digits(self):
        return [random.randint(1, 9) for _ in range(4)]

    def get_solvable_digits(self):
        result = self.random_digits()
        while not self.is_solvable(result):
            result = self.random_digits()
        return result

    def is_solvable(self, digits):
        d_perms = set()
        self.permute(digits, d_perms, 0)

        total = 4 * 4 * 4
        o_perms = []
        self.permute_operators(o_perms, 4, total)

        sb = ""

        for pattern in self.patterns:
            pattern_chars = list(pattern)

            for dig in d_perms:
                for opr in o_perms:
                    i, j = 0, 0
                    for c in pattern_chars:
                        if c == 'n':
                            sb += str(dig[i])
                            i += 1
                        else:
                            sb += self.ops[opr[j]]
                            j += 1

                    candidate = sb
                    try:
                        if self.evaluate(candidate):
                            self.solution = self.postfix_to_infix(candidate)
                            return True
                    except Exception:
                        pass
                    sb = ""
        return False

    def postfix_to_infix(self, postfix):
        class Expression:
            def __init__(self, e1, e2, o):
                self.ex = "{} {} {}".format(e1, o, e2)
                self.op = o
                self.prec = self.ops.index(o) // 2

        expr = []

        for c in postfix:
            idx = self.ops.find(c)
            if idx != -1:
                r = expr.pop()
                l = expr.pop()
                op_prec = idx // 2

                if l.prec < op_prec:
                    l.ex = "({})".format(l.ex)

                if r.prec <= op_prec:
                    r.ex = "({})".format(r.ex)

                expr.append(Expression(l.ex, r.ex, c))
            else:
                expr.append(Expression(c, None, None))
        return expr[-1].ex

    def infix_to_postfix(self, infix):
        sb = []
        s = []

        for c in infix:
            idx = self.ops.find(c)
            if idx != -1:
                if not s:
                    s.append(idx)
                else:
                    while s:
                        prec2 = s[-1] // 2
                        prec1 = idx // 2
                        if prec2 >= prec1:
                            sb.append(self.ops[s.pop()])
                        else:
                            break
                    s.append(idx)
            elif c == '(':
                s.append(-2)
            elif c == ')':
                while s[-1] != -2:
                    sb.append(self.ops[s.pop()])
                s.pop()
            else:
                sb.append(c)

        while s:
            sb.append(self.ops[s.pop()])

        return "".join(sb)

    def permute(self, lst, res, k):
        for i in range(k, len(lst)):
            lst[k], lst[i] = lst[i], lst[k]
            self.permute(lst, res, k + 1)
            lst[k], lst[i] = lst[i], lst[k]
        if k == len(lst):
            res.add(tuple(lst))

    def permute_operators(self, res, n, total):
        npow = n * n
        for i in range(total):
            res.append([i // npow, (i % npow) // n, i % n])


game = Game24Player()
game.main()
```