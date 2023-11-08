```python
import string

stripchars = lambda s, exclude: ''.join(filter(lambda c: c not in exclude, s))
```