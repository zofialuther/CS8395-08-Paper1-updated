```python
def find_divisors(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return divisors

def classify_number(num):
    divisors_sum = sum(find_divisors(num))
    if divisors_sum < num:
        return "deficient"
    elif divisors_sum == num:
        return "perfect"
    else:
        return "abundant"

def main():
    classifications = {'deficient': 0, 'perfect': 0, 'abundant': 0}
    for i in range(1, 20001):
        classification = classify_number(i)
        classifications[classification] += 1
    print(classifications)

main()
```