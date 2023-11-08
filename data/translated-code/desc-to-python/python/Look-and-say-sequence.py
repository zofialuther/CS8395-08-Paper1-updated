import re

def lookandsay(input_str):
    result = ''
    for match in re.finditer(r'(\d)\1*', input_str):
        result += str(len(match.group(0))) + match.group(1)
    return result

num = "1"
for i in range(10):
    print(num)
    num = lookandsay(num)