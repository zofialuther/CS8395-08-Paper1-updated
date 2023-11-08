import random
import string

def generate_key():
    return ''.join(random.choice(string.printable) for _ in range(50))

def encode(plaintext, key):
    encoded_text = ""
    for i in range(len(plaintext)):
        encoded_text += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return encoded_text

def decode(encoded_text, key):
    return encode(encoded_text, key)

key = generate_key()
plaintext = "Hello, world!"
encoded_text = encode(plaintext, key)
decoded_text = decode(encoded_text, key)

print("Original: ", plaintext)
print("Encoded: ", encoded_text)
print("Decoded: ", decoded_text)