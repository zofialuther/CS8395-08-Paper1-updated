```python
from itertools import count

def infixes(sub, s):
    return [i for i, ss in zip(count(), (s[j:] for j in range(len(s)))) if ss.startswith(sub)]

result = infixes("ab", "abcdefabqqab")
print(result)
```