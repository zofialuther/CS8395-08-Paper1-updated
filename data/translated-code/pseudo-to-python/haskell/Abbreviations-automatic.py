```python
from typing import List
from itertools import islice

def minAbbrevnLength(xs: List[str]) -> int:
    if not xs:
        return 0
    n = len(xs)
    transposedInits = list(map(list, zip(*xs)))
    setOfTransposedInits = set(map(tuple, transposedInits))
    filteredSet = {x for x in setOfTransposedInits if len(x) >= n}
    firstElement = next(iter(filteredSet))
    return len(firstElement)

def main() -> None:
    with open("./weekDayNames.txt", "r") as file:
        s = file.read()
    linesOfS = s.split("\n")
    abbrevnLengths = list(map(minAbbrevnLength, linesOfS))
    firstTenAbbrevnLengths = list(islice(abbrevnLengths, 10))
    tabSeparatedAbbrevnLengths = "\t".join(map(str, firstTenAbbrevnLengths))
    print(tabSeparatedAbbrevnLengths)
```