```python
import Data.ByteString
import Data.Bits

def main():
    content = [105, 35, 35, 10, 50, 53, 54, 32, 50, 53, 54, 10, 50, 53, 54, 10]
    with open("out.pgm", "wb") as file:
        file.write(bytearray(content))

if __name__ == "__main__":
    main()
```