def collapse_(chars, result):
    if len(chars) == 0:
        result = []
    elif len(chars) == 1:
        result = chars
    elif chars[0] == chars[1]:
        collapse_(chars[1:], result)
    else:
        result = [chars[0]]
        collapse_(chars[1:], result)
    return result

def collapse(string, collapsed):
    chars = list(string)
    result = collapse_(chars, [])
    collapsed = ''.join(result)
    return collapsed
