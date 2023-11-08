```python
def mid3digits(num):
    if type(num) != int:
        return "Input must be an integer"
    if abs(num) < 100:
        return "Input must be at least 3 digits long"
    num_str = str(abs(num))
    mid_index = len(num_str) // 2
    return int(num_str[mid_index - 1:mid_index + 2])

def test_mid3digits():
    test_cases = [123456, -987654, 12, "abc"]
    for num in test_cases:
        result = mid3digits(num)
        print(f"mid3digits({num}) = {result}")

test_mid3digits()
```