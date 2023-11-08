string = "abcdefgh"

# Extracting a substring from a specific position and of a certain length
substring1 = string[2:5]

# Extracting a substring from a known character or substring within the string
substring2 = string[string.index("d"):]

print(substring1)
print(substring2)