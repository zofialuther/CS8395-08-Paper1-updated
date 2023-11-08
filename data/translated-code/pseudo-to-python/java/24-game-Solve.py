```python
from random import Random
from java.util import ArrayList, HashSet, Collections
from java.util import EmptyStackException, Random, Stack

class Game24Player:
    patterns = ["nnonnoo", "nnonono", "nnnoono", "nnnonoo", "nnnnooo"]
    ops = "+-*/^"
    solution = ""
    digits = []

    def main(self):
        Game24Player().play()

    def play(self):
        self.digits = self.getSolvableDigits()

        while True:
            print("Make 24 using these digits: ")
            print(self.digits)
            print("(Enter 'q' to quit, 's' for a solution)")
            line = input("> ")

            if line.lower() == "q":
                print("\nThanks for playing")
                return

            if line.lower() == "s":
                print(self.solution)
                self.digits = self.getSolvableDigits()
                continue

            entry = list(filter(lambda x: x in "+-*/()1234567890", line))

            try:
                self.validate(entry)

                if self.evaluate(self.infixToPostfix(entry)):
                    print("\nCorrect! Want to try another? ")
                    self.digits = self.getSolvableDigits()
                else:
                    print("\nNot correct.")

            except Exception as e:
                print(f"\n{e}. Try again.")

    def validate(self, input):
        total1 = 0
        parens = 0
        opsCount = 0

        for c in input:
            if c.isdigit():
                total1 += 1 << (int(c) - 1) * 4
            elif c == '(':
                parens += 1
            elif c == ')':
                parens -= 1
            elif c in self.ops:
                opsCount += 1

            if parens < 0:
                raise Exception("Parentheses mismatch.")

        if parens != 0:
            raise Exception("Parentheses mismatch.")

        if opsCount != 3:
            raise Exception("Wrong number of operators.")

        total2 = 0
        for d in self.digits:
            total2 += 1 << d * 4

        if total1 != total2:
            raise Exception("Not the same digits.")

    def evaluate(self, line):
        s = Stack()
        for c in line:
            if c.isdigit():
                s.push(float(c))
            else:
                s.push(self.applyOperator(s.pop(), s.pop(), c))

        try:
            return abs(24 - s.peek()) < 0.001
        except EmptyStackException:
            raise Exception("Invalid entry.")

    def applyOperator(self, a, b, c):
        if c == '+':
            return a + b
        elif c == '-':
            return b - a
        elif c == '*':
            return a * b
        elif c == '/':
            return b / a
        else:
            return float("NaN")

    def randomDigits(self):
        r = Random()
        result = ArrayList()
        for i in range(4):
            result.add(r.nextInt(9) + 1)
        return result

    def getSolvableDigits(self):
        result = []
        while not self.isSolvable(result):
            result = self.randomDigits()
        return result

    def isSolvable(self, digits):
        dPerms = HashSet(4 * 3 * 2)
        self.permute(digits, dPerms, 0)

        total = 4 * 4 * 4
        oPerms = ArrayList(total)
        self.permuteOperators(oPerms, 4, total)

        sb = StringBuilder(4 + 3)

        for pattern in self.patterns:
            patternChars = list(pattern)

            for dig in dPerms:
                for opr in oPerms:
                    i = 0
                    j = 0
                    for c in patternChars:
                        if c == 'n':
                            sb.append(dig.get(i))
                            i += 1
                        else:
                            sb.append(self.ops.charAt(opr.get(j)))
                            j += 1

                    candidate = sb.toString()
                    try:
                        if self.evaluate(list(candidate)):
                            self.solution = self.postfixToInfix(list(candidate))
                            return True
                    except:
                        pass
                    sb.setLength(0)

        return False

    def postfixToInfix(self, postfix):
        class Expression:
            op = ""
            ex = ""
            prec = 3

            def __init__(self, e1=None, e2=None, o=None):
                if e1 and e2 and o:
                    self.ex = f"{e1} {o} {e2}"
                    self.op = o
                    self.prec = self.ops.index(o) // 2
                else:
                    self.ex = e1

        expr = Stack()

        for c in postfix:
            idx = self.ops.find(c)
            if idx != -1:
                r = expr.pop()
                l = expr.pop()
                opPrec = idx // 2

                if l.prec < opPrec:
                    l.ex = '(' + l.ex + ')'

                if r.prec <= opPrec:
                    r.ex = '(' + r.ex + ')'

                expr.push(Expression(l.ex, r.ex, c))
            else:
                expr.push(Expression(c))

        return expr.peek().ex

    def infixToPostfix(self, infix):
        sb = StringBuilder()
        s = Stack()
        for c in infix:
            idx = self.ops.find(c)
            if idx != -1:
                if s.isEmpty():
                    s.push(idx)
                else:
                    while not s.isEmpty():
                        prec2 = s.peek() // 2
                        prec1 = idx // 2
                        if prec2 >= prec1:
                            sb.append(self.ops[s.pop()])
                        else:
                            break
                    s.push(idx)
            elif c == '(':
                s.push(-2)
            elif c == ')':
                while s.peek() != -2:
                    sb.append(self.ops[s.pop()])
                s.pop()
            else:
                sb.append(c)

        while not s.isEmpty():
            sb.append(self.ops[s.pop()])

        return list(sb.toString())

    def permute(self, lst, res, k):
        for i in range(k, lst.size()):
            Collections.swap(lst, i, k)
            self.permute(lst, res, k + 1)
            Collections.swap(lst, k, i)
        if k == lst.size():
            res.add(ArrayList(lst))

    def permuteOperators(self, res, n, total):
        for i in range(total):
            res.add(Arrays.asList((i // (n * n)), ((i % (n * n)) // n), (i % n))


Game24Player().main()
```