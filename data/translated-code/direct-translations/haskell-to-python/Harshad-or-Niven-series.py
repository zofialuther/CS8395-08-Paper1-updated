from itertools import islice

def harshads():
    n = 1
    while True:
        if n % digit_sum(n) == 0:
            yield n
        n += 1

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

if __name__ == "__main__":
    h = harshads()
    print(list(islice(h, 20)))
    h = harshads()
    print(next(x for x in h if x > 1000))