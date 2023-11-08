def squeeze(s, char):
    result = ""
    for i in range(len(s)):
        if s[i] == char or s[i] != s[i-1]:
            result += s[i]
    return result

test_strings = ["aaabbbccc", "xxxxxyyyyzzz", "1122334455"]
test_char = "b"

for string in test_strings:
    print("Original string:", string)
    print("Squeezed string:", squeeze(string, test_char))