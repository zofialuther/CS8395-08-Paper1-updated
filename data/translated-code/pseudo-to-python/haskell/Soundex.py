```python
from Text.PhoneticCode import Soundex

def main() -> None:
    mapM_(print, [(Soundex.soundexSimple <$> ["Soundex", "Example", "Sownteks", "Ekzampul"])])
```