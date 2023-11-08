def semiprime(n):
    count = 0
    for i in range(2, n+1):
        while n % i == 0:
            n = n // i
            count = count + 1
        if count > 2:
            return False
    if count == 2:
        return True
    else:
        return False

print(semiprime(1679))

result = []
for n in range(1, 101):
    if semiprime(n) == True:
        result.append(n)
print(result)