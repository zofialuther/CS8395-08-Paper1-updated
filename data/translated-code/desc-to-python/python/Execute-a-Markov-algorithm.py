```python
import re

def extractreplacements(grammar):
    replacements = re.findall(r'(\w+)\s*->\s*(\w+)', grammar)
    return dict(replacements)

def replace(text, replacements):
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

# Example grammars and texts
grammar1 = "A -> B\nB -> C"
text1 = "A B C"

grammar2 = "apple -> banana\nbanana -> cherry"
text2 = "apple banana cherry"

# Assertions to test functionality
assert extractreplacements(grammar1) == {'A': 'B', 'B': 'C'}
assert extractreplacements(grammar2) == {'apple': 'banana', 'banana': 'cherry'}
assert replace(text1, extractreplacements(grammar1)) == "B C C"
assert replace(text2, extractreplacements(grammar2)) == "banana cherry cherry"
```