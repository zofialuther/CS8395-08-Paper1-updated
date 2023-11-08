def main():
    passing = [123, 12345, 1234567, 987654321, 10001, -10001, -123, -100, 100, -12345, float('-inf'), float('inf')]
    failing = [1, 2, -1, -10, 2002, -2002, 0, float('-inf'), float('inf')]

    for n in passing:
        print("middleThreeDigits(n): " + middleThreeDigits(n))

    for n in failing:
        print("middleThreeDigits(n): " + middleThreeDigits(n))

def middleThreeDigits(n):
    s = str(n)
    if s[0] == '-':
        s = s[1:]
    length = len(s)
    if length < 3 or length % 2 == 0:
        return "Need odd and >= 3 digits"
    mid = length // 2
    return s[mid - 1:mid + 2]