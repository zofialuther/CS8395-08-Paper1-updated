# All equal
all(a == nexta for a, nexta in zip(strings, strings[1:]))

# Strictly ascending
all(a < nexta for a, nexta in zip(strings, strings[1:]))

# Concise all equal
len(set(strings)) == 1

# Concise (but not particularly efficient) ascending
sorted(strings, reverse=True) == strings