import java.io.IOException
from java.nio.file import Files, Path
from java.util import List

def isOrdered(aWord):
    return ''.join(sorted(aWord)) == aWord

def main(aArgs):
    ordered = Files.lines(Path.of("unixdict.txt")).filter(lambda word: isOrdered(word)).toList()

    maxLength = max(map(len, ordered))
    for word in ordered:
        if len(word) == maxLength:
            print(word)

if __name__ == "__main__":
    try:
        main([])
    except IOException as e:
        print(e)