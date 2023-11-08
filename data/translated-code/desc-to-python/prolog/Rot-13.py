import ctypes

def rot13_char(char):
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    else:
        return char

def rot13(input_string):
    return ''.join(rot13_char(char) for char in input_string)

def runtime_entry():
    user_input = input("Enter a string to encrypt: ")
    encrypted_string = rot13(user_input)
    print("Encrypted string: " + encrypted_string)

runtime_entry()