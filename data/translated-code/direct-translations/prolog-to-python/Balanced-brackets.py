```python
import random

def test_brackets(Goal):
    if Goal == []:
        print('(empty)')
    else:
        for item in Goal:
            print(item, end="")
    if balanced_brackets(Goal, []):
        print(' succeed')
    else:
        print(' failed')

# grammar of balanced brackets
def balanced_brackets(Goal, _):
    if Goal == []:
        return True
    if Goal[0] == '[' and Goal[-1] == ']':
        return balanced_brackets(Goal[1:-1], [])
    if Goal[0] == '[' and Goal[1] == ']' and len(Goal) >= 2:
        return balanced_brackets(Goal[2:], [])
    return False

# generator of random brackets
def gen_bracket(N):
    if N == 0:
        return []
    else:
        R = random.randint(0, 1)
        return [bracket(R)] + gen_bracket(N-1)

def bracket(R):
    if R == 0:
        return '['
    else:
        return ']'

test_brackets([])
test_brackets(['[',']'])
test_brackets(['[',']','[',']'])
test_brackets(['[','[',']','[',']',']'])
test_brackets([']','['])
test_brackets([']','[',']','['])
test_brackets(['[',']',']','[','[',']'])

gen_bracket(2)
gen_bracket(4)
gen_bracket(4)
gen_bracket(6)
gen_bracket(6)
gen_bracket(8)
gen_bracket(8)
gen_bracket(10)
gen_bracket(10)
```