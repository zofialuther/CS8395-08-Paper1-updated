def properDivsSum(n):
    sum = 0
    for i in range(1, (n + 1) // 2 + 1):
        if n % i == 0:
            sum = sum + i
    return sum

def main():
    limit = 20000
    map = {}
    for number in range(1, limit + 1):
        map[number] = properDivsSum(number)
    for number in range(1, limit + 1):
        m = map.get(number)
        if m > number and m <= limit and map.get(m) == number:
            print(number, m)