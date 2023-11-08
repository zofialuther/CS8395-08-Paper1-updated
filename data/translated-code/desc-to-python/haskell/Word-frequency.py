```python
import sys
from collections import Counter

n = int(sys.argv[1])
text = sys.stdin.read().lower().split()
word_freq = Counter(text)
top_n_words = word_freq.most_common(n)

for word, freq in top_n_words:
    print(word, freq)
```