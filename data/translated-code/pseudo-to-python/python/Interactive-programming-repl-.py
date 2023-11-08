def f(string1, string2, separator):
    return separator.join([string1, '', string2])

print(f('Rosetta', 'Code', ':'))