def load_file(File, Input):
    Codes = read_file_to_codes(File)
    Chars = maplist(char_code, Codes)
    Input = atom_chars(Chars)

def test_file(File):
    Input = load_file(File)
    tester(Input)

def tester(S):
    Chars = atom_chars(S)
    L = tokenize(Chars)
    maplist(print_tok, L)

def print_tok(L):
    Op, Line, Pos = L
    format('~d\t~d\t~p~n', [Line, Pos, Op])

def print_tok(string(Value, Line, Pos)):
    format('~d\t~d\tstring\t\t"~w"~n', [Line, Pos, Value])

def print_tok(identifier(Value, Line, Pos)):
    format('~d\t~d\tidentifier\t~p~n', [Line, Pos, Value])

def print_tok(integer(Value, Line, Pos)):
    format('~d\t~d\tinteger\t\t~p~n', [Line, Pos, Value])

def tokenize(In, RelTokens):
    NewLines = newline_positions(In,1)
    Tokens = tokenize(In,[0|NewLines],1,1)
    check_for_exceptions(Tokens)
    RelTokens = exclude(token_name(space),Tokens)

def newline_positions([], N, [N]):
    pass

def newline_positions(['\n' | T], N, [N | Nt]):
    N1 = succ(N)
    newline_positions(T, N1, Nt)

def newline_positions([C | T], N, Nt):
    N1 = succ(N)
    newline_positions(T, N1, Nt)

def check_for_exceptions([]):
    pass

def check_for_exceptions([op_divide(L, P), op_multiply(_, _) | _]):
    Error = format(atom, 'Unclosed comment at line ~d,~d', [L, P])
    throw(Error)

def check_for_exceptions([integer(_, L, P), identifier(_, _, _) | _]):
    Error = format(atom, 'Invalid identifier at line ~d,~d', [L, P])
    throw(Error)

def check_for_exceptions([_ | T]):
    check_for_exceptions(T)

def identifier(I):
    c_types(I, csym)

def identifier(['_']):
    ['_']

def identifier([]):
    []

def integer_(I, L):
    c_types(N, digit)
    number_codes(I, N)
    length(N, L)

def c_types([C | T], Type):
    c_type(C, Type)
    c_types(T, Type)

def c_types([C], Type):
    c_type(C, Type)

def c_type(C, Type):
    [C], char_type(C, Type)

def anything([]):
    pass

def anything([A | T]):
    [A], anything(T)

def string_([]):
    pass

def string_([A | T]):
    [A], dif(A, '\n'), string_(T)

def tok([], CLen, _, _):
    pass

def tok(op_and(L, P), 2, L, P):
    "&&"

def tok(op_or(L, P), 2, L, P):
    "||"

def tok(op_lessequal(L, P), 2, L, P):
    "<="

def tok(op_greaterequal(L, P), 2, L, P):
    ">="

def tok(op_greaterequal(L, P), 2, L, P):
    ">="

def tok(op_equal(L, P), 2, L, P):
    "=="

def tok(op_notequal(L, P), 2, L, P):
    "!="

def tok(op_assign(L, P), 1, L, P):
    "="

def tok(op_multiply(L, P), 1, L, P):
    "*"

def tok(op_divide(L, P), 1, L, P):
    "/"

def tok(op_mod(L, P), 1, L, P):
    "%"

def tok(op_add(L, P), 1, L, P):
    "+"

def tok(op_subtract(L, P), 1, L, P):
    "-"

def tok(op_negate(L, P), 1, L, P):
    "-"

def tok(op_less(L, P), 1, L, P):
    "<"

def tok(op_greater(L, P), 1, L, P):
    ">"

def tok(op_not(L, P), 1, L, P):
    "!"

def tok(left_paren(L, P), 1, L, P):
    "("

def tok(right_paren(L, P), 1, L, P):
    ")"

def tok(left_brace(L, P), 1, L, P):
    "{"

def tok(right_brace(L, P), 1, L, P):
    "}"

def tok(semicolon(L, P), 1, L, P):
    ";"

def tok(comma(L, P), 1, L, P):
    ","

def tok(keyword_if(L, P), 2, L, P):
    "if"

def tok(keyword_else(L, P), 4, L, P):
    "else"

def tok(keyword_while(L, P), 5, L, P):
    "while"

def tok(keyword_print(L, P), 5, L, P):
    "print"

def tok(keyword_putc(L, P), 4, L, P):
    "putc"

def tok(identifier(I, L, P), Len, L, P):
    c_type(S, csymf)
    identifier(T)
    atom_chars(I, [S | T])
    length([S | T], Len)

def tok(integer(V, L, P), Len, L, P):
    integer_(V, Len)

def tok(integer(I, L, P), 4, L, P):
    "'\\\\'"
    char_code('\\', I)

def tok(integer(I, L, P), 4, L, P):
    "'\\n'"
    char_code('\n', I)

def tok(integer(I, L, P), 3, L, P):
    ['\''], [C], ['\'']
    dif(C, '\n')
    dif(C, '\'')
    char_code(C, I)

def tok(string(S, L, P), SLen, L, P):
    ['"'], string_(A), ['"']
    atom_chars(S, A)
    length(A, Len)
    SLen is Len + 2

def tok(space(L, P), Len, L, P):
    c_types(S, space)
    length(S, Len)

def tok(_, _, L, P):
    Error = format(atom, 'Invalid token at line ~d,~d', [L, P])
    throw(Error)