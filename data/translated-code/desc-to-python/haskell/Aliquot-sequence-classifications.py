```python
def divisors(num):
    divisors_list = []
    for i in range(1, num):
        if num % i == 0:
            divisors_list.append(i)
    return divisors_list

def aliquot(num):
    sequence = [num]
    while True:
        div_sum = sum(divisors(sequence[-1]))
        if div_sum in sequence or div_sum == sequence[-1]:
            break
        sequence.append(div_sum)
    return sequence

def classify(sequence):
    div_sum = sum(sequence[:-1])
    if div_sum == sequence[-1]:
        return "Perfect"
    elif div_sum in sequence:
        return "Amicable"
    elif len(set(sequence)) == len(sequence):
        return "Sociable"
    elif sequence[-1] == 0:
        return "Aspiring"
    elif sequence[-1] in sequence[:-1]:
        return "Cyclic"
    else:
        return "Nonterminating"

def main():
    numbers = [28, 496, 8128, 12496, 33550336]
    for num in numbers:
        sequence = aliquot(num)
        classification = classify(sequence)
        print(f"Number: {num}, Sequence: {sequence}, Classification: {classification}")

if __name__ == "__main__":
    main()
```