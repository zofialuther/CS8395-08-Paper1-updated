```python
from typing import List

def strip_leading(INPUTz: str) -> str:
    OUTPUTz = ""
    strip_leading_nonspacious(OUTPUTz, INPUTz)
    return OUTPUTz

def strip_trailing(INPUTz: str) -> str:
    OUTPUTz = ""
    strip_trailing_nonspacious(OUTPUTz, INPUTz)
    return OUTPUTz

def strip_leading_and_trailing(INPUTz: str) -> str:
    OUTPUTz = ""
    strip_leading_spacious() + strip_trailing_nonspacious(OUTPUTz, INPUTz) + strip_trailing_spacious()
    return OUTPUTz

def strip_leading_spacious() -> List[str]:
    # Implementation for strip_leading_spacious
    pass

def strip_leading_nonspacious(OUTPUTz: str, INPUTz: str) -> str:
    # Implementation for strip_leading_nonspacious
    pass

def strip_trailing_nonspacious(OUTPUTz: str, INPUTz: str) -> str:
    # Implementation for strip_trailing_nonspacious
    pass

def strip_trailing_spacious() -> List[str]:
    # Implementation for strip_trailing_spacious
    pass
```