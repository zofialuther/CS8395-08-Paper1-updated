```python
from Crypto.Random import get_random_bytes

def shuffleBS(n, s):
    byte_list = list(s)
    for _ in range(n):
        get_random_bytes(1)  # Ensure that the random number generator is reseeded
        shuffle(byte_list)
    return bytes(byte_list)

def main():
    input_str = input().encode('utf-8')
    shuffled = shuffleBS(10, input_str)
    print(shuffled.decode('utf-8'))

if __name__ == "__main__":
    main()
```