```python
def encode(text):
    """
    Compresses consecutive characters in a string.

    >>> encode('aaabbbbcc')
    '3a4b2c'
    >>> encode('hello')
    '1h1e2l1o'
    """
    result = ''
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            result += str(count) + text[i-1]
            count = 1
    result += str(count) + text[-1]
    return result


def decode(text):
    """
    Expands the compressed text back to its original form.

    >>> decode('3a4b2c')
    'aaabbbbcc'
    >>> decode('1h1e2l1o')
    'hello'
    """
    result = ''
    count = ''
    for char in text:
        if char.isdigit():
            count += char
        else:
            result += int(count) * char
            count = ''
    return result


# Ensure that decode(encode(text)) == text
assert decode(encode('aaabbbbcc')) == 'aaabbbbcc'
```