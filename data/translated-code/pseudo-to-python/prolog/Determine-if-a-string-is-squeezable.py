def squeeze_(Chars, SqueezeChar, Result):
    if len(Chars) == 0:
        Result = ""
    elif len(Chars) == 1:
        Result = Chars
    elif Chars[0] == SqueezeChar:
        squeeze_(Chars[1:], SqueezeChar, Result)
    elif Chars[0] == Chars[1]:
        squeeze_(Chars[1:], SqueezeChar, Result)
    elif Chars[0] != Chars[1]:
        Result = Chars[0] + squeeze_(Chars[1:], SqueezeChar, Result)
    return Result

def squeeze(Str, SqueezeChar, Collapsed):
    Chars = list(Str)
    Result = ""
    Result = squeeze_(Chars, SqueezeChar, Result)
    Collapsed = "".join(Result)