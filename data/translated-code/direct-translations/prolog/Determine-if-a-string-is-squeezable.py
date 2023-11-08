```python
def squeeze_(chars, squeeze_char, result):
    if len(chars) == 0:
        result = []
    elif len(chars) == 1:
        result = chars
    elif chars[0] == squeeze_char and chars[0] == chars[1]:
        result = squeeze_(chars[1:], squeeze_char, result)
    elif chars[0] == chars[1]:
        result = [chars[0]] + squeeze_(chars[1:], squeeze_char, result)
    elif chars[0] != chars[1]:
        result = [chars[0]] + squeeze_(chars[1:], squeeze_char, result)
    return result

def squeeze(string, squeeze_char, collapsed):
    chars = list(string)
    result = squeeze_(chars, squeeze_char, [])
    collapsed = ''.join(result)
    return collapsed
```