```python
def mid3(num):
    num = abs(num)
    num_str = str(num)
    
    if len(num_str) < 3 or len(num_str) % 2 == 0:
        return "Error: Number is too small or has an even number of digits"
    else:
        mid_index = len(num_str) // 2
        return num_str[mid_index-1:mid_index+2]

def justifyRight(s, length, char):
    return (char * (length - len(s))) + s

test_numbers = [12345, 67890, 123456789, -987654321, 100, 999]
for num in test_numbers:
    result = mid3(num)
    print(f"Number: {num}, Result: {result}")

```