```python
class BraceExpansion:
    @staticmethod
    def expand(s):
        result = []
        BraceExpansion.expandR(s, "", result)
        result.sort()
        return result
    
    @staticmethod
    def expandR(s, current, result):
        if len(s) == 0:
            result.append(current)
            return
        if s[0] == '{':
            i = s.find('}')
            for letter in s[1:i].split(','):
                BraceExpansion.expandR(s[i+1:], current+letter, result)
        else:
            BraceExpansion.expandR(s[1:], current + s[0], result)

if __name__ == "__main__":
    example1 = "a{b,c}d"
    example2 = "e{f,g{h,i}}j"
    print(BraceExpansion.expand(example1))
    print(BraceExpansion.expand(example2))
```