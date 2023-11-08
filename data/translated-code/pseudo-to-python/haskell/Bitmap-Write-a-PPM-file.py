from typing import TypeVar
from typing import IO
from Data.Array.ST import STArray
from Control.Monad import ST
from Control.Monad import Monad
from System.IO import FilePath

c = TypeVar('c')

nil = None

def readNetpbm(FilePath: FilePath) -> IO:
    def die():
        return fail("readNetpbm: bad format")

    # read file at path and store in ppm
    ppm = ...

    # split ppm into (s, rest)
    s, rest = ...

    # check if s is equal to magicNumber, if not then execute die
    if s != magicNumber:
        die()

    def getNum(String: str) -> IO:
        # split input string and get the number and the rest of the string
        # if number is empty, execute die
        # return the number and the rest of the string
        return ...

    # call getNum twice with rest, and store the width and height
    width, rest = getNum(rest)
    height, rest = getNum(rest)

    if getMaxval:
        _, c, rest = getNum(rest)

    # if c is not a space, execute die
    if c != " ":
        die()

    # create a new image i with dimensions width and height using listImage and fromNetpbm
    i = ...

    return i


def skipBlanks(String: str) -> str:
    # function that removes whitespace and comments from a string
    return ...


magicNumber = netpbmMagicNumber(nil)
getMaxval = not null(netpbmMaxval(nil))

def writeNetpbm(FilePath: FilePath, Image: RealWorld, c) -> IO:
    # open file at path in write mode
    file = open(FilePath, "w")

    # get dimensions of the image and store in (width, height)
    width, height = ...

    def w(String: str):
        # function that writes a string to the file
        file.write(String)

    # write magicNumber to the file
    w(magicNumber)

    # write width and height to the file
    w(width)
    w(height)

    if maxval is not None:
        # write maxval to the file
        w(maxval)

    # get the pixels of the image and convert to Netpbm format, then write to the file
    pixels = ...
    netpbm_format = convertToNetpbmFormat(pixels)
    w(netpbm_format)