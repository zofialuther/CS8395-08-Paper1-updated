```python
all_syms = []
symbols = {}
key_words = {}
the_ch = " "
the_col = 0
the_line = 1
input_file = None

def error(line, col, msg):
    print(line, col, msg)
    exit(1)

def next_ch():
    global the_ch, the_col, the_line
    the_ch = input_file.read(1)
    the_col += 1
    if the_ch == '\n':
        the_line += 1
        the_col = 0
    return the_ch

def char_lit(err_line, err_col):
    global the_ch
    n = ord(the_ch)
    if the_ch == "'":
        error(err_line, err_col, "empty character constant")
    elif the_ch == "\\":
        the_ch = next_ch()
        if the_ch == 'n':
            n = 10
        elif the_ch == '\\':
            n = ord('\\')
        else:
            error(err_line, err_col, f"unknown escape sequence \\{the_ch}")
    if next_ch() != "'":
        error(err_line, err_col, "multi-character constant")
    next_ch()
    return "tk_Integer", err_line, err_col, n

def div_or_cmt(err_line, err_col):
    global the_ch
    if the_ch != '*':
        return "tk_Div", err_line, err_col
    the_ch = next_ch()
    while True:
        if the_ch == '*':
            if next_ch() == '/':
                next_ch()
                return gettok()
        elif len(the_ch) == 0:
            error(err_line, err_col, "EOF in comment")
        else:
            the_ch = next_ch()

def string_lit(start, err_line, err_col):
    global the_ch
    text = ""
    while the_ch != start:
        if len(the_ch) == 0:
            error(err_line, err_col, "EOF while scanning string literal")
        if the_ch == '\n':
            error(err_line, err_col, "EOL while scanning string literal")
        if the_ch == '\\':
            the_ch = next_ch()
            if the_ch != 'n':
                error(err_line, err_col, f"escape sequence unknown \\{the_ch}")
            the_ch = '\n'
        text += the_ch
        the_ch = next_ch()
    next_ch()
    return "tk_String", err_line, err_col, text

def ident_or_int(err_line, err_col):
    global the_ch
    is_number = True
    text = ""
    while the_ch.isalnum() or the_ch == '_':
        text += the_ch
        if not the_ch.isdigit():
            is_number = False
        the_ch = next_ch()
    if len(text) == 0:
        error(err_line, err_col, f"ident_or_int: unrecognized character: ({ord(the_ch)}) {the_ch}")
    if text[0].isdigit():
        if is_number == False:
            error(err_line, err_col, f"invalid number: {text}")
        n = int(text)
        return "tk_Integer", err_line, err_col, n
    if text in key_words:
        return key_words[text], err_line, err_col
    return "tk_Ident", err_line, err_col, text

def follow(expect, ifyes, ifno, err_line, err_col):
    global the_ch
    if the_ch == expect:
        the_ch = next_ch()
        return ifyes, err_line, err_col
    if ifno == "tk_EOI":
        error(err_line, err_col, f"follow: unrecognized character: ({ord(the_ch)}) {the_ch}")
    return ifno, err_line, err_col

def gettok():
    global the_ch, the_line, the_col
    while the_ch.isspace():
        the_ch = next_ch()
    err_line = the_line
    err_col = the_col
    if len(the_ch) == 0:
        return "tk_EOI", err_line, err_col
    elif the_ch == '/':
        return div_or_cmt(err_line, err_col)
    elif the_ch == "'":
        return char_lit(err_line, err_col)
    elif the_ch == '<':
        return follow('=', "tk_Leq", "tk_Lss", err_line, err_col)
    elif the_ch == '>':
        return follow('=', "tk_Geq", "tk_Gtr", err_line, err_col)
    elif the_ch == '=':
        return follow('=', "tk_Eq", "tk_Assign", err_line, err_col)
    elif the_ch == '!':
        return follow('=', "tk_Neq", "tk_Not", err_line, err_col)
    elif the_ch == '&':
        return follow('&', "tk_And", "tk_EOI", err_line, err_col)
    elif the_ch == '|':
        return follow('|', "tk_Or", "tk_EOI", err_line, err_col)
    elif the_ch == '"':
        return string_lit(the_ch, err_line, err_col)
    elif the_ch in symbols:
        sym = symbols[the_ch]
        the_ch = next_ch()
        return sym, err_line, err_col
    else:
        return ident_or_int(err_line, err_col)

import sys
input_file = sys.stdin
if len(sys.argv) > 1:
    try:
        input_file = open(sys.argv[1], 'r', 4096)
    except IOError as e:
        error(0, 0, f"Can't open {sys.argv[1]}")

while True:
    t = gettok()
    tok = t[0]
    line = t[1]
    col = t[2]
    print(f"{line:5d}  {col:5d}   {all_syms[tok]:-14s}", end='')
    if tok == "tk_Integer":
        print(f"   {t[3]:5d}")
    elif tok == "tk_Ident":
        print(f"  {t[3]:s}")
    elif tok == "tk_String":
        print(f'  "{t[3]:s}"')
    else:
        print("")
    if tok == "tk_EOI":
        break
```