import ctypes

def runtime_entry():
    prompt = input('')
    rot13()

def rot13():
    ch = ord(input())
    if ch == -1:
        pass
    else:
        rot = rot13_char(ch)
        print(chr(rot), end='')
        rot13()

def rot13_char(ch):
    if ch.isalpha():
        up = ch.upper()
        letter = ord(up) - ord('A')
        rot = ch + ((letter + 13) % 26) - letter
        return rot
    else:
        return ch

runtime_entry()