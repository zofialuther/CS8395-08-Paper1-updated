```python
import sys

def strip_line_comments(args):
    if len(args) < 1:
        print("Usage: python strip_line_comments.py StringToProcess")
    else:
        inputFile = args[0]
        input = ""
        try:
            with open(inputFile, 'r') as reader:
                for line in reader:
                    print(line.split("#")[0].split(";")[0])
        except Exception as e:
            print(e)

if __name__ == "__main__":
    strip_line_comments(sys.argv[1:])
```