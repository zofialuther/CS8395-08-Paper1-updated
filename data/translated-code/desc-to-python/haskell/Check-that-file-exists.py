```python
import os

def check(func, filepath):
    if func(filepath):
        print(f"{filepath} exists")
    else:
        print(f"{filepath} does not exist")

def main():
    check(os.path.exists, "file1.txt")
    check(os.path.exists, "file2.txt")
    check(os.path.exists, "file3.txt")

if __name__ == "__main__":
    main()
```