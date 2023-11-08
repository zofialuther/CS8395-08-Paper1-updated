def caesar(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

message = "Hello, World!"
encoded_message = caesar(message, 3)
print("Encoded message:", encoded_message)

decoded_message = caesar(encoded_message, -3)
print("Decoded message:", decoded_message)