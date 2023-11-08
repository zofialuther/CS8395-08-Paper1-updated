```python
class Comb:
    @staticmethod
    def bitprint(x, n):
        for i in range(n):
            print((x >> i) & 1, end="")
        print()

    @staticmethod
    def bitcount(x):
        count = 0
        while x:
            x &= (x - 1)
            count += 1
        return count

    @staticmethod
    def comb(n, r):
        result = []
        for i in range(1 << n):
            if Comb.bitcount(i) == r:
                result.append(i)
        result.sort()
        return result

    @staticmethod
    def main():
        print(Comb.comb(3, 5))

Comb.main()
```