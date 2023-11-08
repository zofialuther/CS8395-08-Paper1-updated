def sumDigits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

count = 0
i = 1
while count < 20:
    if i % sumDigits(i) == 0:
        print(i)
        count += 1
    i += 1

print()

i = 1001
while True:
    if i % sumDigits(i) == 0:
        print(i)
        break
    i += 1