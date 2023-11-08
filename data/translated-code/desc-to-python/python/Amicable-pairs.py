```python
def sum_of_divisors(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors)

def are_amicable(a, b):
    return sum_of_divisors(a) == b and sum_of_divisors(b) == a

def find_amicable_pairs(limit):
    amicable_pairs = []
    for i in range(1, limit):
        for j in range(i, limit):
            if are_amicable(i, j):
                amicable_pairs.append((i, j))
    return amicable_pairs

def main():
    limit = 20000
    amicable_pairs = find_amicable_pairs(limit)
    for pair in amicable_pairs:
        print(pair)

if __name__ == "__main__":
    main()
```