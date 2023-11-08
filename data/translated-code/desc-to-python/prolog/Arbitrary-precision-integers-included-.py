```python
def calculate_length_of_codes():
    num = 5 ** (4 ** (3 ** 2))
    code_list = list(str(num))
    code_list.insert(0, "ABC")
    code_list.append("XYZ")
    return len(code_list)
```