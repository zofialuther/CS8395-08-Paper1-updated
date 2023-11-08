```python
from typing import List

def sum35(n: int) -> int:
    return sumMul(n, 3) + sumMul(n, 5) - sumMul(n, 15)

def sumMul(n: int, f: int) -> int:
    n1 = (n - 1) // f
    return f * n1 * (n1 + 1) // 2

def main() -> None:
    print(sum35(1000))
    print(sum35(100000000000000000000000000000000))
    print(sumMulS(1000, [3, 5]))
    print(sumMulS(10000000, [2, 3, 5, 7, 11, 13]))

def pairLCM(nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            result.append(lcm(nums[i], nums[j]))
    return result

def sumMulS(n: int, s: List[int]) -> int:
    unique_s = list(set(s))
    return sum(map(lambda x: sumMul(n, x), unique_s)) - sum(pairLCM(unique_s))

def lcm(a: int, b: int) -> int:
    return abs(a*b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    main()
```