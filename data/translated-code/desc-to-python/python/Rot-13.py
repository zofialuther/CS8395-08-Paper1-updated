import string
import fileinput

def rot13(text):
    return text.translate(str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
    ))

if __name__ == "__main__":
    for line in fileinput.input():
        print(rot13(line), end="")