```python
# No need to specify ScopedTypeVariables in Python

import Bitmap
import Data.Char
import System.IO
import Control.Monad
import Control.Monad.ST
import Data.Array.ST

def readNetpbm(c, path):
    def die():
        raise Exception("readNetpbm: bad format")

    with open(path, 'r') as file:
        ppm = file.read()
        s, rest = ppm[:2], ppm[2:]
        if s != magicNumber:
            die()
        
        def getNum(ppm):
            s, rest = '', skipBlanks(ppm)
            while rest[0].isdigit():
                s += rest[0]
                rest = rest[1:]
            if not s:
                die()
            return int(s), rest
        
        width, rest = getNum(rest)
        height, rest = getNum(rest)
        if getMaxval:
            _, c, rest = getNum(rest)
        if not c.isspace():
            die()
        
        i = listImage(width, height, fromNetpbm(list(map(ord, rest))))
        return i

def skipBlanks(ppm):
    ppm = ppm.lstrip()
    while ppm[0] == '#':
        ppm = ppm[1:]
        ppm = ppm[ppm.index('\n') + 1:].lstrip()
    return ppm

magicNumber = netpbmMagicNumber(nil)
getMaxval = bool(netpbmMaxval(nil))

def writeNetpbm(c, path, i):
    with open(path, 'w') as file:
        width, height = dimensions(i)
        file.write(magicNumber + '\n')
        file.write(str(width) + ' ' + str(height) + '\n')
        if maxval:
            file.write(maxval + '\n')
        file.write(toNetpbm(getPixels(i)))

magicNumber = netpbmMagicNumber(nil)
maxval = netpbmMaxval(nil)
```