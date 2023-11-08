def mertens(count):
    mertens_numbers = [0] * count
    m = 0
    for n in range(1, count):
        m += mu(n)
        mertens_numbers[n] = m
    return mertens_numbers

def mu(n):
    if n == 1:
        return 1
    else:
        divisors = [1]
        for i in range(2, n + 1):
            if n % i == 0:
                divisors.append(i)
        if len(divisors) % 2 == 0:
            return 1
        else:
            return -1

mertens_numbers = mertens(100)
for i, mertens_number in enumerate(mertens_numbers):
    print("Mertens number", i, ":", mertens_number)

zero_count = mertens_numbers.count(0)
print("Number of times Mertens function equals zero:", zero_count)

cross_zero_count = sum(1 for x, y in zip(mertens_numbers, mertens_numbers[1:]) if x * y < 0)
print("Number of times Mertens function crosses zero:", cross_zero_count)