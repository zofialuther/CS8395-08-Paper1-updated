import re

def lookandsay(string):
    return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), string)

num = "1"
for i in range(10):
    print(num)
    num = lookandsay(num)