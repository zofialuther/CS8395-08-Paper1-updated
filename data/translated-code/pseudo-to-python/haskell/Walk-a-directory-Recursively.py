```python
import System.Environment
import System.Directory
import System.FilePath.Find

def search(pat):
    return find(always, (fileName ~~? pat))

def main():
    pat = getArgs()[0]
    dir = getCurrentDirectory()
    files = search(pat, dir)
    mapM_(putStrLn, files)
```