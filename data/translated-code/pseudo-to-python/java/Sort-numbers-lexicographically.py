def lexOrder(n):
    first = 1
    last = n
    if n < 1:
        first = n
        last = 1
    result = []
    for i in range(first, last+1):
        result.append(str(i))
    result.sort()
    for i in range(len(result)):
        result[i] = int(result[i])
    return result

print("In lexicographical order:\n")
ints = [0, 5, 13, 21, -22]
for n in ints:
    print(str(n) + ": " + str(lexOrder(n)))