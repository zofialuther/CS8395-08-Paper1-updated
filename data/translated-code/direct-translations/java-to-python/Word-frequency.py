```python
import re
import urllib.request

def print_word_frequency():
    url = "https://www.gutenberg.org/files/135/135-0.txt"
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        pattern = re.compile(r"(\w+)")
        word_map = {}
        for word in pattern.findall(data):
            word = word.lower()
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1
        # print out top 10
        sorted_word_map = sorted(word_map.items(), key=lambda x: x[1], reverse=True)
        count = 1
        for word, frequency in sorted_word_map[:10]:
            print(f"{word: <20}{frequency: >7}")
            if count == 10:
                break
            count += 1

print_word_frequency()
```