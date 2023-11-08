```python
class IntToWords:
    def int2Text(self, num: int) -> str:
        pass

    def main(self):
        # Test the int2Text method with various input numbers
        num1 = 123456789
        num2 = -987654321
        num3 = 1000000000
        
        print(self.int2Text(num1))
        print(self.int2Text(num2))
        print(self.int2Text(num3))

# Create an instance of IntToWords and call the main method
int_to_words = IntToWords()
int_to_words.main()
```