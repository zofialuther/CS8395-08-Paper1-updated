def makeToken(lexer):
    t, l, c = get()
    val = lexer
    
    if val == Skip:
        return nextToken
    elif val == LexError msg:
        _, l_, c_ = get()
        code = takeSubstring(t, c_ - c + 1)
        str = formatString(msg, " ", l_, c_, code)

        ch = peek()
        if ch != '\0':
            advance(1)
        return Token(LexError str, l, c)
    else:
        return Token(val, l, c)

def simpleToken(lexeme, name):
    return lit(lexeme) $> SymbolVal(name)

def makeTokenizers(tokens):
    return asum(map(uncurry simpleToken, tokens))

def isIdStart(ch):
    return isAsciiLower(ch) or isAsciiUpper(ch) or ch == '_'

def isIdEnd(ch):
    return isIdStart(ch) or isDigit(ch)

def identifier():
    lexeme = T.cons(one(isIdStart), many(isIdEnd))
    return TextVal("Identifier", lexeme)

def integer():
    lexeme = some(isDigit)
    next_ch = peek()

    if isIdStart(next_ch):
        return LexError("Invalid number. Starts like a number, but ends in non-numeric characters.")
    else:
        num = parseInt(lexeme)
        return IntVal(num)

def character():
    lit("'")
    str = lookahead(3)

    switch str:
        case (ch : '\'' : _):
            advance(2) $> IntVal(ord(ch))
        case "\n'":
            advance(3) $> IntVal(10)
        case "\\\\'":
            advance(3) $> IntVal(92)
        case ('\\' : ch : "\'"):
            advance(2) $> LexError(formatString("Unknown escape sequence \\%c", ch))
        case ('\'' : _):
            return LexError("Empty character constant")
        default:
            advance(2) $> LexError("Multi-character constant")

def string():
    lit("\"")

    while True:
        ch = peek()
        if ch == '\\':
            next_ch = next()
            if next_ch == 'n':
                ch = next()
                t = T.snoc(t, '\n')
            elif next_ch == '\\':
                ch = next()
                t = T.snoc(t, '\\')
            else:
                return LexError(formatString("Unknown escape sequence \\%c", next_ch))
        elif ch == '"':
            next()
            return TextVal("String", t)
        elif ch == '\n':
            return LexError("End-of-line while scanning string literal. Closing string character not found before end-of-line.")
        elif ch == '\0':
            return LexError("End-of-file while scanning string literal. Closing string character not found.")
        else:
            ch = next()
            t = T.snoc(t, ch)

def skipComment():
    lit("/*")

    while True:
        ch = peek()
        if ch == '\0':
            return LexError("End-of-file in comment. Closing comment characters not found.")
        elif ch == '*':
            next_ch = next()
            if next_ch == '/':
                return Skip
            else:
                ch = next_ch
        else:
            ch = next()

def nextToken():
    skipWhitespace()

    makeToken(skipComment() or keywords() or identifier() or integer() or character() or string() or operators() or symbols() or simpleToken("\0", "End_of_input") or LexError("Unrecognized character."))