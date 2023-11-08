def commentstripper(sample):
    result = ""
    insideComment = False
    insideString = False
    for c in sample:
        if not insideString:
            if c == '/' and sample[sample.index(c)+1] == '*':
                insideComment = True
            elif c == '*' and sample[sample.index(c)+1] == '/':
                insideComment = False
            elif not insideComment:
                result += c
    return result

def test():
    print('\nNON-NESTED BLOCK COMMENT EXAMPLE:')
    sample = "/* This is a block comment */ This is not a comment"
    print(commentstripper(sample))
    print('\nNESTED BLOCK COMMENT EXAMPLE:')
    sample = "/* This is a block comment /* Nested block comment */ This is not a comment */"
    print(commentstripper(sample))

if __name__ == '__main__':
    test()