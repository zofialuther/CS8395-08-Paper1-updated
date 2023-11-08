limiter = 100
primelist = []

def primer(num):
    for i in primelist:
        if num % i == 0:
            return False
    primelist.append(num)
    return True

for num in range(2, limiter):
    if primer(num):
        print(num, "is a prime number")

print("Total number of prime numbers found:", len(primelist))
print("List of prime numbers:", primelist)