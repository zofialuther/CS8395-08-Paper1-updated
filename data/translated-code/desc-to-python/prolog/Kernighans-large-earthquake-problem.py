```python
def main(file):
    if file:
        with open(file, 'r') as f:
            for line in f:
                parts = line.split(',')
                if float(parts[3]) > 6:
                    print(line)
    else:
        print("File argument is missing")

main("input_file.txt")
```