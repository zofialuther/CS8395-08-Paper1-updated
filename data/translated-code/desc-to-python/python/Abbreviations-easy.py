```python
def find_minimal_abbreviation(cmd_table, user_input):
    abbreviations = {}
    for word in user_input:
        abbr_len = sum(1 for c in word if c.isupper())
        abbreviations[word] = word[:abbr_len]
    
    user_input_words = user_input.split()
    full_commands = [cmd_table[abbreviations[word]] for word in user_input_words]
    
    for i in range(len(user_input_words)):
        print(f"{user_input_words[i]} -> {full_commands[i]}")
```