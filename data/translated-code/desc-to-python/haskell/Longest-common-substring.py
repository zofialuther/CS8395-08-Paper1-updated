```python
from Data.List import intersect
from Data.Ord import maximumBy, comparing

def longestCommon(list1, list2):
    common_elements = intersect(list1, list2)
    return maximumBy(comparing(len), common_elements)

def main():
    str1 = "abcdefg"
    str2 = "xyzdef"
    result = longestCommon(str1, str2)
    print(result)

main()
```