```python
class Roman:
    def __init__(self):
        self.roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def decodeSingle(self, s):
        return self.roman_map[s]

    def decode(self, s):
        total = 0
        prev_value = 0
        for char in s:
            curr_value = self.decodeSingle(char)
            if curr_value > prev_value:
                total += curr_value - 2 * prev_value
            else:
                total += curr_value
            prev_value = curr_value
        return total

def main():
    r = Roman()
    print(r.decode("III"))  # Output: 3
    print(r.decode("IX"))   # Output: 9
    print(r.decode("LVIII"))   # Output: 58

if __name__ == "__main__":
    main()
```