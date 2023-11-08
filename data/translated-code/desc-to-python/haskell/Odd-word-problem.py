```python
def split(s):
    alpha = ''
    non_alpha = ''
    for char in s:
        if char.isalpha():
            alpha += char
        else:
            non_alpha += char
    return (alpha, non_alpha)

def parse(s):
    if len(s) == 0:
        return ''
    else:
        alpha, non_alpha = split(s)
        return parse(s[:-1]) + non_alpha[::-1] + alpha

def main():
    import sys
    sys.stdin = open(0)
    sys.stdout = open(1, 'w')
    while True:
        user_input = input()
        if user_input == '.':
            break
        parsed_result = parse(user_input)
        print(parsed_result + '.')

if __name__ == "__main__":
    main()
```