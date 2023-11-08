```python
def load_file(file_name):
    with open(file_name, 'r') as file:
        return list(file.read())

def tester(input_characters):
    tokens = tokenize(input_characters)
    print(tokens)

def tokenize(input_characters):
    # code for tokenizing input characters using DCG
    pass

# helper DCGs and token type definitions
# handling exceptions

# example usage
file_name = "input.txt"
input_characters = load_file(file_name)
tester(input_characters)
```