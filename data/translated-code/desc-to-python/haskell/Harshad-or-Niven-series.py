def rem(a, b):
    return a % b

def unfoldr(f, x):
    if f(x):
        return [x]
    else:
        return [x] + unfoldr(f, f(x))

def digitSum(n):
    return sum(unfoldr(lambda x: x == 0, lambda x: x // 10, n))

def harshads():
    return list(filter(lambda x: rem(x, digitSum(x)) == 0, range(1, 10000)))

def main():
    numbers = harshads()
    print(numbers[:20])
    print(next(x for x in numbers if x > 1000))

main()