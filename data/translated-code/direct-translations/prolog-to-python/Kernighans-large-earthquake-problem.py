```python
import re

def process_line(Line):
    _, _, Magnitude_string = re.split(r"\s\t", Line)
    Magnitude = float(Magnitude_string)
    if Magnitude > 6:
        print(Line)

def process_stream(Stream):
    String = Stream.readline()
    while String != '':
        process_line(String)
        String = Stream.readline()

def process_file(File):
    with open(File, 'r') as Stream:
        process_stream(Stream)

def main(args):
    if len(args) > 1:
        process_file(args[1])
    else:
        print('File argument is missing', file=sys.stderr)

if __name__ == "__main__":
    import sys
    main(sys.argv)
```