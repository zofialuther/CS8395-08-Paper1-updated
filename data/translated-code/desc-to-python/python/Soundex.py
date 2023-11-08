```python
import fuzzy

soundex = fuzzy.Soundex(4)
words = ["soundex", "example", "ciondecks", "ekzampul"]
soundex_codes = [soundex(sound) for sound in words]
print(soundex_codes)
```