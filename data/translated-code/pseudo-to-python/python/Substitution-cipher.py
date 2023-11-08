from string import printable
import random

EXAMPLE_KEY = ''.join(sorted(printable, key=lambda _:random.random()))

def encode(plaintext, key):
    encodedText = ""
    for char in plaintext:
        index = printable.index(char)
        encodedChar = key[index]
        encodedText += encodedChar
    return encodedText

def decode(plaintext, key):
    decodedText = ""
    for char in plaintext:
        index = key.index(char)
        decodedChar = printable[index]
        decodedText += decodedChar
    return decodedText

original = "A simple example."
encoded = encode(original, EXAMPLE_KEY)
decoded = decode(encoded, EXAMPLE_KEY)
print("The original is: " + original)
print("Encoding it with the key: " + EXAMPLE_KEY)
print("Gives: " + encoded)
print("Decoding it by the same key gives: " + decoded)