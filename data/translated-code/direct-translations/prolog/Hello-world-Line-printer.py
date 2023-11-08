```python
import os

def main():
    printer = os.open("/dev/lp0", os.O_WRONLY)
    os.write(printer, b"Hello, world!\n")
    os.close(printer)

if __name__ == "__main__":
    main()
```