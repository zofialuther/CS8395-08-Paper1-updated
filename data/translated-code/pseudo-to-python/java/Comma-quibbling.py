def quibble(words):
    qText = "{"
    for wIndex in range(len(words)):
        qText += words[wIndex]
        if wIndex == len(words) - 1:
            qText += ""
        elif wIndex == len(words) - 2:
            qText += " and "
        else:
            qText += ", "
    qText += "}"
    return qText

def main(args):
    print(quibble({}))
    print(quibble({"ABC"}))
    print(quibble({"ABC", "DEF"}))
    print(quibble({"ABC", "DEF", "G"}))
    print(quibble({"ABC", "DEF", "G", "H"}))