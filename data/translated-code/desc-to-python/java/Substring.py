```python
class SubstringExtractor:
    def extract_substring(self, s, start, length):
        return s[start:start+length]

    def extract_substring_from_start(self, s, start):
        return s[start:]

    def extract_substring_to_second_last(self, s):
        return s[:-1]

    def extract_substring_from_character(self, s, char, length):
        index = s.find(char)
        return s[index:index+length]

    def extract_substring_from_substring(self, s, sub, length):
        index = s.find(sub)
        return s[index:index+length]
```