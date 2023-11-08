```python
class SubstitutionCipher:
    
    key = "]kYV}(!7P$n5_0i R:?jOWtF/=-pe'AD&@r6%ZXs\"v*N" + "[#wSl9zq2^+g;LoB`aGh{3.HIu4fbK)mU8|dMET><,Qc\\C1yxJ"
    
    text = "Here we have to do is there will be a input/source " + "file in which we are going to Encrypt the file by replacing every " + "upper/lower case alphabets of the source file with another " + "predetermined upper/lower case alphabets or symbols and save " + "it into another output/encrypted file and then again convert " + "that output/encrypted file into original/decrypted file. This " + "type of Encryption/Decryption scheme is often called a " + "Substitution Cipher."
    
    def main(self):
        enc = self.encode(self.text)
        print("Encoded: " + enc)
        print("\nDecoded: " + self.decode(enc))
    
    def encode(self, s):
        sb = []
        
        for c in s:
            sb.append(self.key[ord(c) - 32])
        
        return ''.join(sb)
    
    def decode(self, s):
        sb = []
        
        for c in s:
            sb.append(chr(self.key.index(c) + 32))
        
        return ''.join(sb)

SubstitutionCipher().main()
```