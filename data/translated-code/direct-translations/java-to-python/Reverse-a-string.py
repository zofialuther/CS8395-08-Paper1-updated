import java.text.BreakIterator

def graphemeReverse(text):
    boundary = BreakIterator.getCharacterInstance()
    boundary.setText(text)
    reversed = StringBuilder()
    end = boundary.last()
    start = boundary.previous()
    while start != BreakIterator.DONE:
        reversed.append(text[start:end])
        end = start
        start = boundary.previous()
    return reversed

def main():
    a = "as⃝df̅"
    print(graphemeReverse(a)) # f̅ds⃝a

if __name__ == "__main__":
    main()