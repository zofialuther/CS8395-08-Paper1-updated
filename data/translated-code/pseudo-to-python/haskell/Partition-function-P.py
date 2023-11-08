```python
class Memo:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def memo(node, n):
    if n == 0:
        return node.value
    elif n % 2 != 0:
        return memo(node.left, n // 2)
    else:
        return memo(node.right, n // 2 - 1)

def nats():
    def generate(node):
        return Memo(node.value + 1, (lambda x: x*2 + 1)(node), (lambda x: x*2)(node))
    return Memo(0, generate(nats()), generate(nats()))

def partitions():
    return partitionP(nats())

def partitionP(n):
    if n < 2:
        return 1
    else:
        terms = [memo(partitions(), n - i) for i in takeWhile(lambda x: x <= n, ofsets)]
        signs = cycle([1, 1, -1, -1])
        return sum([a*b for a, b in zip(signs, terms)])

ofsets = list(accumulate(lambda a, b: a+b, mix([i for i in range(1, 100, 2)], [i for i in range(1, 100, 2)])))
def mix(a, b):
    return [val for pair in zip(a, b) for val in pair]

print(partitionP(6666))
```