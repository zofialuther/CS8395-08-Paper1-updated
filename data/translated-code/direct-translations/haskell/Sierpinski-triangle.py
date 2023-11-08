from itertools import accumulate
from operator import xor

def sierpinski(n):
    def rule90(m):
        return list(accumulate(range(1, m), initial="*", func=lambda x, y: "".join(map(lambda a, b: " " if a == b else "*", " " + x, x + " "))))
    
    def spacing(x, s, w):
        return "".join([w, " ".join(x), "\n", s]), w + " "
    
    result, _ = accumulate(rule90(2**n), initial=("", ""), func=lambda x, y: spacing(y, x[0], x[1]))
    return result

print(sierpinski(4))