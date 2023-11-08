import re

def lookandsay(s):
    return re.sub(r'(.)\1*', lambda x: str(len(x.group(0))) + x.group(1), s)

num = "1"
for _ in range(10):
    print(num)
    num = lookandsay(num)