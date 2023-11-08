# First code
for i in range(1, 11):
    divisors = [x for x in range(1, i) if i % x == 0]
    print(f"The proper divisors of {i} are {divisors}")

# Second code
max_divisors = 0
number_with_max_divisors = 0
for i in range(1, 20001):
    divisors = [x for x in range(1, i) if i % x == 0]
    if len(divisors) > max_divisors:
        max_divisors = len(divisors)
        number_with_max_divisors = i
print(f"The number {number_with_max_divisors} has {max_divisors} proper divisors, which is the highest within the given range.")