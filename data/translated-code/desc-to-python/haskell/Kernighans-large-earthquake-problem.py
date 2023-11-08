import Data.ByteString.Lazy.Char8 as B

with open("data.txt", "rb") as file:
    content = file.read()

lines = B.lines(content)

for line in lines:
    words = B.words(line)
    last_word = B.last(words)
    try:
        if float(last_word) > 6:
            print(line.decode("utf-8"))
    except ValueError:
        pass