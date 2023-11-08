```python
import Data.Digest.Pure.SHA as SHA
import qualified Data.ByteString.Lazy as B

def convertString(s):
    return B.pack(map(ord, s))

def convertToSHA1(s):
    return showDigest(sha1(convertString(s)))

def main():
    print("Rosetta Code SHA1-codiert: ", end="")
    print(convertToSHA1("Rosetta Code"))

main()
```