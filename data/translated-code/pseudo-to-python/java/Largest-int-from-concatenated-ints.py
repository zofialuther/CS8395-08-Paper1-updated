```python
from functools import cmp_to_key

class IntConcat:
    @staticmethod
    def SORTER(o1, o2):
        o1s = str(o1)
        o2s = str(o2)
        if len(o1s) == len(o2s):
            return int(o2s) - int(o1s)
        else:
            mlen = max(len(o1s), len(o2s))
            while len(o1s) < mlen * 2:
                o1s += o1s
            while len(o2s) < mlen * 2:
                o2s += o2s
            return int(o2s) - int(o1s)

def main():
    ints1 = [123, 45, 678, 9]
    result1 = sorted(ints1, key=cmp_to_key(IntConcat.SORTER))
    print(''.join(map(str, result1)))
    
    ints2 = [987, 654, 32, 1]
    result2 = sorted(ints2, key=cmp_to_key(IntConcat.SORTER))
    print(''.join(map(str, result2)))

main()
```