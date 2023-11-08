import random
import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def calculate_rpn(expression):
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            result = ops[token](a, b)
            stack.append(result)
    return stack[0]

def generate_digits():
    return [random.randint(1, 9) for _ in range(4)]

def main():
    digits = generate_digits()
    print("The 4 digits are:", digits)
    user_input = input("Enter your expression in reverse polish notation: ").split()
    try:
        result = calculate_rpn(user_input)
        if result == 24:
            print("Congratulations! Your expression is correct.")
        else:
            print("Sorry, the result is not 24.")
    except (IndexError, ValueError, ZeroDivisionError):
        print("Invalid expression.")

if __name__ == "__main__":
    main()