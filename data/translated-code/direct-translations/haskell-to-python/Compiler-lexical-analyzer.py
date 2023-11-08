```python
from typing import Tuple, List
import Control.Applicative
import Control.Monad.State.Lazy
import Control.Monad.Trans.Maybe
import Data.Char
import Data.Foldable
import Data.Functor
import Data.Text as T
import Prelude
import System.Environment
import System.IO
import Text.Printf

# Tokens
class Val:
    def __init__(self, value: int, name: str, text: Text, symbol: str, skip: bool, msg: str):
        self.value = value
        self.name = name
        self.text = text
        self.symbol = symbol
        self.skip = skip
        self.msg = msg

class Token:
    def __init__(self, val: Val, line: int, column: int):
        self.val = val
        self.line = line
        self.column = column

# Tokenizers
def makeToken(lexer: Val) -> Token:
    t, l, c = get()
    val = lexer

    if val.skip:
        return nextToken()

    elif val.msg:
        _, l_, c_ = get()
        code = T.take(c_ - c + 1, t)
        str_ = f"{val.msg}\n{' '*27}({l_}, {c_}): {code}"
        ch = peek()
        if ch != '\0':
            advance(1)
        return Token(LexError(str_), l, c)

    else:
        return Token(val, l, c)

def simpleToken(lexeme: str, name: str) -> Val:
    return SymbolVal(name) if lexeme == symbol else None

def makeTokenizers(pairs: List[Tuple[str, str]]) -> Val:
    return asum(map(simpleToken, pairs))

def keywords() -> Val:
    return makeTokenizers(
        [("if", "Keyword_if"), ("else", "Keyword_else"), ("while", "Keyword_while"),
         ("print", "Keyword_print"), ("putc", "Keyword_putc")])

def operators() -> Val:
    return makeTokenizers(
        [("*", "Op_multiply"), ("/", "Op_divide"), ("%", "Op_mod"), ("+", "Op_add"),
         ("-", "Op_subtract"), ("<=", "Op_lessequal"), ("<", "Op_less"), (">=", "Op_greaterequal"),
         (">", "Op_greater"), ("==", "Op_equal"), ("!=", "Op_notequal"), ("!", "Op_not"),
         ("=", "Op_assign"), ("&&", "Op_and"), ("||", "Op_or")])

def symbols() -> Val:
    return makeTokenizers(
        [("(", "LeftParen"), (")", "RightParen"),
         ("{", "LeftBrace"), ("}", "RightBrace"),
         (";", "Semicolon"), (",", "Comma")])

def isIdStart(ch: str) -> bool:
    return isAsciiLower(ch) or isAsciiUpper(ch) or ch == '_'

def isIdEnd(ch: str) -> bool:
    return isIdStart(ch) or isDigit(ch)

def identifier() -> Val:
    return TextVal("Identifier", lexeme)

def integer() -> Val:
    lexeme = some(isDigit)
    next_ch = peek()
    if isIdStart(next_ch):
        return LexError("Invalid number. Starts like a number, but ends in non-numeric characters.")
    else:
        num = int(lexeme)
        return IntVal(num)

def character() -> Val:
    lit("'")
    str_ = lookahead(3)
    if str_ == (ch + '\''):
        advance(2)
        return IntVal(ord(ch))
    elif str_ == "\\n'":
        advance(3)
        return IntVal(10)
    elif str_ == "\\\\'":
        advance(3)
        return IntVal(92)
    elif str_.startswith('\\'):
        advance(2)
        return LexError(f"Unknown escape sequence \\{ch}")
    elif str_.startswith('\''):
        return LexError("Empty character constant")
    else:
        advance(2)
        return LexError("Multi-character constant")

def string() -> Val:
    lit("\"")
    loop(T.pack(""), peek())

def skipComment() -> Val:
    lit("/*")
    loop(peek())

def nextToken() -> Token:
    skipWhitespace()
    makeToken([
        skipComment(),
        keywords(),
        identifier(),
        integer(),
        character(),
        string(),
        operators(),
        symbols(),
        simpleToken("\0", "End_of_input"),
        LexError("Unrecognized character.")
    ])

# File handling
def getIOHandles(args: List[str]) -> Tuple[IO, IO]:
    if len(args) == 0:
        return (stdin, stdout)
    elif len(args) == 1:
        inhandle = openFile(args[0], ReadMode)
        return (inhandle, stdout)
    else:
        inhandle = openFile(args[0], ReadMode)
        outhandle = openFile(args[1], WriteMode)
        return (inhandle, outhandle)

def withHandles(in_handle: IO, out_handle: IO, f: str) -> None:
    contents = hGetContents(in_handle)
    contents_ = contents + "\0"
    hPutStr(out_handle, f(contents_))
    if in_handle != stdin:
        hClose(in_handle)
    if out_handle != stdout:
        hClose(out_handle)

# Lexer
class LexerState:
    def __init__(self, t: Text, l: int, c: int):
        self.t = t
        self.l = l
        self.c = c

def lexerAdvance(n: int, ctx: LexerState) -> LexerState:
    if n == 0:
        return ctx
    elif n == 1:
        ch = ctx.t[0]
        if ch == '\n':
            return (ctx.t[1:], ctx.l + 1, 1)
        else:
            return (ctx.t[1:], ctx.l, ctx.c + 1)
    else:
        return lexerAdvance(n - 1, lexerAdvance(1, ctx))

def advance(n: int) -> None:
    modify(lexerAdvance(n, get()))

def peek() -> str:
    return get().t[0]

def lookahead(n: int) -> str:
    return T.take(n, get().t)

def next() -> str:
    advance(1)
    return peek()

def skipWhitespace() -> None:
    ch = peek()
    if ch in [" ", "\n"]:
        next()
        skipWhitespace()

def lit(lexeme: str) -> None:
    t, _, _ = get()
    if T.isPrefixOf(T.pack(lexeme), t):
        advance(len(lexeme))

def one(f: str) -> str:
    ch = peek()
    if f(ch):
        next()
        return ch
    return None

def lexerMany(f: str, ctx: LexerState) -> Tuple[Text, LexerState]:
    lexeme, _ = T.span(f, ctx.t)
    t_, l_, c_ = lexerAdvance(len(lexeme), ctx)
    return (lexeme, (t_, l_, c_))

def many(f: str) -> Text:
    return lexerMany(f, get())

def some(f: str) -> Text:
    return T.cons(one(f), many(f))

def lex(lexer: str, str_: str) -> List[str]:
    t = T.pack(str_)
    loop(lexer, (t, 1, 1))

# Main
def main() -> None:
    args = getArgs()
    hin, hout = getIOHandles(args)
    withHandles(hin, hout, printTokens(lex(nextToken)))

```