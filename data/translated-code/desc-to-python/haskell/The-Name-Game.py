```python
def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

def is_special_char(char):
    special_chars = "!@#$%^&*()_+{}|:\"<>?=-[]\;',./`~"
    return char in special_chars

def shorten_name(name):
    if len(name) < 2:
        return name
    elif is_vowel(name[0]):
        return name
    elif is_special_char(name[0]):
        return name
    else:
        return name[1:]

def create_line(prefix, name):
    return f"{prefix}, {prefix} bo B{shorten_name(name)}\nBonana fanna fo F{shorten_name(name)}\nFee fy mo M{shorten_name(name)}\n{prefix}!"

def name_game(name):
    prefix = name.capitalize()
    return create_line(prefix, name)

def main():
    names = ["Katie", "Bob", "Fred", "Lucy"]
    for name in names:
        print(name_game(name))

main()
```