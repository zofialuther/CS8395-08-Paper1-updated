import re

def encode(text):
    return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), text)

def decode(text):
    return re.sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), text)

textin = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
assert decode(encode(textin)) == textin