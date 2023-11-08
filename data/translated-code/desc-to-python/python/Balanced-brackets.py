import numpy as np

def gen(length):
    brackets = np.random.choice(['[', ']'], size=length)
    return ''.join(brackets)

def balanced(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '[':
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

for _ in range(10):
    random_brackets = gen(10)
    is_balanced = balanced(random_brackets)
    print(f"Generated brackets: {random_brackets}, Balanced: {is_balanced}")