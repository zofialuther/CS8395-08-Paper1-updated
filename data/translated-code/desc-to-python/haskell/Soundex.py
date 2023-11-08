```python
from Text.PhoneticCode import Soundex

def main():
    words = ["Soundex", "Example", "Sownteks", "Ekzampul"]
    soundex_codes = Soundex.soundexSimple <*> words
    mapM_(print, soundex_codes)

main()
```