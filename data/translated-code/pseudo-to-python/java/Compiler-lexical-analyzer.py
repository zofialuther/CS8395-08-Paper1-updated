class Lexer:
    def __init__(self, source):
        self.line = 1
        self.pos = 0
        self.position = 0
        self.s = source
        self.chr = self.s[0]
        self.keywords = {"if": "Keyword_if", "else": "Keyword_else", "print": "Keyword_print", "putc": "Keyword_putc", "while": "Keyword_while"}

    class Token:
        def __init__(self, token_type, value, line, pos):
            self.token_type = token_type
            self.value = value
            self.line = line
            self.pos = pos

        def __str__(self):
            result = "{:5d} {:5d} {:15s}".format(self.line, self.pos, self.token_type)
            if self.token_type == "Integer":
                result += "  {:4s}".format(self.value)
            elif self.token_type == "Identifier":
                result += " {}".format(self.value)
            elif self.token_type == "String":
                result += ' "{}"'.format(self.value)
            return result

    def error(line, pos, msg):
        if line > 0 and pos > 0:
            print("{} in line {}, pos {}".format(msg, line, pos))
        else:
            print(msg)
        exit(1)