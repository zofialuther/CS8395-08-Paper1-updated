def properDivsSum(n):
    divs_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divs_sum += i
    return divs_sum

deficient = 0
perfect = 0
abundant = 0

for i in range(1, 20001):
    div_sum = properDivsSum(i)
    if div_sum < i:
        deficient += 1
    elif div_sum == i:
        perfect += 1
    else:
        abundant += 1

print("Deficient: " + str(deficient))
print("Perfect: " + str(perfect))
print("Abundant: " + str(abundant))