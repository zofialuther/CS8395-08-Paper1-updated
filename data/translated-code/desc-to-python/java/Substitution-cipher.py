class SubstitutionCipher:
    def __init__(self, key):
        self.key = key

    def encode(self, text):
        encoded_text = ""
        for char in text:
            if char in self.key:
                encoded_text += self.key[self.key.index(char)]
            else:
                encoded_text += char
        return encoded_text

    def decode(self, encoded_text):
        decoded_text = ""
        for char in encoded_text:
            if char in self.key:
                decoded_text += self.key[self.key.index(char)]
            else:
                decoded_text += char
        return decoded_text

if __name__ == "__main__":
    key = "abcdefghijklmnopqrstuvwxyz"
    cipher = SubstitutionCipher(key)
    text = "hello world"
    encoded_text = cipher.encode(text)
    decoded_text = cipher.decode(encoded_text)
    print("Original Text:", text)
    print("Encoded Text:", encoded_text)
    print("Decoded Text:", decoded_text)