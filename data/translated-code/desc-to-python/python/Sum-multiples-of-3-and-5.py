def sum35a(n):
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

def sum35b(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

def sum35c(n):
    threes = (n-1) // 3
    fives = (n-1) // 5
    fifteens = (n-1) // 15
    return 3 * threes * (threes + 1) // 2 + 5 * fives * (fives + 1) // 2 - 15 * fifteens * (fifteens + 1) // 2

print(sum35a(10))
print(sum35b(10))
print(sum35c(10))

print(sum35a(1000))
print(sum35b(1000))
print(sum35c(1000))