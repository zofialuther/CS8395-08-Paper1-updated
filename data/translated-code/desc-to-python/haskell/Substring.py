```python
def extract_substring(text, start, end):
    return text[start:end]

def extract_from_index(text, start):
    return text[start:]

def remove_last_character(text):
    return text[:-1]

def extract_substring_by_character(text, char):
    return text.split(char)

def extract_substring_by_string(text, substring):
    return text.split(substring)

# Test section
sample_text = "This is a sample text"
print(extract_substring(sample_text, 2, 8))
print(extract_from_index(sample_text, 5))
print(remove_last_character(sample_text))
print(extract_substring_by_character(sample_text, ' '))
print(extract_substring_by_string(sample_text, 'sample'))
```