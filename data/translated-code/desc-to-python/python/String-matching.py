```python
# demonstrate usage of string methods
string1 = "abcd"
print(string1.startswith("ab"))  # True
print(string1.endswith("zn"))     # False
string2 = "abab"
print(string2.find("bb"))         # -1
print(string2.find("ab"))         # 0
print(string2.find("ab", 1))      # 2
```