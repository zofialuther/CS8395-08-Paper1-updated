input_string = input()
result = ""

words = input_string.split(" ")

for word in words:
    if len(word) % 2 == 0:
        result += word
    else:
        result += word[::-1]

print(result)