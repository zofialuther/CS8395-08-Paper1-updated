```python
class GrayCode:
    def grayEncode(self, n: int) -> int:
        pass
    
    def grayDecode(self, n: int) -> int:
        pass
    
    def grayEncodeBigInteger(self, n: int) -> int:
        pass
    
    def grayDecodeBigInteger(self, n: int) -> int:
        pass
    
    def alternativeGrayEncode(self, n: int) -> int:
        pass
    
    def alternativeGrayDecode(self, n: int) -> int:
        pass
    
if __name__ == "__main__":
    gc = GrayCode()
    
    num = 10
    binary = bin(num)[2:]
    gray = gc.grayEncode(num)
    decoded = gc.grayDecode(gray)
    print(f"Number: {num}, Binary: {binary}, Gray Code: {gray}, Decoded: {decoded}")
    
    big_num = 123456789012345678901234567890
    gray_big = gc.grayEncodeBigInteger(big_num)
    decoded_big = gc.grayDecodeBigInteger(gray_big)
    print(f"Big Number: {big_num}, Gray Code: {gray_big}, Decoded: {decoded_big}")
```