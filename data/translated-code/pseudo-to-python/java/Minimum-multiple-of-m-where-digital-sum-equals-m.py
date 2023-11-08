def digitSum(aN):
    sum = 0
    while aN > 0:
        sum = sum + (aN % 10)
        aN = aN // 10
    return sum

for n in range(1, 71):
    k = 0
    while digitSum(k + n) != n:
        k += n
    print(k / n, end="\n" if n % 10 == 0 else " ")