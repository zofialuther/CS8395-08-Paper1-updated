import random

def answer():
    return 24

def play():
    round()
    play()

def round():
    Ns = [random.randint(1, 10) for _ in range(4)]
    print('Digits:', Ns)
    input_str = input()
    while input_str != "stop":
        result = parse(Ns, [], input_str)
        if result == 'correct':
            print(result)
        else:
            print(result)
        input_str = input()

def parse(Ns, stack, input_str):
    if not input_str:
        return 'correct' if answer() == stack[0] else 'wrong'
    elif input_str[0] in ['+', '-', '*', '/']:
        if len(stack) < 2:
            return 'wrong'
        else:
            op = input_str[0]
            x = stack.pop(0)
            y = stack.pop(0)
            if op == '+':
                z = x + y
            elif op == '-':
                z = x - y
            elif op == '*':
                z = x * y
            elif op == '/':
                z = x // y
            stack.insert(0, z)
            return parse(Ns, stack, input_str[1:])
    elif input_str[0] == ' ':
        return parse(Ns, stack, input_str[1:])
    else:
        num_str = ''
        while input_str and input_str[0].isdigit():
            num_str += input_str[0]
            input_str = input_str[1:]
        num = int(num_str)
        if num in Ns:
            stack.insert(0, num)
            return parse(Ns, stack, input_str)
        else:
            return 'wrong'

def main():
    random.seed()
    play()

if __name__ == "__main__":
    main()