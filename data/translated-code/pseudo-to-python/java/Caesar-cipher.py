class Cipher:
    def main(self):
        string = "The quick brown fox Jumped over the lazy Dog"
        print(self.encode(string, 12))
        print(self.decode(self.encode(string, 12), 12))

    def decode(self, enc, offset):
        return self.encode(enc, 26-offset)

    def encode(self, enc, offset):
        offset = offset % 26 + 26
        encoded = ""
        for i in enc:
            if i.isalpha():
                if i.isupper():
                    encoded += chr(((ord(i) - ord('A') + offset) % 26) + ord('A'))
                else:
                    encoded += chr(((ord(i) - ord('a') + offset) % 26) + ord('a'))
            else:
                encoded += i
        return encoded