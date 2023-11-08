```python
import Data.Text as T
import Data.Text.IO as O

def fromMforN(n, m, s):
    return T.take(m, T.drop(n, s))

def fromNtoEnd(n, s):
    return T.drop(n, s)

def allButLast(s):
    return T.init(s)

def fromCharForN(m, needle, haystack):
    return T.take(m, T.breakOn(needle, haystack)[1])

def fromStringForN(m, needle, haystack):
    return fromCharForN(m, needle, haystack)

def main():
    O.putStrLn(fromMforN(9, 10, "天地不仁仁者人也🐒话说天下大势分久必合🍑合久必分🔥"))
    O.putStrLn(fromNtoEnd(20, "天地不仁仁者人也🐒话说天下大势分久必合🍑合久必分🔥"))
    O.putStrLn(allButLast("天地不仁仁者人也🐒话说天下大势分久必合🍑合久必分🔥"))
    O.putStrLn(fromCharForN(6, "话", "天地不仁仁者人也🐒话说天下大势分久必合🍑合久必分🔥"))
    O.putStrLn(fromStringForN(6, "大势", "天地不仁仁者人也🐒话说天下大势分久必合🍑合久必分🔥"))

if __name__ == "__main__":
    main()
```