import random

def main():
    digits = randomDigits()
    print("Make 24 using these digits:", digits)
    user_input = input("> ")
    s = []
    total = 0
    for c in user_input:
        if c.isdigit():
            d = int(c)
            total += 1 << (d * 5)
            s.append(float(d))
        elif c in "+-*/":
            s.append(applyOperator(s.pop(), s.pop(), c))
    if tallyDigits(digits) != total:
        print("Not the same digits.")
    elif abs(24 - s[-1]) < 0.001:
        print("Correct!")
    else:
        print("Not correct.")

def applyOperator(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return b - a
    elif c == '*':
        return a * b
    elif c == '/':
        return b / a
    else:
        return float('nan')

def tallyDigits(a):
    total = 0
    for i in range(4):
        total += 1 << (a[i] * 5)
    return total

def randomDigits():
    result = []
    for i in range(4):
        result.append(random.randint(1, 9))
    return result

if __name__ == "__main__":
    main()