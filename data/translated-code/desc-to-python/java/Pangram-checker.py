```python
class Pangram:
    def isPangram(self, s):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            if char not in s.lower():
                return False
        return True

if __name__ == "__main__":
    p = Pangram()
    test_strings = ["The quick brown fox jumps over the lazy dog", "Pack my box with five dozen liquor jugs", "Hello World"]
    for test in test_strings:
        print(test, "is a pangram:", p.isPangram(test))
```