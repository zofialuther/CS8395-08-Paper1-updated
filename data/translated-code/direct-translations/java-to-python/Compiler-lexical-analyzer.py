```python
class Lexer:
    def __init__(self, source):
        self.line = 1
        self.pos = 0
        self.position = 0
        self.s = source
        self.chr = self.s[0]
        self.keywords = {
            "if": TokenType.Keyword_if,
            "else": TokenType.Keyword_else,
            "print": TokenType.Keyword_print,
            "putc": TokenType.Keyword_putc,
            "while": TokenType.Keyword_while
        }

    class Token:
        def __init__(self, token, value, line, pos):
            self.tokentype = token
            self.value = value
            self.line = line
            self.pos = pos

        def __str__(self):
            result = f"{self.line:5}  {self.pos:5} {self.tokentype:15}"
            if self.tokentype == TokenType.Integer:
                result += f"  {self.value:4}"
            elif self.tokentype == TokenType.Identifier:
                result += f" {self.value}"
            elif self.tokentype == TokenType.String:
                result += f' "{self.value}"'
            return result

    class TokenType:
        End_of_input, Op_multiply,  Op_divide, Op_mod, Op_add, Op_subtract, \
        Op_negate, Op_not, Op_less, Op_lessequal, Op_greater, Op_greaterequal, \
        Op_equal, Op_notequal, Op_assign, Op_and, Op_or, Keyword_if, \
        Keyword_else, Keyword_while, Keyword_print, Keyword_putc, LeftParen, RightParen, \
        LeftBrace, RightBrace, Semicolon, Comma, Identifier, Integer, String = range(31)

    def error(self, line, pos, msg):
        if line > 0 and pos > 0:
            print(f"{msg} in line {line}, pos {pos}")
        else:
            print(msg)
        exit(1)

    def follow(self, expect, ifyes, ifno, line, pos):
        if self.get_next_char() == expect:
            self.get_next_char()
            return self.Token(ifyes, "", line, pos)
        if ifno == self.TokenType.End_of_input:
            self.error(line, pos, f"follow: unrecognized character: ({ord(self.chr)}) '{self.chr}'")
        return self.Token(ifno, "", line, pos)

    def char_lit(self, line, pos):
        c = self.get_next_char()  # skip opening quote
        n = ord(c)
        if c == '\'':
            self.error(line, pos, "empty character constant")
        elif c == '\\':
            c = self.get_next_char()
            if c == 'n':
                n = 10
            elif c == '\\':
                n = ord('\\')
            else:
                self.error(line, pos, f"unknown escape sequence \\{c}")
        if self.get_next_char() != '\'':
            self.error(line, pos, "multi-character constant")
        self.get_next_char()
        return self.Token(self.TokenType.Integer, str(n), line, pos)

    def string_lit(self, start, line, pos):
        result = ""
        while self.get_next_char() != start:
            if self.chr == '\u0000':
                self.error(line, pos, "EOF while scanning string literal")
            if self.chr == '\n':
                self.error(line, pos, "EOL while scanning string literal")
            result += self.chr
        self.get_next_char()
        return self.Token(self.TokenType.String, result, line, pos)

    def div_or_comment(self, line, pos):
        if self.get_next_char() != '*':
            return self.Token(self.TokenType.Op_divide, "", line, pos)
        self.get_next_char()
        while True:
            if self.chr == '\u0000':
                self.error(line, pos, "EOF in comment")
            elif self.chr == '*':
                if self.get_next_char() == '/':
                    self.get_next_char()
                    return self.get_token()
            else:
                self.get_next_char()

    def identifier_or_integer(self, line, pos):
        is_number = True
        text = ""
        while self.chr.isalpha() or self.chr.isdigit() or self.chr == '_':
            text += self.chr
            if not self.chr.isdigit():
                is_number = False
            self.get_next_char()
        if text == "":
            self.error(line, pos, f"identifer_or_integer unrecognized character: ({ord(self.chr)}) {self.chr}")
        if text[0].isdigit():
            if not is_number:
                self.error(line, pos, f"invalid number: {text}")
            return self.Token(self.TokenType.Integer, text, line, pos)
        if text in self.keywords:
            return self.Token(self.keywords[text], "", line, pos)
        return self.Token(self.TokenType.Identifier, text, line, pos)

    def get_token(self):
        while self.chr.isspace():
            self.get_next_char()
        line, pos = self.line, self.pos
        if self.chr == '\u0000':
            return self.Token(self.TokenType.End_of_input, "", self.line, self.pos)
        elif self.chr == '/':
            return self.div_or_comment(line, pos)
        elif self.chr == '\'':
            return self.char_lit(line, pos)
        elif self.chr == '<':
            return self.follow('=', self.TokenType.Op_lessequal, self.TokenType.Op_less, line, pos)
        # ... (other cases)

    def get_next_char(self):
        self.pos += 1
        self.position += 1
        if self.position >= len(self.s):
            self.chr = '\u0000'
            return self.chr
        self.chr = self.s[self.position]
        if self.chr == '\n':
            self.line += 1
            self.pos = 0
        return self.chr

    def print_tokens(self):
        t = self.get_token()
        while t.tokentype != self.TokenType.End_of_input:
            print(t)
            t = self.get_token()
        print(t)

    if __name__ == "__main__":
        import sys
        if len(sys.argv) > 0:
            try:
                with open(sys.argv[0], 'r') as f:
                    source = " "
                    for line in f:
                        source += line + "\n"
                    l = Lexer(source)
                    l.print_tokens()
            except FileNotFoundError as e:
                error(-1, -1, "Exception: " + e.strerror)
        else:
            error(-1, -1, "No args")
```