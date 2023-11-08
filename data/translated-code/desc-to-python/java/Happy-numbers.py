```python
class Happy:
    
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1

if __name__ == "__main__":
    happy = Happy()
    count = 0
    num = 1
    while count < 8:
        if happy.isHappy(num):
            print(num)
            count += 1
        num += 1
```