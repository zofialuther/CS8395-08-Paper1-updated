```python
def shuffleBS(n, s):
    s = yieldMany(*s)
    s = shuffleC(n)
    s = mapC(charUtf8)
    s = builderToByteString(s)
    s = foldC(s)

def main():
    stdin = sourceHandle
    mapMC = shuffleBS(10)
    stdout = sinkHandle
```