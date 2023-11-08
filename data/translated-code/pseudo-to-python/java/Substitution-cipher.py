def encode(s):
    sb = ""

    for c in s:
        sb += key[ord(c) - 32]

    return sb

def decode(s):
    sb = ""

    for c in s:
        sb += chr(key.index(c) + 32)

    return sb

def main():
    enc = encode(text)
    print("Encoded: " + enc)
    print("Decoded: " + decode(enc))