from java.io import IOException
from java.nio.charset import StandardCharsets
from java.nio.file import Files, Paths
from java.util import ArrayList, List
from org.apache.commons.lang3 import StringUtils

class ColumnAligner:
    def __init__(self, s):
        self.words = []
        self.columns = 0
        self.columnWidths = []
        lines = s.split("\n")
        for line in lines:
            self.processInputLine(line)

    def processInputLine(self, line):
        lineWords = line.split("\\$")
        self.words.append(lineWords)
        self.columns = max(self.columns, len(lineWords))
        for i in range(len(lineWords)):
            word = lineWords[i]
            if i >= len(self.columnWidths):
                self.columnWidths.append(len(word))
            else:
                self.columnWidths[i] = max(self.columnWidths[i], len(word))

    def alignLeft(self):
        return self.align(lambda s, length: StringUtils.rightPad(s, length))

    def alignRight(self):
        return self.align(lambda s, length: StringUtils.leftPad(s, length))

    def alignCenter(self):
        return self.align(lambda s, length: StringUtils.center(s, length))

    def align(self, a):
        result = ""
        for lineWords in self.words:
            for i in range(len(lineWords)):
                word = lineWords[i]
                if i == 0:
                    result += "|"
                result += a(word, self.columnWidths[i]) + "|"
            result += "\n"
        return result

    def main(args):
        if len(args) < 1:
            print("Usage: ColumnAligner file [left|right|center]")
            return
        filePath = args[0]
        alignment = "left"
        if len(args) >= 2:
            alignment = args[1]
        ca = ColumnAligner(Files.readAllLines(Paths.get(filePath), StandardCharsets.UTF_8))
        if alignment == "left":
            print(ca.alignLeft())
        elif alignment == "right":
            print(ca.alignRight())
        elif alignment == "center":
            print(ca.alignCenter())
        else:
            print("Error! Unknown alignment: '" + alignment + "'")