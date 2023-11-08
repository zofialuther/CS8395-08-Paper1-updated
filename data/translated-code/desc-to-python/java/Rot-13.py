```python
import sys

def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 13 if char.islower() else -13
            result += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result

if len(sys.argv) > 1:
    input_text = " ".join(sys.argv[1:])
    print(rot13(input_text))
else:
    input_text = input("Enter text to encrypt/decrypt: ")
    print(rot13(input_text))
```