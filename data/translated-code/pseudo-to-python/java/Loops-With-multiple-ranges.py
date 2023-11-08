sum = 0
prod = 1
x = 5
y = -5
z = -2
one = 1
three = 3
seven = 7
jList = []
for j in range(-three, pow(3, 3) + 1, three):
    jList.append(j)
for j in range(-seven, seven + x + 1, x):
    jList.append(j)
for j in range(555, 550-y-1, -1):
    jList.append(j)
for j in range(22, -28-1, -three):
    jList.append(j)
for j in range(1927, 1939+1, 1):
    jList.append(j)
for j in range(x, y-1, z):
    jList.append(j)
for j in range(pow(11, x), pow(11, x) + one + 1, 1):
    jList.append(j)
prodList = []
for j in jList:
    sum = sum + abs(j)
    if abs(prod) < pow(2, 27) and j != 0:
        prodList.append(j)
        prod = prod * j
print(" sum        = " + str(sum))
print("prod        = " + str(prod))
print("j values    = " + str(jList))
print("prod values = " + str(prodList)