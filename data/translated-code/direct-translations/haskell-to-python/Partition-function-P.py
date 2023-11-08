from functools import lru_cache

@lru_cache(maxsize=None)
def memo(node, n):
    if n == 0:
        return node[0]
    elif n % 2 != 0:
        return memo(node[1], n // 2)
    else:
        return memo(node[2], n // 2 - 1)

def nats():
    def node(x):
        return (x, node(2*x + 1), node(2*x + 2))
    return node(0)

def partitions():
    @lru_cache(maxsize=None)
    def partitionP(n):
        if n < 2:
            return 1
        else:
            terms = [memo(partitions, n - i) for i in ofsets if i <= n]
            signs = cycle([1, 1, -1, -1])
            return sum(sign * term for sign, term in zip(signs, terms))

    return partitionP

def ofsets():
    def mix(a, b):
        return [x for pair in zip(a, b) for x in pair]
    
    a = [i for i in range(1, 10000, 2)]
    b = [i for i in range(1, 10000, 2)]
    return list(itertools.accumulate(mix(a, b)))

def main():
    print(partitions()(6666))

if __name__ == "__main__":
    main()