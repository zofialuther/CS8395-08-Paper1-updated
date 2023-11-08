```python
class Expr:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        if self.op in "+-*/":
            return f"({self.left} {self.op} {self.right})"
        else:
            return str(self.op)

def toDoc(expr):
    if isinstance(expr, Expr):
        return f"({toDoc(expr.left)} {expr.op} {toDoc(expr.right)})"
    else:
        return str(expr)

ops = [
    ("+", lambda x, y: x + y),
    ("-", lambda x, y: x - y),
    ("*", lambda x, y: x * y),
    ("/", lambda x, y: x / y)
]

def solve(target, nums):
    def split(nums):
        for i in range(1, len(nums)):
            yield nums[:i], nums[i:]

    def select(exprs):
        for left, right in split(exprs):
            for l in generate(left):
                for r in generate(right):
                    for op, fn in ops:
                        try:
                            exprs = Expr(op, l, r)
                            if fn(l, r) != float('inf'):
                                yield exprs
                        except ZeroDivisionError:
                            pass

    def generate(nums):
        if len(nums) == 1:
            yield nums[0]
        else:
            for expr in select(nums):
                for result in generate([e for e in nums if e != expr.left and e != expr.right] + [expr]):
                    yield result

    for expr in generate(nums):
        if expr == target:
            yield expr

def main():
    target = 24
    nums = [2, 3, 8, 9]
    for expr in solve(target, nums):
        print(toDoc(expr))

main()
```