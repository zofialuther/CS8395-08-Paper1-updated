```python
from itertools import groupby

def encode(s):
    return ''.join(str(len(list(group))) + key for key, group in groupby(s))

def decode(s):
    result = ""
    i = 0
    while i < len(s):
        num = ""
        while s[i].isdigit():
            num += s[i]
            i += 1
        result += int(num) * s[i]
        i += 1
    return result

test_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
print("encode", test_string)
encoded_string = encode(test_string)
print(encoded_string)
print("decode", encoded_string)
decoded_string = decode(encoded_string)
print(decoded_string)
```