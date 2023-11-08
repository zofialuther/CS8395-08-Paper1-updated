```python
# Python code to perform Gray code encoding and decoding

def make_num(input):
    return int(input)

def write_record(num, gray_code, decoded_num):
    print(f"{num}: {gray_code} - {decoded_num}")

def gray_code(num):
    return num ^ (num >> 1)

def decode_gray_code(gray_code):
    num = 0
    while gray_code:
        num ^= gray_code
        gray_code >>= 1
    return num

def go():
    for num in range(32):
        gray_code = gray_code(num)
        decoded_num = decode_gray_code(gray_code)
        write_record(num, bin(gray_code)[2:].zfill(5), decoded_num)
        
go()
exit(1)
```