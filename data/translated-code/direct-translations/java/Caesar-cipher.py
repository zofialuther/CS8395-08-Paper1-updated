class Cipher:
    def main(args):
        str = "The quick brown fox Jumped over the lazy Dog"
        print( Cipher.encode( str, 12 ))
        print( Cipher.decode( Cipher.encode( str, 12), 12 ))

    def decode(enc, offset):
        return encode(enc, 26-offset)

    def encode(enc, offset):
        offset = offset % 26 + 26
        encoded = ""
        for i in enc:
            if i.isalpha():
                if i.isupper():
                    encoded += chr(65 + (ord(i) - 65 + offset) % 26)
                else:
                    encoded += chr(97 + (ord(i) - 97 + offset) % 26)
            else:
                encoded += i
        return encoded