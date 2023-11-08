```python
class SelfDescribingNumbers:
    def isSelfDescribing(self, num):
        num_str = str(num)
        for i in range(len(num_str)):
            count = 0
            for j in range(len(num_str)):
                if int(num_str[j]) == i:
                    count += 1
            if count != int(num_str[i]):
                return False
        return True

def main():
    sdn = SelfDescribingNumbers()
    for num in range(100000000):
        if sdn.isSelfDescribing(num):
            print(num)

main()
```