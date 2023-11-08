```python
def word_wrap(input_string, line_length):
    words = input_string.split()
    return wrap(words, line_length, line_length)

def wrap(words, line_length, space_left):
    result = []
    current_line = []
    while words:
        word = words[0]
        if len(word) <= space_left:
            current_line.append(word)
            space_left -= len(word) + 1
            words = words[1:]
        else:
            result.append(' '.join(current_line))
            current_line = []
            space_left = line_length
    result.append(' '.join(current_line))
    return result

def test_word_wrap():
    input_string = "This is a sample text for word wrapping functionality in Prolog"
    line_length = 10
    print(word_wrap(input_string, line_length))

def main():
    test_word_wrap()

if __name__ == "__main__":
    main()
```