def quibble(ws):
    return "{" + quibbles(ws) + "}"

def quibbles(ws):
    if len(ws) == 0:
        return ""
    elif len(ws) == 1:
        return ws[0]
    elif len(ws) == 2:
        return ws[0] + " and " + ws[1]
    else:
        return ws[0] + ", " + quibbles(ws[1:])

def words(s):
    return s.split()

def main():
    list = [[], ["ABC"], ["ABC", "DEF"], ["ABC", "DEF", "G", "H"]] + list(map(words, ["One two three four", "Me myself I", "Jack Jill", "Loner"]))
    list(map(print, list(map(quibble, list)))

main()