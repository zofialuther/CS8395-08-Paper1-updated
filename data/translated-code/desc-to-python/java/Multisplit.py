```python
import re

class MultiSplit:
    def regex_split(self, string):
        result = re.split(r'==|!=|=', string)
        print(result)
    
    def manual_split(self, string):
        separators = ['==', '!=', '=']
        result = self.multiSplit(string, separators)
        print(result)
    
    def multiSplit(self, string, separators):
        result = []
        start = 0
        for i in range(len(string)):
            if string[i:i+2] in separators:
                result.append(string[start:i])
                start = i + 2
        result.append(string[start:])
        return result

m = MultiSplit()
m.regex_split("a!===b=!=c")
m.manual_split("a!===b=!=c")
```