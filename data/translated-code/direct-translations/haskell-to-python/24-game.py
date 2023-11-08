```python
import random
import operator

def calc(xs):
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    stack = []
    for x in xs:
        if x.isdigit():
            stack.append(int(x))
        elif x in ops:
            if len(stack) < 2:
                return "Too few values before " + x
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[x](a, b))
        else:
            return "Unrecognized symbol: " + x
    if len(stack) == 1:
        return stack[0]
    else:
        return "Too few operators"

def process_guess(digits, xs):
    if not all(c.isdigit() for c in "".join(xs)):
        return "Wrong digits used"
    result = calc(xs)
    if result == 24:
        return "Correct"
    else:
        return str(result) + " is wrong"

def guess_loop(digits):
    guess = input("Your expression: ")
    result = process_guess(digits, guess.split())
    if isinstance(result, str):
        print(result)
        guess_loop(digits)
    else:
        print(result)

def main():
    print("THE 24 GAME\n")
    print("Given four digits in the range 1 to 9")
    print("Use the +, -, *, and / operators in reverse polish notation")
    print("To show how to make an answer of 24.\n")
    random.seed()
    digits = sorted(random.sample(range(1, 10), 4))
    print("Your digits:", " ".join(map(str, digits)))
    guess_loop(digits)

if __name__ == "__main__":
    main()
```