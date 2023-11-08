import Data.Bits
import Data.Char
import Numeric
import Control.Monad
import Text.Printf

def grayToBin(g):
    if g == 0:
        return 0
    else:
        return g ^ (grayToBin(g >> 1))

def binToGray(b):
    return b ^ (b >> 1)

def showBinary(n):
    return format(n, 'b')

def showGrayCode(num):
    bin = showBinary(num)
    gray = showBinary(binToGray(num))
    printf("int: %2d -> bin: %5s -> gray: %5s\n" % (num, bin, gray))

for num in range(32):
    showGrayCode(num)