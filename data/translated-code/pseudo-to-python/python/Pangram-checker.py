```python
import string
import sys

if sys.version[0] < '3':
    input = raw_input

def ispangram(sentence, alphabet):
    alphaset = set(alphabet)
    sentence_set = set(sentence.lower())
    return alphaset.issubset(sentence_set)

print(ispangram(input("Enter a sentence: "), string.ascii_lowercase))
```