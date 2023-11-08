```python
def squeeze(Str, SqueezeChar, Collapsed):
    char_list = list(Str)
    result_list = []
    for char in char_list:
        if char != SqueezeChar or (char == SqueezeChar and len(result_list) == 0) or char != result_list[-1]:
            result_list.append(char)
    Collapsed = ''.join(result_list)
    return Collapsed
```