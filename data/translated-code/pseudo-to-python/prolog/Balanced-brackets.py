from itertools import product

def rosetta_brackets():
    test_brackets([])
    test_brackets(['[',']'])
    test_brackets(['[',']','[',']'])
    test_brackets(['[','[',']','[',']',']'])
    test_brackets([']','['])
    test_brackets([']','[',']','['])
    test_brackets(['[',']',']','[','[',']'])

def balanced_brackets():
    gen_bracket(2,  [], []), test_brackets(B1)
    gen_bracket(4,  [], []), test_brackets(B2)
    gen_bracket(4,  [], []), test_brackets(B3)
    gen_bracket(6,  [], []), test_brackets(B4)
    gen_bracket(6,  [], []), test_brackets(B5)
    gen_bracket(8,  [], []), test_brackets(B6)
    gen_bracket(8,  [], []), test_brackets(B7)
    gen_bracket(10, [], []), test_brackets(B8)
    gen_bracket(10, [], []), test_brackets(B9)

def test_brackets(Goal):
    if len(Goal) == 0:
        print("(empty)")
    else:
        for g in Goal:
            print(g)
    if balanced_brackets(Goal, []):
        print("succeed")
    else:
        print("failed")

def balanced_brackets(Goal, L):
    if len(Goal) == 0:
        return True
    if len(Goal) == 1:
        return False
    if Goal[0] == '[' and Goal[-1] == ']':
        return balanced_brackets(Goal[1:-1], L)
    if Goal[0] == '[' and Goal[-1] == ']':
        return balanced_brackets(Goal[1:], L)
    if Goal[0] == ']' and Goal[-1] == '[':
        return balanced_brackets(Goal[:-1], L)
    return False

def gen_bracket(N, B, L):
    if N == 0:
        yield B, L
    else:
        for b in ['[', ']']:
            for bp, lp in gen_bracket(N-1, B + [b], L):
                yield bp, lp