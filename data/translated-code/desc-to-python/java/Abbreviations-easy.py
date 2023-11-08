```python
# Python code
def count_capital_letters(word):
    count = 0
    for letter in word:
        if letter.isupper():
            count += 1
    return count

abbreviations = {
    "Hello": 5,
    "Goodbye": 7,
    "Yes": 3,
    "No": 2
}

user_input = input("Enter a command: ")
words = user_input.split()

for word in words:
    if word in abbreviations:
        print(word.upper())
    else:
        print("Error: No matching abbreviation found")
```