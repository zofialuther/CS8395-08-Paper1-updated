ucode = ''.join(chr(int(n[2:], 16)) for n in
                 'U+006B U+0301 U+0075 U+032D U+006F U+0304 U+0301 U+006E'.split())

def say_rev(input_string):
    input_string = input_string[::-1]
    print(input_string)

say_rev(ucode)