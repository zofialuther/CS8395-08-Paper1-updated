def graphemeReverse(text):
    boundary = getCharacterInstance()
    boundary.setText(text)
    reversed = ""
    end = boundary.last()
    start = boundary.previous()
    while start != DONE:
        reversed += text.substring(start, end)
        end = start
        start = boundary.previous()
    return reversed

def main(args):
    a = "as⃝df̅"
    print(graphemeReverse(a))

main()