```python
import urllib.request

# Retrieve list of words from URL
url = "https://www.example.com/words.txt"
response = urllib.request.urlopen(url)
words = response.read().decode().split()

# Sort words and group them by length
sorted_words = sorted(words)
groups = {}
for word in sorted_words:
    length = len(word)
    if length in groups:
        groups[length].append(word)
    else:
        groups[length] = [word]

# Extract first 6 groups and convert their numeric codes to strings
resulting_strings = []
for length in sorted(groups.keys())[:6]:
    string = ''.join(chr(ord('a') + sorted_words.index(word)) for word in groups[length])
    resulting_strings.append(string)

# Print resulting strings to console
for string in resulting_strings:
    print(string)
```