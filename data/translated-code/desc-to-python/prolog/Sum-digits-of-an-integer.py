```python
def digit_sum(N, Base, Sum):
    if N == 0:
        return Sum
    else:
        return digit_sum(N // Base, Base, Sum + N % Base)

def test_digit_sum(N, Base):
    print(digit_sum(N, Base, 0))

def main():
    test_digit_sum(123, 10)
    test_digit_sum(1010, 2)
    test_digit_sum(777, 8)

main()
```