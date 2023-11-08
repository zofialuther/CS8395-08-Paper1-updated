```python
def frequency(File):
    with open(File, 'r') as f:
        code = [ord(c) for c in f.read()]
    lst_char_code = list(filter(my_code_type, code))
    lst_char = list(map(my_upcase, lst_char_code))
    sort_lst_char = sorted(lst_char)
    freq = packList(sort_lst_char)
    for pair in freq:
        my_write(pair)

def my_write(pair):
    num = str(pair[0])
    atom = pair[1]
    print(f'Number of {atom} : {num}')

def my_code_type(code):
    return code.isalpha()

def my_upcase(char_code):
    return chr(char_code).upper()

def packList(lst):
    packed = []
    if len(lst) == 0:
        return packed
    elif len(lst) == 1:
        return [[1, lst[0]]]
    else:
        return packListHelper(lst, packed)

def packListHelper(lst, packed):
    if len(lst) == 0:
        return packed
    else:
        first = lst[0]
        rest = lst[1:]
        xRun, rest = run(first, rest)
        packed.append(xRun)
        return packListHelper(rest, packed)

def run(var, rest):
    n = 1
    for i, val in enumerate(rest):
        if var == val:
            n += 1
        else:
            return [n, var], rest[i:]
    return [n, var], []
```