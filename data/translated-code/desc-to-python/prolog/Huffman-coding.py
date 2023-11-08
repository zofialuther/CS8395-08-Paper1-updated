```python
# Function to build Huffman tree
def build_huffman_tree(data):
    # implementation details here

# Function to encode characters
def encode_characters(data):
    # implementation details here

# Function to print Huffman codes
def print_huffman_codes(symbols, weights, codes):
    # implementation details here

# Main code
string = "example_string"
characters = list(string)
packed_list = sorted(characters)
huffman_tree = build_huffman_tree(packed_list)
huffman_codes = encode_characters(packed_list)
print_huffman_codes(packed_list, huffman_tree, huffman_codes)
```