import itertools

def harshad(n):
    for num in itertools.count():
        if num % sum(int(digit) for digit in str(num)) == 0:
            yield num

harshad_nums = list(itertools.islice(harshad(1), 20))

for num in harshad(1000):
    if num > 1000:
        print(num)
        break