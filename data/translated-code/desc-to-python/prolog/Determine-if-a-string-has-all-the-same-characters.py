```python
import string

# Set double quotes flag to 'chars'
double_quotes_flag = 'chars'

# Define main predicate
def main():
    input_string1 = "example1"
    input_string2 = "example2"
    same_or_different(input_string1, input_string2)

# Define same_or_different predicate
def same_or_different(input_string1, input_string2):
    formatted_string1 = input_string1.lower().strip(string.punctuation)
    formatted_string2 = input_string2.lower().strip(string.punctuation)
    examine(list(formatted_string1))
    examine(list(formatted_string2))

# Define examine predicate
def examine(input_list):
    if len(set(input_list)) == 1:
        print("All the characters are the same.")
    else:
        different_char = next((char, index) for index, char in enumerate(input_list) if char != input_list[0])
        print(f"The character '{different_char[0]}' is different at index {different_char[1]}.")

# Call the main predicate
main()
```