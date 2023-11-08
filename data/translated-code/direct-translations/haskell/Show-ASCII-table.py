from Data.Char import chr
from Data.List import transpose
from Data.List.Split import chunksOf
from Text.Printf import printf

# ASCII TABLE
def asciiEntry(n):
    k = asciiName(n)
    if not k:
        return k
    else:
        return f"{n:3d} : {k}"

def asciiName(n):
    if n < 32 or n > 127:
        return ""
    elif n == 32:
        return "Spc"
    elif n == 127:
        return "Del"
    else:
        return chr(n)

def main():
    asciiTable = "\n".join(map(lambda x: "".join(f"{x:12}", asciiEntry(x)), transpose(chunksOf(16, map(asciiEntry, range(32, 128))))))
    print(asciiTable)

main()