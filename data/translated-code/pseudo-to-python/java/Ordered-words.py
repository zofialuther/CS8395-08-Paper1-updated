from java.io import IOException
from java.nio.file import Files, Paths

def main():
    try:
        ordered = readLinesFromFile("unixdict.txt").filter(lambda word: isOrdered(word)).collect()
        maxLength = findMaxLength(ordered)
        printLongestWords(ordered, maxLength)
    except IOException as e:
        handleIOException(e)

def readLinesFromFile(fileName):
    return Files.lines(Paths.get(fileName))

def isOrdered(aWord):
    return "".join(sorted(aWord)) == aWord

def findMaxLength(words):
    return max(len(word) for word in words)

def printLongestWords(words, maxLength):
    for word in words:
        if len(word) == maxLength:
            print(word)

def handleIOException(exception):
    # Handle the IOException
    pass