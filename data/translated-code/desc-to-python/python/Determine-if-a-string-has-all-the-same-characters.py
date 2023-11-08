```python
def firstDifferingCharLR(input_string):
    result = {}
    first_char = input_string[0]
    for char in input_string:
        if char != first_char:
            result['First differing character'] = char
            result['Position'] = input_string.index(char)
            return result
    return "No character changes were seen"

def main():
    test_strings = ["aaaaaa", "abaaaa", "abcde", "1111111", "2222222", "a", ""]
    for string in test_strings:
        print(firstDifferingCharLR(string))

main()
```