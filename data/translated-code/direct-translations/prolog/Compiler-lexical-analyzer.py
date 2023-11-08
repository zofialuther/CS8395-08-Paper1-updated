```python
from collections import namedtuple

# Token namedtuple for storing token information
Token = namedtuple('Token', ['type', 'line', 'pos', 'value'])

# Load file and convert to list of chars
def load_file(file, input):
    with open(file, 'r') as f:
        content = f.read()
        input.extend(content)

# Test file function
def test_file(file):
    input = []
    load_file(file, input)
    tester(input)

# Tester function
def tester(s):
    tokens = tokenize(s)
    for token in tokens:
        print_tok(token)

# Print token function
def print_tok(token):
    if token.type == 'string':
        print(f'{token.line}\t{token.pos}\tstring\t\t"{token.value}"')
    elif token.type == 'identifier':
        print(f'{token.line}\t{token.pos}\tidentifier\t{token.value}')
    elif token.type == 'integer':
        print(f'{token.line}\t{token.pos}\tinteger\t\t{token.value}')
    else:
        print(f'{token.line}\t{token.pos}\t{token.type}')

# Tokenize function
def tokenize(chars):
    # Implement the tokenize function here
    pass
```