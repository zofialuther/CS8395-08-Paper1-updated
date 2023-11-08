```python
def encode(text, offset):
    result = ""
    for char in text:
        if char.isalpha():
            shift = (ord(char) + offset - 65) % 26 + 65 if char.isupper() else (ord(char) + offset - 97) % 26 + 97
            result += chr(shift)
        else:
            result += char
    return result

def decode(text, offset):
    return encode(text, -offset)

if __name__ == "__main__":
    message = "Hello, World!"
    offset = 3
    encoded_message = encode(message, offset)
    decoded_message = decode(encoded_message, offset)

    print("Original message:", message)
    print("Encoded message:", encoded_message)
    print("Decoded message:", decoded_message)
```