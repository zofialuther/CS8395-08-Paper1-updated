def multisplit(text, separators):
    segments = []
    positions = []
    start = 0
    for i in range(len(text)):
        if text[i] in separators:
            segments.append(text[start:i])
            positions.append((text[i], i))
            start = i + 1
    segments.append(text[start:])
    return segments, positions

# Example usage
text1 = "Hello, world! This is a test."
separators1 = [',', '!', ' ']
result1 = multisplit(text1, separators1)
print(result1)

text2 = "This/is/a/test"
separators2 = ['/', 'a']
result2 = multis   plit(text2, separators2)
print(result2)