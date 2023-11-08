words = ["", ".", "abcABC", "XYZ ZYX", "1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ"]

for word in words:
    seen = set()
    for i, char in enumerate(word):
        if char in seen:
            print(f"The word '{word}' has a repeated character at position {i}")
            break
        seen.add(char)
    else:
        print(f"The word '{word}' has all unique characters")