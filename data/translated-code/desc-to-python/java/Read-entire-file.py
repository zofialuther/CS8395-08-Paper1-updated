```python
import os

class ReadAll:
    @staticmethod
    def readAllLines(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    
    @staticmethod
    def readAllBytes(filename):
        with open(filename, 'rb') as file:
            bytes = file.read()
        return bytes
```