```python
class RepStrings:
    def repString(self, s):
        n = len(s)
        res = ""
        for i in range(n):
            for j in range(i+1, n):
                if s[i:i+(j-i)] in s[j:]:
                    if len(s[i:i+(j-i)]) > len(res):
                        res = s[i:i+(j-i)]
        if res == "":
            print("Not a rep-string")
        else:
            print("Original string:", s)
            print("Longest repeated substring:", res)

if __name__ == "__main__":
    rs = RepStrings()
    strings = ["110110", "1010101", "111000111"]
    for s in strings:
        rs.repString(s)
```