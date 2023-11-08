import ctypes

def runtime_entry(start):
    input(_, '')
    rot13()

def rot13():
    Ch = get0()
    if Ch == endfile:
        return
    else:
        rot13_char(Ch, Rot)
        put(Rot)
        rot13()

def rot13_char(Ch, Rot):
    if Ch.isalpha():
        Up = Ch.upper()
        Letter = ord(Up) - ord('A')
        Rot = chr(ord(Ch) + ((Letter + 13) % 26) - Letter)
    else:
        Rot = Ch